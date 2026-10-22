#!/usr/bin/env python3
"""
Validate Markdown repository: internal links, anchors and GFM tables.

Checks (exit code 1 if any issue found):
  1. Internal links: every relative link [text](target) in *.md and llms.txt
     must resolve to an existing file in the repo.
  2. Anchors: every intra-document link [text](#anchor) must match a heading
     slug in the same document (GitHub-slugger compatible).
  3. Tables: every table must have
     - a valid delimiter row (second line: only | : - spaces, pipe count = header),
     - a blank line (or heading/hr/blockquote) before the table start,
     - no raw "|" inside inline code spans in cells (breaks rendering; use \\|).

Used by CI (.github/workflows/ci.yml). Run locally: python3 scripts/validate_markdown.py
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ERRORS = []
WARNINGS = []


def err(path, line_no, msg):
    ERRORS.append(f"{path}:{line_no}: {msg}")


def warn(path, line_no, msg):
    WARNINGS.append(f"{path}:{line_no}: {msg}")


def md_files():
    files = [REPO / "README.md", REPO / "index.md"]
    files += sorted((REPO / "docs").glob("*.md"))
    return [f for f in files if f.is_file()]


def strip_code_blocks(lines):
    """Replace fenced code block content with blank lines, keep line numbers."""
    out = []
    in_code = False
    fence_re = re.compile(r"^\s*(```|~~~)")
    for ln in lines:
        if fence_re.match(ln):
            in_code = not in_code
            out.append("")
            continue
        out.append("" if in_code else ln)
    return out


def github_slug(text):
    """GitHub-slugger compatible anchor."""
    text = text.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)  # drop punctuation (keep letters, digits, _, -, space)
    text = re.sub(r" ", "-", text)
    return text


def split_cells(row):
    """Split table row into cells, honouring \\| escapes and inline code spans."""
    cells = []
    cur = []
    i = 0
    in_code = False
    while i < len(row):
        ch = row[i]
        if ch == "`":
            in_code = not in_code
            cur.append(ch)
        elif ch == "\\" and i + 1 < len(row) and row[i + 1] == "|":
            cur.append("\\|")
            i += 1
        elif ch == "|" and not in_code:
            cells.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
        i += 1
    cells.append("".join(cur))
    return cells


def count_cells(row):
    return len(split_cells(row))


def raw_pipe_in_code(row):
    """Yield positions of unescaped | inside backtick spans."""
    i = 0
    in_code = False
    hits = []
    while i < len(row):
        ch = row[i]
        if ch == "`":
            in_code = not in_code
        elif ch == "|" and in_code:
            if i == 0 or row[i - 1] != "\\":
                hits.append(i)
        i += 1
    return hits


DELIM_RE = re.compile(r"^[\s|:\-]+$")
BLOCK_START_RE = re.compile(r"^(#|\||>|`{3,}|~{3,}|[-*_]\s*[-*_\s]*$)")


def check_tables(path, rel, lines):
    lines = strip_code_blocks(lines)
    n = len(lines)
    i = 0
    while i < n:
        ln = lines[i]
        if "|" not in ln:
            i += 1
            continue
        # potential table start: current line has |, next line is delimiter
        if i + 1 < n and "|" in lines[i + 1] and DELIM_RE.match(lines[i + 1]) \
                and "-" in lines[i + 1] \
                and count_cells(ln) == count_cells(lines[i + 1]):
            header_cells = count_cells(ln)
            # blank line / heading / hr / blockquote before table?
            if i > 0:
                prev = lines[i - 1].strip()
                if prev and not BLOCK_START_RE.match(prev):
                    err(rel, i + 1, "таблица не отделена пустой строкой от текста — GitHub не отрендерит её")
            # rows
            j = i
            while j < n and "|" in lines[j]:
                row = lines[j]
                if raw_pipe_in_code(row):
                    err(rel, j + 1, "неэкранированный | внутри inline-кода в ячейке — экранируйте как \\|")
                if j > i + 1:  # body rows (skip header & delimiter)
                    c = count_cells(row)
                    if c != header_cells:
                        warn(rel, j + 1, f"число ячеек {c} != заголовка {header_cells}")
                j += 1
            i = j
        else:
            i += 1


def check_links(path, rel, text, headings):
    lines = strip_code_blocks(text.splitlines())
    for idx, ln in enumerate(lines, 1):
        for m in re.finditer(r"\[[^\]]*\]\(\s*([^)]*?)\s*\)", ln):
            target = m.group(1)
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.startswith("#"):
                anchor = target[1:]
                if anchor and anchor not in headings:
                    err(rel, idx, f"якорь #{anchor} не найден среди заголовков")
                continue
            file_part = target.split("#")[0]
            if not file_part:
                continue
            base = REPO if path.suffix == ".txt" else path.parent  # llms.txt links are repo-root-relative
            if not (base / file_part).is_file():
                err(rel, idx, f"относительная ссылка ведёт на несуществующий файл: {file_part}")


def collect_headings(text):
    lines = strip_code_blocks(text.splitlines())
    return {github_slug(re.sub(r"^#+\s*", "", ln)) for ln in lines if re.match(r"^#{1,6}\s", ln)}


def main():
    for f in md_files():
        rel = f.relative_to(REPO).as_posix()
        text = f.read_text(encoding="utf-8")
        check_links(f, rel, text, collect_headings(text))
        check_tables(f, rel, text.splitlines())

    llms = REPO / "llms.txt"
    if llms.is_file():
        check_links(llms, "llms.txt", llms.read_text(encoding="utf-8"), set())

    print(f"Проверено файлов: {len(md_files()) + 1}")
    if WARNINGS:
        print(f"\nПредупреждения (не блокируют CI): {len(WARNINGS)}")
        for w in WARNINGS[:20]:
            print(f"  WARN {w}")
        if len(WARNINGS) > 20:
            print(f"  … и ещё {len(WARNINGS) - 20}")
    if ERRORS:
        print(f"\nОШИБКИ: {len(ERRORS)}")
        for e in ERRORS[:40]:
            print(f"  ERROR {e}")
        if len(ERRORS) > 40:
            print(f"  … и ещё {len(ERRORS) - 40}")
        sys.exit(1)
    print("\nOK: внутренних битых ссылок, якорей и сломанных таблиц не найдено.")


if __name__ == "__main__":
    main()
