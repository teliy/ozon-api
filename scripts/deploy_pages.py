#!/usr/bin/env python3
"""
Deploy GitHub Pages (docsify) для репозитория ozon-api.

Режимы:
    python3 scripts/deploy_pages.py init   — создать ветку gh-pages из текущего main,
                                              сгенерировать docsify-ассеты, запушить
    python3 scripts/deploy_pages.py sync   — обновить gh-pages из origin/main,
                                              перегенерировать ассеты, запушить

Ассеты (в корне gh-pages): index.html (docsify), _sidebar.md, _navbar.md, .nojekyll
Сайт: https://teliy.github.io/ozon-api/ — рендеринг Markdown на лету, поиск, подсветка кода.
"""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Группировка разделов для сайдбара (все 62 файла docs/)
GROUPS = [
    ("Руководство", ["00-guides"]),
    ("Доступ и кабинет", ["01-api-key", "02-seller-info"]),
    ("Товары и контент", ["03-attributes", "04-products", "05-barcodes",
                          "06-prices-stocks", "34-digital-goods"]),
    ("Акции и ценообразование", ["07-actions-ozon", "08-pricing-strategies",
                                 "40-seller-promotions", "41-actions-ozon-2"]),
    ("Сертификаты", ["09-certificates-brands", "10-quality-certificates"]),
    ("Склады и полигоны", ["11-warehouses-fbs-rfbs", "12-warehouses-fbs",
                           "13-warehouses-rfbs-express", "15-polygons"]),
    ("Заказы и отправления FBS/rFBS", ["14-postings-fbs-rfbs", "26-order-cancellations",
                                      "56-cancel-reasons", "57-delivery-info",
                                      "58-orders", "59-postings-info"]),
    ("Маркировка и сборка", ["19-marking-codes"]),
    ("FBO", ["16-fbo-delivery", "17-fbo-supplies", "18-fbo-warehouses",
             "43-fbo-cargoplaces", "53-fbo-acts"]),
    ("FBP", ["44-fbp-drafts", "45-fbp-drafts-direct", "46-fbp-drafts-dropoff",
             "47-fbp-drafts-pickup", "48-fbp-supplies-direct", "49-fbp-supplies-dropoff",
             "50-fbp-supplies-pickup", "51-fbp-supply"]),
    ("Доставка FBS/rFBS", ["20-fbs-delivery", "21-rfbs-delivery", "22-passes",
                           "55-ozon-delivery", "52-fbs-cargoplaces"]),
    ("Возвраты", ["23-returns-fbo-fbs", "24-returns-rfbs", "25-return-shipments"]),
    ("Общение с покупателями", ["27-chats", "35-reviews", "36-questions-answers"]),
    ("Отчёты и финансы", ["28-invoices", "29-reports", "30-analytics",
                          "31-finance-reports", "32-receipts", "33-seller-rating"]),
    ("Уведомления", ["42-push-notifications", "99-notifications"]),
    ("Прочее", ["37-beta-methods", "38-misc-methods", "39-rabota-s-kvantami",
                "54-premium", "60-common-errors"]),
]

INDEX_HTML = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ozon Seller API — справочник</title>
  <meta name="description" content="Справочник Ozon Seller API 2.1: 482 метода, схемы тел запросов и ответов, примеры.">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/docsify@4/lib/themes/vue.css">
  <style>
    body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Oxygen,Ubuntu,'Helvetica Neue',Arial,sans-serif}
    .sidebar{background:#f7f8fa;border-right:1px solid #e8eaee;padding-top:1.6rem}
    .sidebar>h1 a{color:#005bff;font-weight:700}
    .sidebar a{color:#333}
    .sidebar a:hover,.sidebar a.active{color:#005bff}
    .sidebar li>a.active{border-right:2px solid #005bff}
    .sidebar li strong{display:block;margin-top:14px;color:#005bff;font-size:.72em;
                       text-transform:uppercase;letter-spacing:.05em}
    a,.markdown-section a{color:#005bff}
    .markdown-section h1{font-size:1.9rem}
    .markdown-section h2{margin-top:2.6em;padding-bottom:.3em;border-bottom:1px solid #e8eaee}
    .markdown-section table{display:block;overflow-x:auto;border-collapse:collapse}
    .markdown-section table th{background:#f2f4f7}
    .markdown-section code{background:#f4f5f7}
    .search input{border-radius:6px}
  </style>
</head>
<body>
  <div id="app"></div>
  <script>
    window.$docsify = {
      name: 'Ozon Seller API',
      nameLink: '/',
      repo: 'teliy/ozon-api',
      homepage: 'index.md',
      loadSidebar: true,
      loadNavbar: true,
      subMaxLevel: 2,
      auto2top: true,
      topMargin: 56,
      search: {
        paths: 'auto',
        placeholder: 'Поиск по справочнику…',
        noData: 'Ничего не найдено',
        depth: 3
      }
    };
  </script>
  <script src="https://cdn.jsdelivr.net/npm/docsify@4/lib/docsify.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-json.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/docsify@4/lib/plugins/search.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/docsify-copy-code@2/dist/docsify-copy-code.min.js"></script>
</body>
</html>
"""

NAVBAR = """- [GitHub](https://github.com/teliy/ozon-api)
- [docs.ozon.ru](https://docs.ozon.ru/api/seller/)
- [llms.txt](llms.txt)
"""


def sh(*args):
    r = subprocess.run(args, cwd=REPO, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"git failed: {' '.join(args)}\n{r.stderr}")
    return r.stdout.strip()


def h1_of(stem):
    """Вернуть H1-заголовок файла docs/<stem>.md."""
    p = REPO / "docs" / f"{stem}.md"
    for ln in p.read_text(encoding="utf-8").split("\n"):
        if ln.startswith("# "):
            return ln[2:].strip()
    return stem


def build_sidebar():
    lines = ["- [Шпаргалка: все endpoints](index.md)"]
    covered = [s for _, stems in GROUPS for s in stems]
    actual = sorted(f.stem for f in (REPO / "docs").glob("*.md"))
    missing = set(actual) - set(covered)
    if missing:
        sys.exit(f"В SIDEBAR-группах не учтены файлы: {sorted(missing)}")
    for group, stems in GROUPS:
        lines.append(f"- **{group}**")
        for s in stems:
            lines.append(f"  - [{h1_of(s)}](docs/{s}.md)")
    return "\n".join(lines) + "\n"


def write_assets():
    (REPO / "index.html").write_text(INDEX_HTML, encoding="utf-8")
    (REPO / "_navbar.md").write_text(NAVBAR, encoding="utf-8")
    (REPO / "_sidebar.md").write_text(build_sidebar(), encoding="utf-8")
    (REPO / ".nojekyll").write_text("", encoding="utf-8")
    print("Ассеты записаны: index.html, _sidebar.md, _navbar.md, .nojekyll")


def init():
    sh("git", "checkout", "-b", "gh-pages")
    write_assets()
    sh("git", "add", "index.html", "_sidebar.md", "_navbar.md", ".nojekyll")
    sh("git", "commit", "-m", "GitHub Pages: docsify-просмотр справочника (сайдбар, поиск, подсветка)")
    sh("git", "push", "-u", "origin", "gh-pages")
    print("Ветка gh-pages создана и запушена. Сайт: https://teliy.github.io/ozon-api/")


def sync():
    sh("git", "fetch", "origin")
    sh("git", "checkout", "gh-pages")
    sh("git", "pull", "origin", "gh-pages")
    sh("git", "merge", "origin/main", "--no-edit")
    write_assets()
    sh("git", "add", "index.html", "_sidebar.md", "_navbar.md", ".nojekyll")
    if sh("git", "status", "--porcelain"):
        sh("git", "commit", "-m", "GitHub Pages: синхронизация с main")
        sh("git", "push", "origin", "gh-pages")
        print("gh-pages обновлён и запушен.")
    else:
        print("Изменений нет.")
    sh("git", "checkout", "main")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "sync"
    {"init": init, "sync": sync}[mode]()
