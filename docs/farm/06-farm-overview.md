# 🌾 06 — Farm Overview

The farm in Marketland+ is a fully-featured production facility, not a decorative side feature. It is your primary source of premium goods, your most strategic long-term investment, and the heart of what makes Marketland+ unique among supermarket games.

---

## 🗺️ Farm Structure

The farm is divided into **zones** that are unlocked progressively as the player levels up. Each zone adds new land area that can be used for crop plots, animal pens, processing buildings, or worker paths.

| Zone | Unlock Level | Size | Purpose |
|------|-------------|------|---------|
| Zone 0 (Starter) | Lv.1 | 8×8 tiles | First crops, Barn |
| Zone 1 | Lv.5 | +6×8 tiles | More crops |
| Zone 2 | Lv.10 | +8×8 tiles | Chicken/Cow pens |
| Zone 3 | Lv.15 | +8×10 tiles | Sheep/more crops |
| Zone 4 | Lv.22 | +10×10 tiles | Goat, Duck, more processing |
| Zone 5 | Lv.30 | +12×10 tiles | Large farms, first premium crops |
| Zone 6 | Lv.45 | +12×12 tiles | Textile Mill, Cotton |
| Zone 7 | Lv.65 | +14×12 tiles | Rabbit, Perfume Atelier |
| Zone 8 (Greenhouse) | Lv.40 | Separate area | Year-round exotic crops |
| Zone 9 (Apiary) | Lv.60 | +8×6 tiles | Beehives, special flowers |
| Zone 10 (Deer Range) | Lv.80 | +16×14 tiles | Deer, Gourmet Kitchen |

---

## 🏗️ Farm Building Categories

### 1. Storage
- **Barn** (Lv.1) — Primary storage for raw materials and processed goods. Upgradeable to 50/100/200/500 slots.

### 2. Processing
All 16 processing buildings (detailed in [09-processing-buildings.md](09-processing-buildings.md)) are placed here and convert raw materials to finished goods.

### 3. Animal Pens
Enclosures for all 9 animal types (detailed in [08-animal-husbandry.md](08-animal-husbandry.md)).

### 4. Worker Facilities
- **Worker Hut** — Unlocked at Lv.20; required before hiring any farm workers
- **Tool Shed** — Unlocked at Lv.30; increases worker efficiency by 20%
- **Break Room** — Unlocked at Lv.50; workers never tire, 100% uptime

### 5. Crop Plots
Variable-size plantable areas (1×1 to 4×4) for all 19 crop types.

---

## 🌿 Farm Economy Flow

```
Seeds + Water
     ↓
 Crop Plots → Harvest → Raw Goods → Barn Storage
                                        ↓
Animal Pens → Products → ─────────────→ Processing Buildings
                                        ↓
                              Processed Goods → Supply Lane → Store Stockroom
```

---

## 📐 Farm Grid System

The farm uses a **tile-based grid**:
- Each tile is 1×1 unit
- Crop plots: 1×1 (single) or multi-tile (2×2, 3×3, 4×4 for higher yields)
- Animal pens: fixed sizes (see Animal Husbandry doc)
- Buildings: 2×2 to 4×4 depending on type
- Workers walk on defined paths between buildings

> 💡 **Design Note:** Players are free to arrange their farm however they like within each zone's tile grid. A well-optimised layout (buildings close to barns, short worker paths) produces more goods per hour.

---

## 🏆 Farm Rating

Each farm zone has a **Star Rating** (0–5 stars) based on:
- % of plots actively planted
- % of animal pens occupied
- % of processing buildings active
- Worker coverage
- Fertiliser usage

Higher star ratings grant a passive **Farm Bonus** multiplier on all Farm Token yields for that zone.

---

← [Previous — Unified Game World](../05-unified-game-world.md) | [Back to README](../../README.md) | [Next → Crop System](07-crop-system.md)
