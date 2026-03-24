#!/usr/bin/env python3
"""generate_html.py — Build one HTML page per GDD section.

Usage:
    python3 generate_html.py

Output:
    index.html              — navigation hub (repo root)
    docs/*.html             — core section pages
    docs/farm/*.html        — farm section pages
    docs/store/*.html       — store section pages
    docs/systems/*.html     — systems section pages
"""

import os
import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))

# ── Ordered master list of all GDD pages ──────────────────────────────────────
# Each entry: (md_path_relative_to_ROOT, display_title, group_label)
PAGES = [
    ("docs/01-game-overview.md",              "01 — Game Overview",            "🌐 Core"),
    ("docs/02-core-game-loop.md",             "02 — Core Game Loop",           "🌐 Core"),
    ("docs/03-currency-system.md",            "03 — Currency System",          "🌐 Core"),
    ("docs/04-leveling-xp.md",                "04 — Leveling & XP",            "🌐 Core"),
    ("docs/05-unified-game-world.md",         "05 — Unified Game World",       "🌐 Core"),
    ("docs/farm/06-farm-overview.md",         "06 — Farm Overview",            "🌾 Farm"),
    ("docs/farm/07-crop-system.md",           "07 — Crop System",              "🌾 Farm"),
    ("docs/farm/08-animal-husbandry.md",      "08 — Animal Husbandry",         "🌾 Farm"),
    ("docs/farm/09-processing-buildings.md",  "09 — Processing Buildings",     "🌾 Farm"),
    ("docs/farm/10-crafting-chains.md",       "10 — Crafting Chains",          "🌾 Farm"),
    ("docs/farm/11-farm-workers.md",          "11 — Farm Workers",             "🌾 Farm"),
    ("docs/farm/12-seasons-weather.md",       "12 — Seasons & Weather",        "🌾 Farm"),
    ("docs/farm/13-farm-mastery.md",          "13 — Farm Mastery",             "🌾 Farm"),
    ("docs/farm/14-farm-expansion.md",        "14 — Farm Expansion",           "🌾 Farm"),
    ("docs/store/15-store-grid-layout.md",    "15 — Store Grid & Layout",      "🏪 Store"),
    ("docs/store/16-supply-modes.md",         "16 — Supply Modes",             "🏪 Store"),
    ("docs/store/17-displays-all.md",         "17 — Displays — All Categories","🏪 Store"),
    ("docs/store/18-coin-op-items.md",        "18 — Coin-Op Items",            "🏪 Store"),
    ("docs/store/19-attractions.md",          "19 — Attractions",              "🏪 Store"),
    ("docs/store/20-decorations.md",          "20 — Decorations",              "🏪 Store"),
    ("docs/store/21-store-expansion.md",      "21 — Store Expansion",          "🏪 Store"),
    ("docs/systems/22-supply-chain.md",       "22 — Supply Chain",             "⚙️ Systems"),
    ("docs/systems/23-suppliers-shipments.md","23 — Suppliers & Shipments",    "⚙️ Systems"),
    ("docs/systems/24-stockroom.md",          "24 — Stockroom",                "⚙️ Systems"),
    ("docs/systems/25-customer-system.md",    "25 — Customer System",          "⚙️ Systems"),
    ("docs/systems/26-card-system.md",        "26 — Card System",              "⚙️ Systems"),
    ("docs/systems/27-quest-system.md",       "27 — Quest System",             "⚙️ Systems"),
    ("docs/systems/28-collections.md",        "28 — Collections",              "⚙️ Systems"),
    ("docs/systems/29-campaigns.md",          "29 — Campaigns",                "⚙️ Systems"),
    ("docs/systems/30-luxury-points.md",      "30 — Luxury Points",            "⚙️ Systems"),
    ("docs/systems/31-mastery-stars.md",      "31 — Mastery Stars",            "⚙️ Systems"),
    ("docs/systems/32-special-events.md",     "32 — Special Events",           "⚙️ Systems"),
    ("docs/systems/33-achievements.md",       "33 — Achievements",             "⚙️ Systems"),
    ("docs/systems/34-level-unlock-table.md", "34 — Level Unlock Table",       "⚙️ Systems"),
    ("docs/systems/35-monetization.md",       "35 — Monetization",             "⚙️ Systems"),
    ("docs/systems/36-technical-systems.md",  "36 — Technical Systems",        "⚙️ Systems"),
    ("docs/37-complete-game-mechanics.md",     "37 — Complete Game Mechanics",  "📖 Reference"),
]

# ── Shared CSS ─────────────────────────────────────────────────────────────────
CSS = """
  :root {
    --bg: #0f1117;
    --surface: #1a1d27;
    --surface2: #22263a;
    --accent: #4f8ef7;
    --accent2: #38c172;
    --text: #e2e8f0;
    --muted: #8892a4;
    --border: #2d3348;
    --radius: 10px;
    --max-w: 860px;
  }
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; }
  body {
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.7;
    padding: 0 1rem 3rem;
  }
  a { color: var(--accent); text-decoration: none; }
  a:hover { text-decoration: underline; }

  /* ── Top bar ── */
  .topbar {
    position: sticky; top: 0; z-index: 100;
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    padding: .6rem 1rem;
    display: flex; align-items: center; gap: .8rem;
    font-size: .88rem;
  }
  .topbar .home-link { font-weight: 700; font-size: 1rem; color: var(--text); }
  .topbar .home-link:hover { color: var(--accent); text-decoration: none; }
  .topbar .spacer { flex: 1; }
  .topbar .group-badge {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: .2rem .7rem;
    font-size: .78rem;
    color: var(--muted);
  }

  /* ── Page content ── */
  .page-wrap {
    max-width: var(--max-w);
    margin: 2.5rem auto 0;
  }

  /* ── Markdown body ── */
  .md-body h1 { font-size: 2rem; font-weight: 800; margin-bottom: 1rem; color: var(--text); }
  .md-body h2 { font-size: 1.4rem; font-weight: 700; margin: 2rem 0 .6rem; border-bottom: 1px solid var(--border); padding-bottom: .3rem; }
  .md-body h3 { font-size: 1.1rem; font-weight: 600; margin: 1.4rem 0 .4rem; color: var(--accent); }
  .md-body h4 { font-size: 1rem; font-weight: 600; margin: 1rem 0 .3rem; color: var(--accent2); }
  .md-body p { margin: .6rem 0; }
  .md-body ul, .md-body ol { margin: .5rem 0 .5rem 1.5rem; }
  .md-body li { margin: .25rem 0; }
  .md-body strong { color: #fff; }
  .md-body em { color: #cbd5e1; }
  .md-body blockquote {
    border-left: 3px solid var(--accent);
    padding: .5rem 1rem;
    margin: 1rem 0;
    background: var(--surface2);
    border-radius: 0 var(--radius) var(--radius) 0;
    color: var(--muted);
  }
  .md-body code {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: .1rem .35rem;
    font-size: .88em;
    font-family: 'Fira Code', 'Consolas', monospace;
  }
  .md-body pre {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1rem 1.2rem;
    overflow-x: auto;
    margin: .8rem 0;
  }
  .md-body pre code { background: none; border: none; padding: 0; font-size: .85em; }
  .md-body hr { border: none; border-top: 1px solid var(--border); margin: 1.5rem 0; }
  .md-body table {
    border-collapse: collapse;
    width: 100%;
    margin: 1rem 0;
    font-size: .9rem;
  }
  .md-body th {
    background: var(--surface2);
    text-align: left;
    padding: .5rem .8rem;
    border: 1px solid var(--border);
    color: var(--accent);
    font-weight: 600;
  }
  .md-body td {
    padding: .45rem .8rem;
    border: 1px solid var(--border);
    vertical-align: top;
  }
  .md-body tr:nth-child(even) td { background: rgba(255,255,255,.03); }

  /* ── Prev / Next nav ── */
  .page-nav {
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    margin-top: 3rem;
    padding-top: 1.5rem;
    border-top: 1px solid var(--border);
  }
  .nav-btn {
    display: inline-flex;
    align-items: center;
    gap: .4rem;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: .6rem 1rem;
    color: var(--text);
    font-size: .9rem;
    transition: border-color .2s, background .2s;
    max-width: 48%;
  }
  .nav-btn:hover { border-color: var(--accent); background: var(--surface2); text-decoration: none; }
  .nav-btn.next { margin-left: auto; text-align: right; }
  .nav-label { font-size: .72rem; color: var(--muted); display: block; }

  /* ── Index page ── */
  .hero {
    text-align: center;
    padding: 3rem 1rem 2rem;
  }
  .hero h1 { font-size: 2.6rem; font-weight: 900; letter-spacing: -.5px; }
  .hero .sub { color: var(--muted); margin-top: .5rem; font-size: 1.05rem; }
  .hero .badges { margin-top: 1rem; display: flex; flex-wrap: wrap; justify-content: center; gap: .5rem; }
  .badge {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: .25rem .8rem;
    font-size: .8rem;
    color: var(--muted);
  }
  .section-group { margin-bottom: 2.5rem; }
  .section-group h2 {
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: .08em;
    margin-bottom: 1rem;
    padding-bottom: .4rem;
    border-bottom: 1px solid var(--border);
  }
  .cards {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: .75rem;
  }
  .card {
    display: block;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: .9rem 1.1rem;
    color: var(--text);
    transition: border-color .2s, background .2s, transform .15s;
  }
  .card:hover {
    border-color: var(--accent);
    background: var(--surface2);
    transform: translateY(-2px);
    text-decoration: none;
  }
  .card .num { font-size: .75rem; color: var(--muted); }
  .card .title { font-weight: 600; margin-top: .15rem; }

  @media (max-width: 600px) {
    .hero h1 { font-size: 1.8rem; }
    .nav-btn { max-width: 100%; }
    .page-nav { flex-direction: column; }
  }

  /* ── XP Calculator ── */
  .xp-calc-box {
    max-width: var(--max-w);
    margin: 1.5rem auto 0;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.4rem 1.6rem;
  }
  .xp-calc-box h2 {
    font-size: 1.2rem;
    font-weight: 700;
    margin-bottom: 1rem;
    color: var(--text);
  }
  .xp-calc-row {
    display: flex;
    gap: .75rem;
    align-items: center;
    flex-wrap: wrap;
    margin-bottom: 1rem;
  }
  .xp-calc-row label { color: var(--muted); font-size: .9rem; white-space: nowrap; }
  .xp-calc-row input[type="number"] {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    color: var(--text);
    font-size: 1rem;
    padding: .4rem .75rem;
    width: 140px;
    outline: none;
  }
  .xp-calc-row input[type="number"]:focus { border-color: var(--accent); }
  .xp-calc-btn {
    background: var(--accent);
    color: #fff;
    border: none;
    border-radius: var(--radius);
    padding: .45rem 1.1rem;
    font-size: .95rem;
    font-weight: 600;
    cursor: pointer;
    transition: opacity .15s;
  }
  .xp-calc-btn:hover { opacity: .85; }
  .xp-calc-result {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1rem 1.2rem;
    font-size: .92rem;
    line-height: 1.8;
    display: none;
  }
  .xp-calc-result.visible { display: block; }
  .xp-progress-bar {
    height: 10px;
    background: var(--border);
    border-radius: 5px;
    overflow: hidden;
    margin: .5rem 0 .25rem;
  }
  .xp-progress-fill {
    height: 100%;
    background: var(--accent2);
    border-radius: 5px;
    transition: width .3s ease;
  }
  .xp-steps {
    margin-top: .75rem;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: calc(var(--radius) - 2px);
    padding: .75rem 1rem;
    font-family: 'Fira Code', 'Consolas', monospace;
    font-size: .8rem;
    color: var(--muted);
    white-space: pre-wrap;
    line-height: 1.6;
  }
"""


def md_to_html(md_text):
    """Convert Markdown text to an HTML fragment, rewriting .md links to .html."""
    import re

    # Rewrite Markdown links: [text](something.md) → [text](something.html)
    # Also handle relative-path links like ../README.md → skip (README has no HTML)
    def rewrite_link(m):
        text, target = m.group(1), m.group(2)
        if target.endswith(".md") and not target.endswith("README.md"):
            target = target[:-3] + ".html"
        return f"[{text}]({target})"

    md_text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', rewrite_link, md_text)

    return markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "codehilite", "nl2br"],
        extension_configs={"codehilite": {"css_class": "highlight", "noclasses": True}},
    )


def rel(from_html_path, to_html_path):
    """Return a relative URL from one HTML file to another (both relative to ROOT)."""
    return os.path.relpath(to_html_path, os.path.dirname(from_html_path))


def build_page(md_rel, title, group, prev_entry, next_entry, index_rel_path):
    """Build and write a single section HTML page."""
    md_abs = os.path.join(ROOT, md_rel)
    html_rel = md_rel[:-3] + ".html"        # docs/farm/06-farm-overview.html
    html_abs = os.path.join(ROOT, html_rel)

    with open(md_abs, encoding="utf-8") as f:
        raw = f.read()

    # Strip the existing navigation footer lines that reference .md files
    raw = "\n".join(
        line for line in raw.splitlines()
        if not (line.startswith("←") or line.startswith("← "))
    )

    body_html = md_to_html(raw)

    # Prev / Next buttons
    nav_html = '<div class="page-nav">'
    if prev_entry:
        prev_html_rel = prev_entry[0][:-3] + ".html"
        prev_url = rel(html_rel, prev_html_rel)
        nav_html += (
            f'<a class="nav-btn prev" href="{prev_url}">'
            f'<span>◀</span>'
            f'<span><span class="nav-label">Previous</span>{prev_entry[1]}</span>'
            f'</a>'
        )
    nav_html += (
        f'<a class="nav-btn" href="{rel(html_rel, index_rel_path)}">'
        f'🏠 Index'
        f'</a>'
    )
    if next_entry:
        next_html_rel = next_entry[0][:-3] + ".html"
        next_url = rel(html_rel, next_html_rel)
        nav_html += (
            f'<a class="nav-btn next" href="{next_url}">'
            f'<span><span class="nav-label">Next</span>{next_entry[1]}</span>'
            f'<span>▶</span>'
            f'</a>'
        )
    nav_html += '</div>'

    index_url = rel(html_rel, index_rel_path)
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Marketland+ GDD</title>
  <style>{CSS}</style>
</head>
<body>
  <nav class="topbar">
    <a class="home-link" href="{index_url}">🏪🌾 Marketland+</a>
    <span class="spacer"></span>
    <span class="group-badge">{group}</span>
  </nav>
  <main class="page-wrap">
    <article class="md-body">
      {body_html}
    </article>
    {nav_html}
  </main>
</body>
</html>"""

    with open(html_abs, "w", encoding="utf-8") as f:
        f.write(page)

    print(f"  ✓  {html_rel}")


def build_index():
    """Build and write index.html."""
    index_abs = os.path.join(ROOT, "index.html")

    # Group pages
    groups: dict[str, list] = {}
    for entry in PAGES:
        g = entry[2]
        groups.setdefault(g, []).append(entry)

    groups_html = ""
    for group_label, entries in groups.items():
        cards = ""
        for md_rel, title, _ in entries:
            html_rel = md_rel[:-3] + ".html"
            num, rest = title.split(" — ", 1)
            cards += (
                f'<a class="card" href="{html_rel}">'
                f'<div class="num">{num}</div>'
                f'<div class="title">{rest}</div>'
                f'</a>\n'
            )
        groups_html += (
            f'<section class="section-group">'
            f'<h2>{group_label}</h2>'
            f'<div class="cards">{cards}</div>'
            f'</section>\n'
        )

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Marketland+ — Game Design Document</title>
  <style>{CSS}</style>
</head>
<body>
  <header class="hero">
    <h1>🏪🌾 Marketland+</h1>
    <p class="sub">Farm &amp; Supermarket Empire — Complete Game Design Document v3.0</p>
    <div class="badges">
      <span class="badge">🎮 Unity · 3D</span>
      <span class="badge">📱 Mobile-first</span>
      <span class="badge">⚡ No Energy System</span>
      <span class="badge">💎 No Paywall</span>
      <span class="badge">📄 37 Sections</span>
    </div>
  </header>

  <div class="xp-calc-box">
    <h2>🧮 XP Calculator</h2>
    <div class="xp-calc-row">
      <label for="xp-input">Enter your total XP:</label>
      <input type="number" id="xp-input" min="0" placeholder="e.g. 100">
      <button class="xp-calc-btn" onclick="calcXP()">Calculate</button>
    </div>
    <div class="xp-calc-result" id="xp-result"></div>
  </div>

  <script>
  function xpToReachLevel(n) {{
    if (n <= 1) return 0;
    return Math.floor(50 * n * n + 150 * n - 200);
  }}
  function getCurrentLevel(totalXP) {{
    if (totalXP <= 0) return 1;
    return Math.floor((Math.sqrt(200 * totalXP + 62500) - 150) / 100);
  }}
  function calcXP() {{
    var totalXP = parseInt(document.getElementById('xp-input').value, 10);
    var resultEl = document.getElementById('xp-result');
    if (isNaN(totalXP) || totalXP < 0) {{
      resultEl.innerHTML = '<span style="color:var(--accent)">⚠️ Please enter a valid non-negative XP value.</span>';
      resultEl.classList.add('visible');
      return;
    }}
    var level = getCurrentLevel(totalXP);
    var xpCurrentLevel = xpToReachLevel(level);
    var xpNextLevel = xpToReachLevel(level + 1);
    var xpNeeded = xpNextLevel - totalXP;
    var xpInLevel = totalXP - xpCurrentLevel;
    var xpRange = xpNextLevel - xpCurrentLevel;
    var pct = Math.min(100, (xpInLevel / xpRange) * 100);
    var pctStr = pct.toFixed(1);
    var BAR_SEGMENTS = 16;
    var filled = Math.round(pct / (100 / BAR_SEGMENTS));
    var empty = BAR_SEGMENTS - filled;
    var bar = '▓'.repeat(filled) + '░'.repeat(empty);
    var sqrtVal = Math.sqrt(200 * totalXP + 62500).toFixed(2);
    var ratio = ((parseFloat(sqrtVal) - 150) / 100).toFixed(4);
    var nextLvl = level + 1;
    var steps = [
      'Step 1 — Find current level:',
      '  level = floor( (sqrt(200 × ' + totalXP + ' + 62500) − 150) / 100 )',
      '        = floor( (sqrt(' + (200 * totalXP) + ' + 62500) − 150) / 100 )',
      '        = floor( (' + sqrtVal + ' − 150) / 100 )',
      '        = floor( ' + ratio + ' )',
      '        = ' + level,
      '',
      'Step 2 — XP to reach Level ' + nextLvl + ':',
      '  XP_to_reach(' + nextLvl + ') = floor(50 × ' + nextLvl + '² + 150 × ' + nextLvl + ' − 200)',
      '                   = ' + xpNextLevel + ' XP',
      '',
      'Step 3 — XP accumulated in current level:',
      '  XP_in_level = ' + totalXP + ' − ' + xpCurrentLevel + ' = ' + xpInLevel + ' XP',
      '',
      'Step 4 — XP still needed:',
      '  XP_needed = ' + xpNextLevel + ' − ' + totalXP + ' = ' + xpNeeded + ' XP'
    ].join('\\n');
    resultEl.innerHTML =
      '<div>📊 <strong>Current Level: ' + level + '</strong></div>' +
      '<div>📈 XP to Next Level (Level ' + nextLvl + '): <strong>' + xpNeeded + ' more XP needed</strong> (you have ' + xpInLevel + ' / ' + xpRange + ')</div>' +
      '<div class="xp-progress-bar"><div class="xp-progress-fill" style="width:' + pct + '%"></div></div>' +
      '<div style="color:var(--muted);font-size:.85rem">' + bar + '  ' + pctStr + '%</div>' +
      '<div class="xp-steps">' + steps + '</div>';
    resultEl.classList.add('visible');
  }}
  document.addEventListener('DOMContentLoaded', function() {{
    document.getElementById('xp-input').addEventListener('keydown', function(e) {{
      if (e.key === 'Enter') calcXP();
    }});
  }});
  </script>

  <main style="max-width:var(--max-w);margin:0 auto;padding:0 1rem;margin-top:1.5rem;">
    {groups_html}
  </main>
</body>
</html>"""

    with open(index_abs, "w", encoding="utf-8") as f:
        f.write(page)

    print("  ✓  index.html")


def main():
    print("Generating HTML pages…")
    index_rel = "index.html"

    for i, entry in enumerate(PAGES):
        md_rel, title, group = entry
        prev_entry = PAGES[i - 1] if i > 0 else None
        next_entry = PAGES[i + 1] if i < len(PAGES) - 1 else None
        build_page(md_rel, title, group, prev_entry, next_entry, index_rel)

    build_index()
    print(f"\nDone — {len(PAGES)} section pages + index.html")


if __name__ == "__main__":
    main()
