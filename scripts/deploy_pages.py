#!/usr/bin/env python3
"""
Deploy GitHub Pages (docsify) для репозитория ozon-api.

Режимы:
    python3 scripts/deploy_pages.py init   — создать ветку gh-pages из текущего main,
                                              сгенерировать docsify-ассеты, запушить
    python3 scripts/deploy_pages.py sync   — обновить gh-pages из origin/main,
                                              перегенерировать ассеты, запушить

Ассеты (в корне gh-pages): index.html (docsify), _sidebar.md, _navbar.md, .nojekyll
Библиотеки вендорены в assets/vendor/ (docsify 4.13.1, prism-json, search, copy-code) — без CDN.
Сайт: https://teliy.github.io/ozon-api/ — рендеринг Markdown на лету, поиск, подсветка кода,
светлая/тёмная тема (переключатель + prefers-color-scheme + localStorage), мобильная версия.
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

# Одинаковые H1 в разных файлах — развязка подписей сайдбара (07 и 41 оба «Акции Ozon»)
SIDEBAR_OVERRIDES = {
    "41-actions-ozon-2": "Акции Ozon — авто-добавление товаров",
}

INDEX_HTML = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ozon Seller API — справочник</title>
  <meta name="description" content="Справочник Ozon Seller API 2.1: 482 метода, схемы тел запросов и ответов, примеры.">
  <meta name="theme-color" content="#ffffff">
  <link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
  <script>
    (function () {
      var saved = null;
      try { saved = localStorage.getItem('ozon-theme'); } catch (e) {}
      var theme = (saved === 'light' || saved === 'dark') ? saved
        : (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
      document.documentElement.setAttribute('data-theme', theme);
    })();
  </script>
  <link rel="stylesheet" href="assets/vendor/vue.css">
  <style>
    :root{
      color-scheme:light;--theme-color:#005bff;
      --bg:#ffffff;--bg-soft:#f7f8fa;--text:#24292f;--muted:#5a6772;--accent:#005bff;
      --border:#e8eaee;--code-bg:#f4f5f7;--th-bg:#f2f4f7;--row-alt:#f8f8f8;
      --toggle-shadow:0 2px 10px rgba(1,4,9,.16);
    }
    html[data-theme="dark"]{
      color-scheme:dark;--theme-color:#4da3ff;
      --bg:#0d1117;--bg-soft:#121823;--text:#e6edf3;--muted:#93a1b0;--accent:#4da3ff;
      --border:#28313d;--code-bg:#161b24;--th-bg:#151b26;--row-alt:#151b26;
      --toggle-shadow:0 2px 10px rgba(0,0,0,.5);
    }
    *{scrollbar-width:thin;scrollbar-color:var(--border) transparent}
    body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Oxygen,Ubuntu,'Helvetica Neue',Arial,sans-serif;
         background:var(--bg);color:var(--text)}
    body,.sidebar,.app-nav,.markdown-section,.markdown-section pre,.markdown-section table th,
    .search input,#theme-toggle{transition:background-color .25s ease,color .25s ease,border-color .25s ease}

    /* Сайдбар */
    .sidebar{background:var(--bg-soft);border-right:1px solid var(--border);padding-top:1.6rem}
    .sidebar>h1 a{color:var(--accent);font-weight:700}
    .sidebar a,.sidebar ul li a{color:var(--text)}
    .sidebar a:hover,.sidebar a.active{color:var(--accent)}
    .sidebar li>a.active{border-right:2px solid var(--accent)}
    .sidebar li strong{display:block;margin-top:14px;color:var(--accent);font-size:.72em;
                       text-transform:uppercase;letter-spacing:.05em}
    .sidebar-toggle{background-color:var(--bg) !important;border-color:var(--border) !important}

    /* Контент */
    a,.markdown-section a{color:var(--accent)}
    .markdown-section{color:var(--text)}
    .markdown-section h1{font-size:1.9rem;overflow-wrap:anywhere}
    .markdown-section h2{margin-top:2.6em;padding-bottom:.3em;border-bottom:1px solid var(--border);overflow-wrap:anywhere}
    .markdown-section h3,.markdown-section h4{overflow-wrap:anywhere}
    .markdown-section blockquote{border-left:4px solid var(--accent);background:var(--bg-soft);color:var(--text);
      padding:.55em 1em;margin:1em 0;border-radius:0 8px 8px 0}
    .markdown-section table{display:block;overflow-x:auto;-webkit-overflow-scrolling:touch;border-collapse:collapse}
    .markdown-section table th{background:var(--th-bg)}
    .markdown-section table th,.markdown-section table td{border-color:var(--border)}
    .markdown-section tr:nth-child(2n){background-color:var(--row-alt)}
    .markdown-section code{background:var(--code-bg)}
    html[data-theme="dark"] .markdown-section code{color:#a5d6ff}
    .markdown-section pre{background:var(--code-bg)}
    .markdown-section pre>code{background:transparent}

    /* Prism: тёмная палитра токенов */
    html[data-theme="dark"] .token.punctuation{color:#c9d1d9}
    html[data-theme="dark"] .token.property,html[data-theme="dark"] .token.class-name{color:#7ee787}
    html[data-theme="dark"] .token.string,html[data-theme="dark"] .token.char{color:#a5d6ff}
    html[data-theme="dark"] .token.number{color:#79c0ff}
    html[data-theme="dark"] .token.boolean,html[data-theme="dark"] .token.constant{color:#ffa657}
    html[data-theme="dark"] .token.keyword,html[data-theme="dark"] .token.operator{color:#ff7b72}

    /* Поиск */
    .search{border-bottom:1px solid var(--border)}
    .search input{background:var(--bg);color:var(--text);border:1px solid var(--border);border-radius:6px}
    .search .matching-post{color:var(--text)}
    .search em{color:var(--accent);font-style:normal;font-weight:700}

    /* Навбар */
    .app-nav a{color:var(--text)}
    .app-nav a:hover{color:var(--accent)}

    /* Кнопка копирования кода */
    .docsify-copy-code-button{background:var(--bg-soft);color:var(--muted);border:1px solid var(--border)}
    @media (hover:none){.docsify-copy-code-button{opacity:1 !important}}

    /* Переключатель темы */
    #theme-toggle{position:fixed;bottom:18px;right:18px;z-index:130;width:44px;height:44px;border-radius:50%;
      border:1px solid var(--border);background:var(--bg);color:var(--text);cursor:pointer;
      display:flex;align-items:center;justify-content:center;box-shadow:var(--toggle-shadow);
      -webkit-tap-highlight-color:transparent}
    #theme-toggle:hover{border-color:var(--accent);color:var(--accent)}
    #theme-toggle:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
    #theme-toggle svg{width:20px;height:20px}
    html[data-theme="light"] #theme-toggle .icon-sun{display:none}
    html[data-theme="dark"] #theme-toggle .icon-moon{display:none}

    /* Мобильная версия */
    @media screen and (max-width:768px){
      .markdown-section{padding:22px 16px 40px}
      .markdown-section h1{font-size:1.5rem}
      .markdown-section h2{font-size:1.22rem;margin-top:2em}
      .markdown-section table{font-size:.9em}
      .markdown-section blockquote{padding:.5em .8em}
      #theme-toggle{bottom:14px;right:14px;width:48px;height:48px}
      .app-nav{position:fixed;top:0;left:0;right:0;margin:0;padding:8px 16px;background:var(--bg-soft);
               border-bottom:1px solid var(--border);display:flex;justify-content:flex-end;z-index:110}
      .app-nav ul{display:flex;gap:0 18px;margin:0;padding:0}
      body{padding-top:44px}
    }
  </style>
</head>
<body>
  <div id="app"></div>
  <button id="theme-toggle" type="button" aria-label="Переключить тему" title="Переключить тему">
    <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>
    <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
  </button>
  <script>
    window.$docsify = {
      name: 'Ozon Seller API',
      nameLink: '/',
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
      },
      copyCode: {
        buttonText: 'Копировать',
        errorText: 'Ошибка',
        successText: 'Скопировано'
      }
    };
    (function () {
      var root = document.documentElement;
      var btn = document.getElementById('theme-toggle');
      var meta = document.querySelector('meta[name="theme-color"]');
      function sync() {
        var dark = root.getAttribute('data-theme') === 'dark';
        btn.setAttribute('aria-pressed', dark ? 'true' : 'false');
        if (meta) meta.setAttribute('content', dark ? '#0d1117' : '#ffffff');
      }
      sync();
      btn.addEventListener('click', function () {
        var t = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
        root.setAttribute('data-theme', t);
        try { localStorage.setItem('ozon-theme', t); } catch (e) {}
        sync();
      });
      var mq = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)');
      if (mq && mq.addEventListener) {
        mq.addEventListener('change', function (e) {
          var saved = null;
          try { saved = localStorage.getItem('ozon-theme'); } catch (err) {}
          if (!saved) { root.setAttribute('data-theme', e.matches ? 'dark' : 'light'); sync(); }
        });
      }
    })();
  </script>
  <script src="assets/vendor/docsify.min.js"></script>
  <script src="assets/vendor/prism-json.min.js"></script>
  <script src="assets/vendor/search.min.js"></script>
  <script src="assets/vendor/docsify-copy-code.min.js"></script>
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
            lines.append(f"  - [{SIDEBAR_OVERRIDES.get(s, h1_of(s))}](docs/{s}.md)")
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
