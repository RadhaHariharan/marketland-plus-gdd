# 🏪 15 — Store Grid & Layout

The store in Marketland+ is a tile-based grid that players build, decorate, and optimise. Every placement decision affects customer flow, LP score, and overall revenue.

---

## 📐 Grid System

The store uses a **tile-based grid** system:
- Base size: **10×10 tiles** at Lv.1
- Each zone expansion adds more tiles
- Tile types: Floor, Display, Coin-Op, Attraction, Decoration, Wall, Entrance, Counter
- Items snap to the grid (1×1, 2×1, 2×2, 3×2, 4×2 footprints)

---

## 🏗️ Store Zones

| Zone | Unlock Level | Size Added | Cost | Key Unlocks |
|------|-------------|-----------|------|-------------|
| Zone 1 (Starter) | Lv.1 | 10×10 | Free | Basic displays |
| Zone 2 | Lv.8 | +8×10 | 2,000 coins | More shelving space |
| Zone 3 | Lv.15 | +10×10 | 5,000 coins | Full aisle layout |
| Zone 4 | Lv.25 | +12×10 | 12,000 coins | Beauty & Clothing section |
| Zone 5 | Lv.35 | +12×12 | 25,000 coins | Electronics section |
| Zone 6 | Lv.50 | +14×12 | 50,000 coins | Luxury section |
| Zone 7 | Lv.65 | +14×14 | 80,000 coins | VIP area |
| Zone 8 | Lv.80 | +16×14 | 150,000 coins | Premium wing |

---

## 🏠 Floor Types & Effects

| Floor Type | LP Bonus | Unlock | Cost |
|-----------|---------|--------|------|
| Bare Concrete | 0 LP | Lv.1 | Free |
| Tile Floor | +5 LP | Lv.1 | 100 coins/tile |
| Polished Wood | +15 LP | Lv.10 | 300 coins/tile |
| Marble | +30 LP | Lv.25 | 800 coins/tile |
| Inlaid Mosaic | +50 LP | Lv.40 | 2,000 coins/tile |
| Gold Inlay | +100 LP | Lv.70 | 5,000 coins/tile |
| Crystal Floor | +200 LP | Lv.100 | 15,000 coins/tile |

---

## 🧱 Wall Types & Effects

| Wall Type | LP Bonus | Unlock | Cost |
|-----------|---------|--------|------|
| Plain White | 0 LP | Lv.1 | Free |
| Painted Wall | +3 LP/section | Lv.5 | 50 coins |
| Wallpaper | +8 LP/section | Lv.15 | 200 coins |
| Wood Panel | +15 LP/section | Lv.30 | 500 coins |
| Luxury Plaster | +25 LP/section | Lv.50 | 1,200 coins |
| Mirrored Wall | +50 LP/section | Lv.70 | 3,000 coins |

---

## 🚶 Customer Flow

Customer pathfinding is influenced by store layout:
- Customers enter from the **entrance** (bottom of grid)
- They walk to displays they can afford
- Wider aisles = more customers can pass simultaneously
- **Dead ends** reduce customer flow (design recommendation: open layouts)
- Attractions and coin-op items act as **flow anchors** drawing customers deeper into the store

### Aisle Width Effects:
| Aisle Width | Max Customers | Flow Modifier |
|-------------|--------------|---------------|
| 1 tile | 1 customer | −20% throughput |
| 2 tiles | 2 customers | Base |
| 3 tiles | 4 customers | +15% throughput |
| 4+ tiles | Unlimited | +30% throughput |

---

## 🎨 Store Theming

Players can apply **store themes** that change the visual style of all floors/walls simultaneously:
- 🌿 **Farm Market Theme** — earthy tones, wooden shelves; +10% Fresh badge value
- 🏙️ **Modern City Theme** — sleek minimalism; +5% all purchases
- 🍰 **Cozy Bakery Theme** — warm pastels; +15% bakery section sales
- 💎 **Luxury Boutique Theme** — dark colours, gold trim; +20% luxury customer budget
- 🎄 **Holiday Theme** (seasonal) — festive decor; available during Winter season

---

## 📏 Display Placement Rules

- **Distance rule:** Displays of the same category get +5% LP if placed in the same section
- **Corner bonus:** Corner displays get +10% customer visit frequency
- **Front-of-store bonus:** Displays in the first 3 tile rows get +15% visibility
- **Attraction adjacency:** Any display within 2 tiles of an attraction gets +10% customer visits

---

← [Previous — Farm Expansion](../farm/14-farm-expansion.md) | [Back to README](../../README.md) | [Next → Supply Modes](16-supply-modes.md)
