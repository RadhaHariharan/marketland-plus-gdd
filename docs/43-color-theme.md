# 43 — Color Theme & Visual Identity

> **SuperStoreTycoon** — "One Empire, Two Worlds"
> Premium dark mobile game palette derived directly from the game icon and world design.

---

## Design Philosophy

The color system is built around three core feelings:

| Feeling | How it's achieved |
|---------|------------------|
| **Premium** | Deep navy-black backgrounds; nothing feels washed-out or cheap |
| **Fresh** | High-saturation Farm Emerald and Tycoon Gold as energy colors |
| **Trustworthy** | Consistent use of Store Sapphire for interactive / navigational elements |

The two game worlds have their own tones but share a unified dark foundation so the UI never feels jarring when switching between farm and store.

---

## 1. Brand Foundation

These are the four anchor colors everything else is derived from.

| Token | Hex | Preview | Usage |
|-------|-----|---------|-------|
| `--brand-gold` | `#F7C832` | 🟡 | Crown, rewards, CTAs, prestige |
| `--brand-emerald` | `#22C55E` | 🟢 | Farm world, growth, XP bar, success |
| `--brand-sapphire` | `#4F8EF7` | 🔵 | Store world, links, info, interactive |
| `--brand-ruby` | `#EF4444` | 🔴 | Danger, barn red, urgent alerts |

---

## 2. Background & Surface Scale

Dark from deepest to highest elevation. Each step is roughly +8 lightness in HSL.

| Token | Hex | Usage |
|-------|-----|-------|
| `--bg-void` | `#04061A` | App root background |
| `--bg-deep` | `#080D28` | Behind panels, behind modals |
| `--bg-base` | `#0D1235` | Main page / screen surface |
| `--bg-raised` | `#141B42` | Cards, tab bars, list items |
| `--bg-elevated` | `#1C2550` | Hover state, highlighted cards |
| `--bg-overlay` | `#283580` | Tooltip background, sheet overlay |

---

## 3. Border Scale

| Token | Hex | Usage |
|-------|-----|-------|
| `--border-subtle` | `#1E2860` | Dividers inside cards |
| `--border-default` | `#283585` | Default card borders |
| `--border-strong` | `#3B4EA0` | Active/focused borders |
| `--border-gold` | `#F7C832` | Premium / selected item ring |

---

## 4. Text Scale

| Token | Hex | Usage |
|-------|-----|-------|
| `--text-primary` | `#F1F5F9` | Headings, primary labels |
| `--text-secondary` | `#94A3B8` | Sub-labels, descriptions |
| `--text-muted` | `#64748B` | Timestamps, metadata |
| `--text-disabled` | `#334155` | Disabled states |
| `--text-on-gold` | `#1A0E00` | Text placed on gold backgrounds |
| `--text-on-green` | `#0A1F0D` | Text placed on emerald backgrounds |

---

## 5. Farm World Palette

Used in the farm half of the UI, crop cards, weather overlays, and field HUD.

| Token | Hex | Usage |
|-------|-----|-------|
| `--farm-bg-top` | `#1E7010` | Farm sky/background gradient start |
| `--farm-bg-bottom` | `#071506` | Farm background gradient end |
| `--farm-emerald` | `#22C55E` | Crop health, growth bars |
| `--farm-emerald-dark` | `#15803D` | Pressed state, deep grass |
| `--farm-grass` | `#28A84E` | Ground / grass texture tint |
| `--farm-soil` | `#6E4E14` | Soil / tilled land |
| `--farm-wheat` | `#EEC038` | Wheat, harvest highlight |
| `--farm-wheat-dark` | `#C08A18` | Wheat shadow, dried stalk |
| `--farm-sun` | `#FFD020` | Sun glow, daylight warmth |
| `--farm-barn-red` | `#F04030` | Barn walls, farm buildings |
| `--farm-barn-dark` | `#801808` | Barn shadow, roof trim |
| `--farm-window` | `#FFD878` | Lit barn windows, warm light |

---

## 6. Store World Palette

Used in the store half of the UI, shelving cards, customer HUD, and inventory.

| Token | Hex | Usage |
|-------|-----|-------|
| `--store-bg-top` | `#0D2490` | Store sky/background gradient start |
| `--store-bg-bottom` | `#03071E` | Store background gradient end |
| `--store-sapphire` | `#4F8EF7` | Interactive elements, links |
| `--store-sapphire-dark` | `#1D4ED8` | Pressed state, deep navy |
| `--store-awning` | `#5AA8FF` | Awning, store accents |
| `--store-wall` | `#F8F4EA` | Building wall, cream |
| `--store-wall-dark` | `#D0C8B0` | Wall shadow, aged cream |
| `--store-sign-bg` | `#060E28` | Neon sign background |
| `--store-sign-ring` | `#3060E0` | Neon sign border glow |
| `--store-pavement` | `#1A2272` | Pavement, step, floor |
| `--store-door` | `#03091A` | Door / entrance darkness |
| `--store-handle` | `#4080F8` | Door handles, fixtures |

---

## 7. Supply Lane

The gold vertical divider connecting farm → store is a core visual motif.

| Token | Hex | Usage |
|-------|-----|-------|
| `--lane-gold-top` | `#FFFACC` | Supply lane gradient top |
| `--lane-gold-mid` | `#F7C832` | Supply lane gradient middle |
| `--lane-gold-dark` | `#DA8400` | Supply lane gradient bottom |
| `--lane-gold-deep` | `#8C4A00` | Supply lane deepest shadow |
| `--lane-arrow` | `#0C1A40` | Directional arrow on lane |

---

## 8. Semantic Colors

| Token | Hex | Dark muted bg | Usage |
|-------|-----|---------------|-------|
| `--success` | `#22C55E` | `#14532D` | Harvest complete, sale success |
| `--success-light` | `#86EFAC` | — | Success text on dark bg |
| `--warning` | `#F7C832` | `#713F12` | Crop needs water, low stock |
| `--warning-light` | `#FDE68A` | — | Warning text |
| `--error` | `#EF4444` | `#7F1D1D` | Spoiled crop, payment failure |
| `--error-light` | `#FCA5A5` | — | Error text |
| `--info` | `#4F8EF7` | `#1E3A8A` | Tips, tutorials, notifications |
| `--info-light` | `#BAD1FD` | — | Info text on dark bg |

---

## 9. Currency & Reward Colors

Each currency has a distinct signature color so players immediately know what they earned.

| Currency | Token | Hex | Icon tint |
|----------|-------|-----|-----------|
| **Coins** (main) | `--coin-gold` | `#F7C832` | 🪙 Gold coin |
| **Farm Coins** | `--coin-farm` | `#22C55E` | 🌿 Green coin (Fresh badge) |
| **Luxury Points** | `--luxury` | `#A855F7` | 💎 Purple gem |
| **Gems** (premium) | `--gem` | `#E879F9` | ✨ Magenta gem |
| **XP** | `--xp` | `#4F8EF7` | ⭐ Blue star |
| **Mastery Stars** | `--mastery` | `#F59E0B` | ⭐ Amber star |

---

## 10. Rarity Tiers

Used for item cards, collection slots, supplier quality, and crop seeds.

| Tier | Token | Hex | Glow | Description |
|------|-------|-----|------|-------------|
| Common | `--rarity-common` | `#94A3B8` | none | Basic seeds, starter items |
| Uncommon | `--rarity-uncommon` | `#22C55E` | soft green | Better yield crops |
| Rare | `--rarity-rare` | `#4F8EF7` | soft blue | Imported goods |
| Epic | `--rarity-epic` | `#A855F7` | purple glow | Limited season crops |
| Legendary | `--rarity-legendary` | `#F7C832` | gold glow | Heirloom seeds, crown items |
| Mythic | `--rarity-mythic` | `#EF4444` | red pulse | Festival exclusives |

---

## 11. UI Component Tokens

### Buttons

| State | Background | Text | Border |
|-------|-----------|------|--------|
| Primary (CTA) | `#F7C832` | `#1A0E00` | none |
| Primary hover | `#FDE68A` | `#1A0E00` | none |
| Secondary | `#141B42` | `#F1F5F9` | `#283585` |
| Secondary hover | `#1C2550` | `#F1F5F9` | `#3B4EA0` |
| Danger | `#7F1D1D` | `#FCA5A5` | `#EF4444` |
| Disabled | `#1C2550` | `#334155` | `#1E2860` |

### Cards

| Property | Value |
|----------|-------|
| Background | `#141B42` |
| Border | `#283585` |
| Border radius | `12px` |
| Hover border | `#F7C832` |
| Shadow | `0 4px 24px rgba(0,0,0,0.5)` |
| Selected ring | `2px solid #F7C832` |

### Progress Bars

| Context | Fill | Track |
|---------|------|-------|
| XP | `#4F8EF7` | `#1E2860` |
| Crop growth | `#22C55E` | `#1E2860` |
| Harvest timer | `#F7C832` | `#1E2860` |
| Health / spoil | `#EF4444` | `#1E2860` |
| Mastery | `#F59E0B` | `#1E2860` |

---

## 12. Typography

### Font Stack

```
Primary UI:   'Segoe UI', system-ui, -apple-system, sans-serif
Display/Logo: 'Arial Black', Impact, Arial, sans-serif
Monospace:    'Fira Code', 'Consolas', monospace
```

### Type Scale

| Role | Size | Weight | Color token |
|------|------|--------|-------------|
| Hero title | `2.6rem` | 900 | `--text-primary` |
| Section heading | `1.4rem` | 700 | `--text-primary` |
| Card title | `1rem` | 600 | `--text-primary` |
| Body | `1rem` | 400 | `--text-primary` |
| Label | `0.875rem` | 500 | `--text-secondary` |
| Caption / meta | `0.78rem` | 400 | `--text-muted` |
| Monospace | `0.85em` | 400 | `--text-secondary` |

### Letter Spacing

| Context | Value |
|---------|-------|
| All-caps section labels | `0.08em` |
| "TYCOON" display text | `6px` |
| Button labels | `0.04em` |
| Body text | `0` (default) |

---

## 13. Gradients & Overlays

| Name | Definition | Usage |
|------|-----------|-------|
| Gold shimmer | `linear-gradient(180deg, #FFFACC 0%, #F7C832 35%, #DA8400 65%, #8C4A00 100%)` | Border ring, crown, divider |
| Farm sky | `linear-gradient(180deg, #1E7010 0%, #071506 100%)` | Farm background |
| Store sky | `linear-gradient(180deg, #0D2490 0%, #03071E 100%)` | Store background |
| Dark overlay | `linear-gradient(180deg, transparent 60%, #020510 100%)` | Text legibility at bottom of panels |
| Coin burst | `radial-gradient(circle, #FDE68A 0%, #F7C832 50%, transparent 100%)` | Coin collect effect |
| XP burst | `radial-gradient(circle, #BAD1FD 0%, #4F8EF7 50%, transparent 100%)` | XP collect effect |

---

## 14. Shadows & Depth

| Level | Box shadow | Used on |
|-------|-----------|---------|
| 1 — Subtle | `0 2px 8px rgba(0,0,0,0.3)` | List items |
| 2 — Card | `0 4px 24px rgba(0,0,0,0.5)` | Cards, panels |
| 3 — Float | `0 8px 40px rgba(0,0,0,0.65)` | Modals, dropdowns |
| 4 — Glow Gold | `0 0 20px rgba(247,200,50,0.4)` | Selected legendary items |
| 5 — Glow Emerald | `0 0 16px rgba(34,197,94,0.35)` | Crop-ready badge |
| 6 — Glow Ruby | `0 0 16px rgba(239,68,68,0.4)` | Urgent alerts |

---

## 15. CSS Custom Properties — Full Reference

Paste this `:root` block into any stylesheet or Unity TextMeshPro theme to apply the full system.

```css
:root {
  /* ── Brand ── */
  --brand-gold:       #F7C832;
  --brand-emerald:    #22C55E;
  --brand-sapphire:   #4F8EF7;
  --brand-ruby:       #EF4444;

  /* ── Backgrounds ── */
  --bg-void:          #04061A;
  --bg-deep:          #080D28;
  --bg-base:          #0D1235;
  --bg-raised:        #141B42;
  --bg-elevated:      #1C2550;
  --bg-overlay:       #283580;

  /* ── Borders ── */
  --border-subtle:    #1E2860;
  --border-default:   #283585;
  --border-strong:    #3B4EA0;
  --border-gold:      #F7C832;

  /* ── Text ── */
  --text-primary:     #F1F5F9;
  --text-secondary:   #94A3B8;
  --text-muted:       #64748B;
  --text-disabled:    #334155;
  --text-on-gold:     #1A0E00;
  --text-on-green:    #0A1F0D;

  /* ── Farm World ── */
  --farm-bg-top:      #1E7010;
  --farm-bg-bottom:   #071506;
  --farm-emerald:     #22C55E;
  --farm-emerald-dark:#15803D;
  --farm-grass:       #28A84E;
  --farm-soil:        #6E4E14;
  --farm-wheat:       #EEC038;
  --farm-wheat-dark:  #C08A18;
  --farm-sun:         #FFD020;
  --farm-barn-red:    #F04030;
  --farm-barn-dark:   #801808;
  --farm-window:      #FFD878;

  /* ── Store World ── */
  --store-bg-top:     #0D2490;
  --store-bg-bottom:  #03071E;
  --store-sapphire:   #4F8EF7;
  --store-sapphire-dark: #1D4ED8;
  --store-awning:     #5AA8FF;
  --store-wall:       #F8F4EA;
  --store-wall-dark:  #D0C8B0;
  --store-sign-bg:    #060E28;
  --store-sign-ring:  #3060E0;
  --store-pavement:   #1A2272;
  --store-door:       #03091A;
  --store-handle:     #4080F8;

  /* ── Supply Lane ── */
  --lane-gold-top:    #FFFACC;
  --lane-gold-mid:    #F7C832;
  --lane-gold-dark:   #DA8400;
  --lane-gold-deep:   #8C4A00;
  --lane-arrow:       #0C1A40;

  /* ── Semantic ── */
  --success:          #22C55E;
  --success-muted:    #14532D;
  --success-light:    #86EFAC;
  --warning:          #F7C832;
  --warning-muted:    #713F12;
  --warning-light:    #FDE68A;
  --error:            #EF4444;
  --error-muted:      #7F1D1D;
  --error-light:      #FCA5A5;
  --info:             #4F8EF7;
  --info-muted:       #1E3A8A;
  --info-light:       #BAD1FD;

  /* ── Currency ── */
  --coin-gold:        #F7C832;
  --coin-farm:        #22C55E;
  --luxury:           #A855F7;
  --gem:              #E879F9;
  --xp:               #4F8EF7;
  --mastery:          #F59E0B;

  /* ── Rarity ── */
  --rarity-common:    #94A3B8;
  --rarity-uncommon:  #22C55E;
  --rarity-rare:      #4F8EF7;
  --rarity-epic:      #A855F7;
  --rarity-legendary: #F7C832;
  --rarity-mythic:    #EF4444;

  /* ── Radius ── */
  --radius-sm:        6px;
  --radius-md:        12px;
  --radius-lg:        20px;
  --radius-pill:      999px;
}
```

---

## 16. Unity TextMeshPro Mapping

| TMP Role | Color Hex |
|----------|-----------|
| Normal text | `#F1F5F9` |
| Highlighted text | `#F7C832` |
| Link color | `#4F8EF7` |
| Selected color | `#1C2550` |
| Disabled color | `#334155` |
| Panel background | `#141B42` |

---

*Last updated: April 2026 — aligned with icon.svg v1.0 color anchors.*
