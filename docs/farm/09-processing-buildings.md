# 🏭 09 — Processing Buildings

Processing buildings transform raw farm materials into finished goods that the store can sell for premium prices. With 16 buildings ranging from the basic Bakery Oven to the elite Gourmet Kitchen, the processing layer adds manufacturing depth to the farm.

---

## 🏗️ Complete Processing Building Table

| Building | Unlock | Input → Output | Process Time | Queue Slots |
|----------|--------|----------------|--------------|-------------|
| 🏚️ Barn | Lv.1 | Storage only | — | 50 slots |
| 🌿 Compost Shed | Lv.8 | Animal Waste → Fertiliser | 30 min | 2 |
| 🍞 Bakery Oven | Lv.5 | Wheat+Eggs+Milk → Bread/Muffins/Croissants | 10–20 min | 2 |
| 🧀 Dairy Factory | Lv.12 | Milk → Cheese/Yoghurt/Butter | 20–40 min | 2 |
| 🍓 Jam Kitchen | Lv.14 | Strawberry+Sugar → Jam/Jelly | 15–30 min | 2 |
| 🥤 Juice Press | Lv.16 | Tomato/Grapes/Corn → Juice/Smoothie | 15 min | 3 |
| ☕ Roastery | Lv.18 | Coffee Beans → Roasted Coffee | 25 min | 2 |
| 🍺 Brewery | Lv.32 | Hops+Sugarcane+Yeast → Craft Beer | 2 hr | 2 |
| 🍷 Winery | Lv.35 | Grapes+Sugar → Wine | 4 hr | 2 |
| 🧴 Cosmetics Lab | Lv.40 | Lavender+Goat Milk+Beeswax → Skincare | 1 hr | 3 |
| 🧵 Textile Mill | Lv.45 | Wool/Cotton → Fabric → Clothing | 1.5 hr | 2 |
| 🍫 Chocolate Factory | Lv.50 | Sugarcane+Vanilla+Milk → Artisan Chocolates | 45 min | 3 |
| 🍯 Honey Studio | Lv.62 | Honey+Beeswax → Luxury Honey/Candles | 30 min | 3 |
| 🥃 Distillery | Lv.65 | Grapes/Grain → Whiskey/Vodka | 6 hr | 2 |
| 🌸 Perfume Atelier | Lv.70 | Lavender+Orchid+Vanilla → Luxury Perfume | 3 hr | 2 |
| 🍽️ Gourmet Kitchen | Lv.80 | Truffle+Saffron+Wagyu → Luxury Meals | 2 hr | 2 |

---

## 🔧 Building Upgrade System

Each processing building can be upgraded through **3 tiers** (beyond the base level):

| Upgrade Tier | Queue Bonus | Speed Bonus | Cost |
|-------------|-------------|-------------|------|
| Tier 1 (Base) | Default | Base speed | Free (built-in) |
| Tier 2 | +1 queue slot | −10% time | 1,000–5,000 FT |
| Tier 3 | +2 queue slots | −25% time | 5,000–20,000 FT |
| Tier 4 (Master) | +3 queue slots | −40% time | 20,000–100,000 FT |

---

## ⚙️ Processing Job System

### Manual Operation:
1. Player opens building UI
2. Selects recipe
3. Assigns raw materials from Barn
4. Job queues and starts immediately
5. Player returns to collect finished goods

### Automatic Operation (with Kitchen Hand worker):
- Worker scans barn inventory and queues all available recipes automatically
- Prioritises recipes for displays that are low on stock
- Player can set recipe priority order

---

## 📦 Recipe Output Details

### Bakery Oven Recipes
| Recipe | Inputs | Output | Time | Store Value (Fresh) |
|--------|--------|--------|------|---------------------|
| Bread | 3 Wheat + 1 Egg | 2 Bread | 10 min | 45 coins |
| Muffins | 2 Wheat + 1 Egg + 1 Milk | 3 Muffins | 15 min | 60 coins |
| Croissants | 3 Wheat + 2 Milk + 1 Butter | 2 Croissants | 20 min | 85 coins |

### Dairy Factory Recipes
| Recipe | Inputs | Output | Time | Store Value (Fresh) |
|--------|--------|--------|------|---------------------|
| Cheese | 3 Milk | 1 Cheese | 20 min | 70 coins |
| Yoghurt | 2 Milk + 1 Sugar | 2 Yoghurt | 25 min | 55 coins |
| Butter | 4 Milk | 2 Butter | 15 min | 40 coins |

### Brewery Recipes
| Recipe | Inputs | Output | Time | Store Value (Fresh) |
|--------|--------|--------|------|---------------------|
| Craft Lager | 3 Hops + 2 Sugarcane + Yeast | 3 Bottles | 2 hr | 180 coins |
| Craft Stout | 4 Hops + 2 Sugarcane + Yeast | 2 Bottles | 2.5 hr | 220 coins |

---

## 🏅 Processing Mastery

Each building tracks total jobs completed and awards **Mastery Stars**:
- ⭐ 1 Star: 50 jobs → +5% yield
- ⭐⭐ 2 Stars: 200 jobs → +10% yield, +1 queue slot bonus
- ⭐⭐⭐ 3 Stars: 500 jobs → +20% yield, −15% time, unlock exclusive recipe

---

← [Previous — Animal Husbandry](08-animal-husbandry.md) | [Back to README](../../README.md) | [Next → Crafting Chains](10-crafting-chains.md)
