# 🌱 07 — Crop System

Crops are the foundation of the farm. With 19 crop types spanning from a 5-minute wheat harvest to a 12-hour truffle cultivation, the crop system provides short, medium, and long-term rhythms that keep the farm engaging at every play frequency.

---

## 🌾 Complete Crop Table

| Crop | Unlock | Grow Time | Wilt Timer | Yield | Farm Tokens | Season | Makes |
|------|--------|-----------|------------|-------|-------------|--------|-------|
| 🌾 Wheat | Lv.1 | 5 min | 30 min | 8–12 | 1 | Autumn | Bread, Cereal, Flour, Hay |
| 🍅 Tomato | Lv.1 | 8 min | 45 min | 6–10 | 1 | Summer | Ketchup, Pasta Sauce, Soup |
| 🥕 Carrot | Lv.2 | 10 min | 1 hr | 6–10 | 1 | Spring | Veg Rack, Baby Food, Rabbit Feed |
| 🌽 Corn | Lv.3 | 15 min | 1.5 hr | 8–14 | 1 | Summer | Popcorn, Cereal, Pig Feed |
| 🍓 Strawberry | Lv.4 | 12 min | 1 hr | 5–9 | 2 | Spring | Jam, Smoothies, Pastries |
| 🥔 Potato | Lv.5 | 20 min | 2 hr | 10–16 | 1 | Autumn | Chips, Baby Food, Soup |
| 🥒 Cucumber | Lv.6 | 18 min | 1.5 hr | 6–10 | 1 | Summer | Salad, Pickles, Skincare |
| 🌻 Sunflower | Lv.8 | 25 min | 2 hr | 4–7 | 2 | Summer | Oil, Decoration, Bee Food |
| 🎋 Sugarcane | Lv.10 | 30 min | 3 hr | 8–14 | 2 | Summer | Sugar, Candy, Soft Drinks |
| 🧵 Cotton | Lv.12 | 45 min | 4 hr | 4–8 | 3 | Summer | Fabric, Textile Mill |
| ☕ Coffee Beans | Lv.15 | 1 hr | 6 hr | 4–7 | 3 | All year | Coffee Corner, Roastery |
| 🍇 Grapes | Lv.20 | 2 hr | 8 hr | 6–10 | 4 | Autumn | Wine, Juice, Distillery |
| 🌶️ Chilli | Lv.22 | 40 min | 4 hr | 5–9 | 2 | Summer | Hot Sauce, Spice Display |
| 💜 Lavender | Lv.25 | 1.5 hr | 8 hr | 3–6 | 4 | Spring | Perfume, Cosmetics, Bee Food |
| 🍺 Hops | Lv.28 | 2 hr | 12 hr | 5–9 | 4 | Autumn | Brewery, Craft Beer |
| 🌼 Vanilla | Lv.35 | 3 hr | 12 hr | 2–4 | 6 | Greenhouse | Bakery, Chocolate, Perfume |
| 🌸 Saffron | Lv.50 | 6 hr | 24 hr | 1–3 | 10 | Greenhouse | Luxury Meals, Royal Feast |
| 🍄 Truffle | Lv.60 | 12 hr | 24 hr | 1–2 | 15 | Greenhouse | Gourmet Deli, Royal Feast |
| 🌺 Exotic Orchid | Lv.70 | 8 hr | 24 hr | 2–4 | 12 | Greenhouse | Luxury Beauty, Perfume Atelier |

---

## 🌱 Crop Growth Stages

Each crop passes through **4 growth stages**:
1. **Planted** — Seeds in soil; tapping shows progress
2. **Sprouting** — Small plant visible; 25% grown
3. **Growing** — Full plant size; 75% grown
4. **Ready** — Harvest animation plays; golden glow indicates readiness
5. **Wilting** (if not harvested in time) — Plant degrades; reduced or zero yield

### Wilt Mechanics:
- Once a crop reaches the **Wilt Timer** after becoming ready, it begins to visually wilt
- Partial wilt (50% through wilt timer): yield reduced by 50%
- Full wilt: yield drops to 0 and plot must be cleared (costs nothing, but wastes seeds)
- **Fertiliser** extends the wilt timer by 2× for that plot

---

## 💧 Watering System

Crops require watering **once** during their growth cycle:
- Manual tap-to-water is always free
- **Rain weather** auto-waters all plots
- **Field Hand** worker auto-waters assigned plots
- Skipping water reduces yield by 25%
- Watered crops produce maximum yield

---

## 🌿 Fertiliser

Fertiliser is produced in the **Compost Shed** from animal waste:
- Applying fertiliser to a plot:
  - +30% yield on harvest
  - Wilt timer extended by 2×
  - Plot glows green while active
- Fertiliser expires after one harvest
- **Botanist** worker auto-applies fertiliser if available

---

## 🌡️ Seasonal Effects on Crops

| Season | Affected Crops | Effect |
|--------|----------------|--------|
| 🌸 Spring | Lavender, Carrot, Strawberry | +50% / +20% / +20% yield |
| ☀️ Summer | Tomato, Corn, Cucumber, Sunflower, Sugarcane, Chilli | +25% yield; wilt 25% faster |
| 🍂 Autumn | Wheat, Potato, Grapes, Hops | +10% coins on harvest |
| ❄️ Winter | All outdoor crops | 50% slower growth |
| — | Greenhouse crops (Vanilla, Saffron, Truffle, Orchid) | Unaffected by seasons |

---

## 🌾 Multi-Tile Crop Plots

Players can plant on larger plots for greater efficiency:

| Plot Size | Required Zone | Yield Bonus | Seed Cost |
|-----------|--------------|-------------|-----------|
| 1×1 | Any | Base | 1 seed |
| 2×2 | Zone 2+ | +20% | 4 seeds |
| 3×3 | Zone 4+ | +50% | 9 seeds |
| 4×4 | Zone 6+ | +100% | 16 seeds |

---

← [Previous — Farm Overview](06-farm-overview.md) | [Back to README](../../README.md) | [Next → Animal Husbandry](08-animal-husbandry.md)
