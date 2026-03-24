# 📖 37 — Complete Game Mechanics Reference

This is the master combined reference document covering **every unlockable item across Farm and Store**, including unlock level, build price, quantity/capacity, what it produces or sells, per-unit sell price, and XP earned on successful build, harvest, collection, or restock.

Use this alongside the [XP Calculator on the Index page](../index.html) to plan your progression.

---

## 📐 How to Read This Document

| Column | Meaning |
|--------|---------|
| **Unlock Level** | Player level required to access this item |
| **Build / Buy Cost** | One-time coin or Farm Token cost to place the item |
| **Quantity / Capacity** | Default units produced per cycle, or display stock capacity |
| **Produce / Sells** | What the item outputs (farm) or what it stocks (store) |
| **Sell Price (coins)** | Base coin value per unit sold to customers (store) or per output unit (farm) |
| **XP Gained** | XP awarded on a successful harvest, collection, job completion, or restock |

> 🔑 **Farm Token (FT)** is the secondary currency earned from farm activity. All FT values below refer to Farm Tokens, not coins.

---

## ⭐ XP Quick Reference

| Action | XP Range |
|--------|----------|
| Customer purchase | 1–5 XP per visit |
| Restock a display | 2 XP |
| Harvest a crop | 3–15 XP |
| Collect animal product | 2–8 XP |
| Complete processing job | 5–25 XP |
| Complete daily quest | 50–200 XP |
| Complete story quest | 100–500 XP |
| Complete a collection | 50–300 XP |
| Place decoration | 5–20 XP |
| Install attraction | 50–200 XP |
| Unlock farm zone | 100 XP |
| Unlock store zone | 100 XP |
| First-time milestone | 50–1,000 XP |
| Level-up reward (coins) | 500 × level (every 5 levels) |
| Level-up reward (FT) | 50 × (level ÷ 10) (every 10 levels) |

**XP Formula (cumulative from Lv.1):**
```
XP_to_reach(n) = floor(50 × n² + 150 × n − 200)   for n ≥ 2
XP_to_reach(1) = 0
```

---

## 🔓 Level-by-Level Unlock Summary

| Level | Farm Unlocks | Store Unlocks | Zone / Special |
|-------|-------------|--------------|---------------|
| **1** | Farm Zone 0 (8×8, free), Wheat, Tomato, Carrot, Barn | Bread Shelf, Fruit Stand, Vegetable Rack, Soda Machine, Newspaper Stand | Tutorial begins |
| **2** | Carrot seeds | — | — |
| **3** | Corn seeds | Vending Machine | — |
| **4** | Strawberry seeds | — | — |
| **5** | Bakery Oven, Farm Zone 1 (500 coins), Potato | Egg Display, Music Corner, Store Zone 2 (2,000 coins) | — |
| **6** | Cucumber seeds | Cleaning Supplies | — |
| **7** | — | — | Daily Quests unlock |
| **8** | Sunflower, Compost Shed, Farm Zone 2 (1,500 coins) | Soap & Shampoo, Toy Corner, Aquarium | Collections unlock |
| **10** | Chicken Pen, Sugarcane, Farm Zone 2 (expanded) | Meat Counter, Battery Display, Stationery | Harvest Cards begin (+3/level) |
| **12** | Cow Pen, Cotton, Dairy Factory | Bakery Display, Dairy Fridge, Kids Books | — |
| **14** | Jam Kitchen | — | — |
| **15** | Sheep Pen, Coffee Beans, Farm Zone 3 (3,000 coins) | Cereal Shelf, Book Corner, Store Zone 3 (5,000 coins) | Kids Play Area unlocks |
| **16** | Juice Press | Juice Stand | — |
| **18** | Roastery | Baby Section, Baby Food Section, Hot Drinks Corner | — |
| **20** | Pig Pen, Grapes, Farm Zone 4 (6,000 coins), Farm Market Stand | Pasta Shelf, Phone Accessories, Board Games | Worker Hut unlocks; farm workers available |
| **22** | Chilli seeds, Goat Pen | Chilli Spice Display | — |
| **25** | Lavender, Duck Pen, Cosmetics Lab, Farm Zone 5 begins | Condiment Rack, Makeup Counter, Skincare Display, Store Zone 4 (12,000 coins) | Campaign system unlocks |
| **28** | Hops | — | — |
| **30** | Farm Zone 5 (12,000 coins), Delivery Runner worker | Wine Rack, Home Fragrance, Fountain, Honey & Jam Display | Tool Shed unlock |
| **32** | Brewery | Beer Fridge | — |
| **35** | Winery, Vanilla (Greenhouse ready at Lv.40) | Organic Section, Vitamin Shelf, Store Zone 5 (25,000 coins) | — |
| **40** | Greenhouse Zone 8 (10,000 coins + 200 FT), Cosmetics Lab | Deli Counter, Prepared Meals, Perfume Display, Juice Bar | — |
| **45** | Farm Zone 6 (25,000 coins), Textile Mill, Botanist worker | Clothing Rack, Grand Piano, Store Zone 5 (extended) | — |
| **50** | Chocolate Factory, Saffron (Greenhouse) | Small Appliances, Luxury Beauty, Confectionery Display, Art Gallery, Store Zone 6 (50,000 coins) | Distillery available |
| **55** | Premium Homeware | Accessories Counter, Stage | — |
| **60** | Apiary Zone 9 (30,000 coins + 500 FT), Bees, Honey Studio, Truffle (Greenhouse) | Luxury Fashion, VIP Lounge, Whiskey Display | Mastery Stars: full system active |
| **62** | Honey Studio | Candle Display | — |
| **65** | Rabbit Pen, Perfume Atelier, Farm Zone 7 (50,000 coins) | Store Zone 7 (80,000 coins), Premium Clothing | — |
| **70** | Exotic Orchid (Greenhouse), Master Crafter worker | TV & Media, Gold Inlay Floor | — |
| **72** | — | Perfume Atelier Display | — |
| **80** | Deer Range Zone 10 (80,000 coins + 1,000 FT), Gourmet Kitchen | Gaming Corner, Store Zone 8 (150,000 coins), Champagne Shelf | — |
| **90** | — | Computer Zone | — |
| **100** | All zones maxed | Prestige displays, Royal Wing | Prestige Mode begins |

---

## 🌾 FARM — Complete Mechanics

### 🌱 Crops Master Table

| Crop | Unlock | Grow Time | Wilt Timer | Yield / Harvest | Farm Tokens | Season Bonus | Key Outputs | Sell Value (raw) | XP / Harvest |
|------|--------|-----------|-----------|-----------------|-------------|-------------|-------------|-----------------|-------------|
| 🌾 Wheat | Lv.1 | 5 min | 30 min | 8–12 units | 1 FT | +10% coins (Autumn) | Bread, Flour, Hay, Cereal | 3–5 coins/unit | 3 XP |
| 🍅 Tomato | Lv.1 | 8 min | 45 min | 6–10 units | 1 FT | +25% yield (Summer) | Ketchup, Pasta Sauce, Soup, Juice | 4–6 coins/unit | 3 XP |
| 🥕 Carrot | Lv.2 | 10 min | 1 hr | 6–10 units | 1 FT | +20% yield (Spring) | Veg Rack, Baby Food, Rabbit Feed | 4–6 coins/unit | 3 XP |
| 🌽 Corn | Lv.3 | 15 min | 1.5 hr | 8–14 units | 1 FT | +25% yield (Summer) | Popcorn, Cereal, Pig Feed, Deer Feed | 3–5 coins/unit | 4 XP |
| 🍓 Strawberry | Lv.4 | 12 min | 1 hr | 5–9 units | 2 FT | +20% yield (Spring) | Jam, Smoothies, Pastries | 8–12 coins/unit | 5 XP |
| 🥔 Potato | Lv.5 | 20 min | 2 hr | 10–16 units | 1 FT | +10% coins (Autumn) | Chips, Baby Food, Soup | 4–7 coins/unit | 4 XP |
| 🥒 Cucumber | Lv.6 | 18 min | 1.5 hr | 6–10 units | 1 FT | +25% yield (Summer) | Salad, Pickles, Skincare | 5–8 coins/unit | 4 XP |
| 🌻 Sunflower | Lv.8 | 25 min | 2 hr | 4–7 units | 2 FT | +25% yield (Summer) | Oil, Decoration, Bee Food | 10–15 coins/unit | 5 XP |
| 🎋 Sugarcane | Lv.10 | 30 min | 3 hr | 8–14 units | 2 FT | +25% yield (Summer) | Sugar, Candy, Soft Drinks, Brewery | 6–9 coins/unit | 5 XP |
| 🧵 Cotton | Lv.12 | 45 min | 4 hr | 4–8 units | 3 FT | +25% yield (Summer) | Fabric, Textile Mill → Clothing | 15–20 coins/unit | 7 XP |
| ☕ Coffee Beans | Lv.15 | 1 hr | 6 hr | 4–7 units | 3 FT | All year | Roastery → Roasted Coffee, Hot Drinks | 20–30 coins/unit | 8 XP |
| 🍇 Grapes | Lv.20 | 2 hr | 8 hr | 6–10 units | 4 FT | +10% coins (Autumn) | Wine, Juice, Distillery | 18–25 coins/unit | 10 XP |
| 🌶️ Chilli | Lv.22 | 40 min | 4 hr | 5–9 units | 2 FT | +25% yield (Summer) | Hot Sauce, Spice Display | 12–18 coins/unit | 6 XP |
| 💜 Lavender | Lv.25 | 1.5 hr | 8 hr | 3–6 units | 4 FT | +50% yield (Spring) | Perfume, Cosmetics, Bee Food | 25–35 coins/unit | 10 XP |
| 🍺 Hops | Lv.28 | 2 hr | 12 hr | 5–9 units | 4 FT | +10% coins (Autumn) | Brewery → Craft Beer | 20–28 coins/unit | 10 XP |
| 🌼 Vanilla | Lv.35 | 3 hr | 12 hr | 2–4 units | 6 FT | Greenhouse only | Bakery, Chocolate, Perfume | 40–55 coins/unit | 12 XP |
| 🌸 Saffron | Lv.50 | 6 hr | 24 hr | 1–3 units | 10 FT | Greenhouse only | Luxury Meals, Royal Feast | 80–120 coins/unit | 15 XP |
| 🍄 Truffle | Lv.60 | 12 hr | 24 hr | 1–2 units | 15 FT | Greenhouse only | Gourmet Deli, Royal Feast | 120–180 coins/unit | 15 XP |
| 🌺 Exotic Orchid | Lv.70 | 8 hr | 24 hr | 2–4 units | 12 FT | Greenhouse only | Luxury Beauty, Perfume Atelier | 100–150 coins/unit | 15 XP |

**Crop Plot Size Bonuses (seed cost × plot tiles):**

| Plot Size | Zone Required | Yield Bonus | Seeds Used |
|-----------|--------------|-------------|-----------|
| 1×1 | Any | Base | 1 seed |
| 2×2 | Zone 2+ (Lv.10) | +20% | 4 seeds |
| 3×3 | Zone 4+ (Lv.22) | +50% | 9 seeds |
| 4×4 | Zone 6+ (Lv.45) | +100% | 16 seeds |

**Crop Mastery Bonuses (applies per crop independently):**

| Mastery | Harvests Needed | Bonus |
|---------|----------------|-------|
| ⭐ 1 Star | 25 harvests | +10% yield per plot |
| ⭐⭐ 2 Stars | 100 harvests | +20% yield, +5% FT bonus |
| ⭐⭐⭐ 3 Stars | 300 harvests | +35% yield, +10% FT, wilt timer +50% |

---

### 🐾 Animals Master Table

| Animal | Unlock | Pen Size | Build Cost | Base Capacity | Max Capacity | Upgrade Costs | Product | Cycle Time | Feed | Product Value | XP / Collection |
|--------|--------|----------|-----------|--------------|-------------|--------------|---------|-----------|------|--------------|----------------|
| 🐔 Chicken | Lv.10 | 2×2 | 1,000 coins | 4 chickens | 12 chickens | 500 / 1,000 / 2,000 coins | Eggs (Lv.10) | 10 min | Grain (Wheat) | 8–12 coins/egg | 2 XP |
| 🐄 Cow | Lv.12 | 3×3 | 2,500 coins | 2 cows | 6 cows | 800 / 1,500 / 3,000 coins | Milk | 20 min | Hay (Wheat) | 10–15 coins/unit | 3 XP |
| 🐑 Sheep | Lv.15 | 2×3 | 2,000 coins | 3 sheep | 9 sheep | 600 / 1,200 / 2,400 coins | Wool | 1 hr | Hay | 20–30 coins/unit | 4 XP |
| 🐖 Pig | Lv.20 | 3×3 | 3,500 coins | 2 pigs | 6 pigs | 1,000 / 2,000 / 4,000 coins | Pork + Truffle (10%) | 45 min | Corn Feed | 25–40 coins/pork; 50 FT/truffle | 5 XP |
| 🐐 Goat | Lv.22 | 2×3 | 3,000 coins | 3 goats | 9 goats | 700 / 1,400 / 2,800 coins | Goat Milk | 30 min | Hay | 18–25 coins/unit | 4 XP |
| 🦆 Duck | Lv.25 | 2×2 | 2,500 coins | 4 ducks | 12 ducks | 400 / 800 / 1,600 coins | Duck Eggs + Feathers | 25 min | Grain | 15–20 coins/duck egg | 3 XP |
| 🐝 Bees | Lv.60 | 1×2 | 5,000 coins | 2 hives | 6 hives | 2,000 / 4,000 / 8,000 FT | Honey + Beeswax | 2 hr | Lavender/Sunflower (auto) | 35–50 coins/honey; 20–30 coins/beeswax | 8 XP |
| 🐇 Rabbit | Lv.65 | 2×2 | 6,000 coins | 3 rabbits | 9 rabbits | 1,500 / 3,000 / 6,000 FT | Angora Wool + Lucky Drop | 1.5 hr | Carrot | 50–75 coins/wool; 1 random card | 8 XP |
| 🦌 Deer | Lv.80 | 4×4 | 15,000 coins | 1 deer | 3 deer | 5,000 / 10,000 / 20,000 FT | Velvet + Rare Leather (15%) | 6 hr | Corn + Carrot | 80–120 coins/velvet; 200 coins + 20 FT/leather | 8 XP |

**Animal Happiness Effects:**

| Happiness | Effect |
|-----------|--------|
| 80–100 (Happy) | +25% product quality, bonus product chance |
| 50–79 (Content) | Normal production |
| 20–49 (Sad) | −20% yield |
| 0–19 (Unhappy) | Production paused |

**Animal Mastery Bonuses (applies per animal independently):**

| Mastery | Collections Needed | Bonus |
|---------|--------------------|-------|
| ⭐ 1 Star | 50 collections | +10% product quality |
| ⭐⭐ 2 Stars | 200 collections | +20% quality, bonus product chance doubled |
| ⭐⭐⭐ 3 Stars | 500 collections | +35% quality, +25% special drop chance, happiness regenerates 20% faster |

---

### 🏭 Processing Buildings Master Table

| Building | Unlock | Build Cost | Recipe | Inputs | Output Qty | Process Time | Output Sell Value | XP / Job | Queue (base) |
|---------|--------|-----------|--------|--------|-----------|-------------|-----------------|---------|-------------|
| 🏚️ Barn | Lv.1 | Free | Storage | — | 50 slots | — | — | — | 50 slots |
| 🌿 Compost Shed | Lv.8 | 800 coins | Fertiliser | Animal Waste | 2 fertiliser | 30 min | Not sold directly | 5 XP | 2 slots |
| 🍞 Bakery Oven | Lv.5 | 2,000 coins | Bread | 3 Wheat + 1 Egg | 2 Bread | 10 min | 45 coins/unit | 5 XP | 2 slots |
| 🍞 Bakery Oven | Lv.5 | — | Muffins | 2 Wheat + 1 Egg + 1 Milk | 3 Muffins | 15 min | 60 coins/unit | 6 XP | — |
| 🍞 Bakery Oven | Lv.5 | — | Croissants | 3 Wheat + 2 Milk + 1 Butter | 2 Croissants | 20 min | 85 coins/unit | 8 XP | — |
| 🧀 Dairy Factory | Lv.12 | 3,500 coins | Cheese | 3 Milk | 1 Cheese | 20 min | 70 coins/unit | 6 XP | 2 slots |
| 🧀 Dairy Factory | Lv.12 | — | Yoghurt | 2 Milk + 1 Sugar | 2 Yoghurt | 25 min | 55 coins/unit | 6 XP | — |
| 🧀 Dairy Factory | Lv.12 | — | Butter | 4 Milk | 2 Butter | 15 min | 40 coins/unit | 5 XP | — |
| 🍓 Jam Kitchen | Lv.14 | 3,000 coins | Jam | 3 Strawberry + 1 Sugar | 2 Jam | 15 min | 65 coins/unit | 6 XP | 2 slots |
| 🍓 Jam Kitchen | Lv.14 | — | Jelly | 4 Grapes + 1 Sugar | 2 Jelly | 30 min | 80 coins/unit | 7 XP | — |
| 🥤 Juice Press | Lv.16 | 3,000 coins | Tomato Juice | 4 Tomato | 3 Juice | 15 min | 35 coins/unit | 5 XP | 3 slots |
| 🥤 Juice Press | Lv.16 | — | Grape Juice | 4 Grapes | 3 Juice | 15 min | 50 coins/unit | 6 XP | — |
| 🥤 Juice Press | Lv.16 | — | Smoothie | 3 Strawberry + 2 Carrot | 2 Smoothie | 15 min | 65 coins/unit | 7 XP | — |
| ☕ Roastery | Lv.18 | 4,000 coins | Roasted Coffee | 3 Coffee Beans | 2 Roasted Coffee | 25 min | 75 coins/unit | 8 XP | 2 slots |
| 🍺 Brewery | Lv.32 | 10,000 coins | Craft Lager | 3 Hops + 2 Sugarcane + Yeast | 3 Bottles | 2 hr | 180 coins/bottle | 15 XP | 2 slots |
| 🍺 Brewery | Lv.32 | — | Craft Stout | 4 Hops + 2 Sugarcane + Yeast | 2 Bottles | 2.5 hr | 220 coins/bottle | 18 XP | — |
| 🍷 Winery | Lv.35 | 12,000 coins | Wine | 5 Grapes + 2 Sugar | 2 Bottles | 4 hr | 250 coins/bottle | 20 XP | 2 slots |
| 🧴 Cosmetics Lab | Lv.40 | 15,000 coins | Skincare Cream | 2 Lavender + 2 Goat Milk + 1 Beeswax | 2 Cream | 1 hr | 130 coins/unit | 15 XP | 3 slots |
| 🧵 Textile Mill | Lv.45 | 18,000 coins | Fabric | 4 Wool / 4 Cotton | 2 Fabric | 1.5 hr | 90 coins/fabric | 12 XP | 2 slots |
| 🧵 Textile Mill | Lv.45 | — | Clothing | 3 Fabric | 1 Clothing | 2 hr | 180 coins/clothing | 15 XP | — |
| 🍫 Chocolate Factory | Lv.50 | 20,000 coins | Artisan Chocolate | 2 Sugarcane + 1 Vanilla + 2 Milk | 3 Choc. | 45 min | 120 coins/unit | 15 XP | 3 slots |
| 🍯 Honey Studio | Lv.62 | 12,000 coins | Luxury Honey | 3 Honey | 2 Luxury Honey | 30 min | 95 coins/unit | 10 XP | 3 slots |
| 🍯 Honey Studio | Lv.62 | — | Candles | 2 Beeswax + 1 Honey | 3 Candles | 30 min | 80 coins/candle | 10 XP | — |
| 🥃 Distillery | Lv.65 | 25,000 coins | Whiskey | 4 Grain + 2 Hops | 2 Bottles | 6 hr | 300 coins/bottle | 22 XP | 2 slots |
| 🥃 Distillery | Lv.65 | — | Vodka | 4 Grapes | 2 Bottles | 6 hr | 280 coins/bottle | 20 XP | — |
| 🌸 Perfume Atelier | Lv.70 | 30,000 coins | Luxury Perfume | 2 Lavender + 2 Orchid + 1 Vanilla | 1 Perfume | 3 hr | 400 coins/unit | 25 XP | 2 slots |
| 🍽️ Gourmet Kitchen | Lv.80 | 40,000 coins | Luxury Meal | 1 Truffle + 1 Saffron + 1 Velvet | 2 Meals | 2 hr | 500 coins/meal | 25 XP | 2 slots |

**Processing Building Upgrade Costs & Bonuses:**

| Upgrade Tier | Queue Bonus | Speed Bonus | Cost Range |
|-------------|-------------|-------------|-----------|
| Tier 1 (Base) | Default | Base speed | Free (built-in) |
| Tier 2 | +1 queue slot | −10% time | 1,000–5,000 FT |
| Tier 3 | +2 queue slots | −25% time | 5,000–20,000 FT |
| Tier 4 (Master) | +3 queue slots | −40% time | 20,000–100,000 FT |

**Processing Building Mastery Bonuses:**

| Mastery | Jobs Needed | Bonus |
|---------|-------------|-------|
| ⭐ 1 Star | 50 jobs | +5% yield |
| ⭐⭐ 2 Stars | 200 jobs | +10% yield, +1 queue slot |
| ⭐⭐⭐ 3 Stars | 500 jobs | +20% yield, −15% time, exclusive recipe unlocked |

---

### 🗺️ Farm Zone Expansion

| Zone | Unlock Level | Size Added | Cost | Key New Content | XP on Unlock |
|------|-------------|-----------|------|----------------|-------------|
| Zone 0 (Starter) | Lv.1 | 8×8 | Free | First crops, Barn | — |
| Zone 1 | Lv.5 | +6×8 | 500 coins | More crop plots | 100 XP |
| Zone 2 | Lv.10 | +8×8 | 1,500 coins | Chicken Pen, Cow Pen | 100 XP |
| Zone 3 | Lv.15 | +8×10 | 3,000 coins | Sheep, more crops | 100 XP |
| Zone 4 | Lv.22 | +10×10 | 6,000 coins | Goat, Duck, processing buildings | 100 XP |
| Zone 5 | Lv.30 | +12×10 | 12,000 coins | Premium crop area | 100 XP |
| Zone 6 | Lv.45 | +12×12 | 25,000 coins | Textile Mill, Cotton | 100 XP |
| Zone 7 | Lv.65 | +14×12 | 50,000 coins | Rabbit Pen, Perfume Atelier | 100 XP |
| Zone 8 (Greenhouse) | Lv.40 | Separate 12×8 | 10,000 coins + 200 FT | Vanilla, Saffron, Truffle, Orchid (year-round) | 100 XP |
| Zone 9 (Apiary) | Lv.60 | +8×6 | 30,000 coins + 500 FT | Bees, bee-friendly flowers | 100 XP |
| Zone 10 (Deer Range) | Lv.80 | +16×14 | 80,000 coins + 1,000 FT | Deer, Gourmet Kitchen | 100 XP |

---

## 🏪 STORE — Complete Mechanics

### 🛒 Displays Master Table

#### 🥖 Food & Grocery

| Display | Unlock | Size | Build Cost | Stock Cap | Base Sell Value | Fresh Bonus | Supply | XP / Restock |
|---------|--------|------|-----------|----------|----------------|------------|--------|-------------|
| Bread Shelf | Lv.1 | 2×1 | 500 coins | 20 units | 30 coins/unit | +40% (Farm bread) | Farm / Supplier | 2 XP |
| Fruit Stand | Lv.1 | 2×1 | 500 coins | 24 units | 25 coins/unit | +30% (Farm fruit) | Farm / Supplier | 2 XP |
| Vegetable Rack | Lv.2 | 2×1 | 600 coins | 24 units | 22 coins/unit | +30% (Farm veg) | Farm / Supplier | 2 XP |
| Egg Display | Lv.5 | 1×1 | 800 coins | 30 units | 35 coins/unit | +30% (Farm eggs) | Farm / Supplier | 2 XP |
| Meat Counter | Lv.10 | 3×1 | 2,000 coins | 20 units | 55 coins/unit | +50% (Farm pork) | Farm / Supplier | 2 XP |
| Bakery Display | Lv.12 | 3×2 | 3,500 coins | 18 units | 70 coins/unit | +40% (Farm bread/pastries) | Farm / Supplier | 2 XP |
| Cereal Shelf | Lv.15 | 2×1 | 1,500 coins | 24 units | 40 coins/unit | +30% | Farm / Supplier | 2 XP |
| Pasta Shelf | Lv.20 | 2×1 | 1,500 coins | 24 units | 38 coins/unit | +35% | Supplier | 2 XP |
| Condiment Rack | Lv.25 | 2×1 | 2,000 coins | 20 units | 42 coins/unit | +45% (Farm ketchup) | Farm / Supplier | 2 XP |
| Organic Section | Lv.35 | 3×2 | 5,000 coins | 20 units | 80 coins/unit | +55% (Farm produce) | Farm only | 2 XP |
| Deli Counter | Lv.40 | 3×2 | 6,000 coins | 16 units | 90 coins/unit | +50% | Farm / Supplier | 2 XP |
| Prepared Meals | Lv.40 | 2×2 | 5,000 coins | 16 units | 75 coins/unit | +45% | Farm / Supplier | 2 XP |
| Confectionery Display | Lv.50 | 2×2 | 6,000 coins | 18 units | 85 coins/unit | +50% (Farm chocolate/candy) | Farm / Supplier | 2 XP |
| Spice Display | Lv.22 | 1×1 | 1,500 coins | 20 units | 45 coins/unit | +45% (Farm chilli) | Farm / Supplier | 2 XP |
| Baby Food Section | Lv.18 | 2×1 | 2,000 coins | 20 units | 50 coins/unit | +40% (Farm baby food) | Farm / Supplier | 2 XP |
| Honey & Jam Display | Lv.30 | 2×1 | 3,000 coins | 20 units | 65 coins/unit | +55% (Farm honey/jam) | Farm only | 2 XP |
| Dairy Fridge | Lv.12 | 2×2 | 3,000 coins | 18 units | 60 coins/unit | +50% (Farm dairy) | Farm / Supplier | 2 XP |
| Cheese Counter | Lv.25 | 2×2 | 4,500 coins | 16 units | 75 coins/unit | +55% (Farm cheese) | Farm / Supplier | 2 XP |
| Chocolate Display | Lv.50 | 2×2 | 6,000 coins | 16 units | 95 coins/unit | +60% (Farm artisan choc.) | Farm / Supplier | 2 XP |
| Gourmet Deli | Lv.60 | 3×2 | 12,000 coins | 12 units | 150 coins/unit | +70% (Farm truffle) | Farm only | 2 XP |
| Royal Feast Counter | Lv.80 | 4×2 | 30,000 coins | 10 units | 300 coins/unit | +85% (Farm gourmet meals) | Farm only | 2 XP |
| Farm-to-Table Display | Lv.30 | 4×3 | 10,000 coins | 12 units | 120 coins/unit | +70% Farm only | Farm only | 2 XP |

#### 🥤 Beverages

| Display | Unlock | Size | Build Cost | Stock Cap | Base Sell Value | Farm Mode Bonus | XP / Restock |
|---------|--------|------|-----------|----------|----------------|----------------|-------------|
| Soda Machine | Lv.5 | 1×1 | 800 coins | 40 units | 20 coins/unit | ❌ | 2 XP |
| Juice Stand | Lv.16 | 2×1 | 2,500 coins | 24 units | 45 coins/unit | +50% (Farm juice) | 2 XP |
| Beer Fridge | Lv.32 | 2×2 | 5,000 coins | 16 units | 80 coins/unit | +70% (Farm craft beer) | 2 XP |
| Wine Rack | Lv.30 | 2×2 | 5,500 coins | 16 units | 95 coins/unit | +75% (Farm wine) | 2 XP |
| Hot Drinks Corner | Lv.18 | 2×2 | 4,000 coins | 20 units | 55 coins/unit | +60% (Farm roasted coffee) | 2 XP |
| Smoothie Bar | Lv.25 | 2×2 | 4,500 coins | 18 units | 65 coins/unit | +55% (Farm smoothies) | 2 XP |
| Craft Beer Corner | Lv.35 | 3×2 | 8,000 coins | 14 units | 120 coins/unit | +75% (Farm craft beer) | 2 XP |
| Whiskey Display | Lv.65 | 2×2 | 15,000 coins | 12 units | 180 coins/unit | +80% (Farm whiskey) | 2 XP |
| Champagne Shelf | Lv.80 | 2×2 | 20,000 coins | 12 units | 200 coins/unit | +75% | 2 XP |
| Juice Bar | Lv.40 | 3×2 | 7,000 coins | 16 units | 100 coins/unit | +60% (Farm juice) | 2 XP |

#### 💅 Health & Beauty

| Display | Unlock | Size | Build Cost | Stock Cap | Base Sell Value | Farm Mode Bonus | XP / Restock |
|---------|--------|------|-----------|----------|----------------|----------------|-------------|
| Soap & Shampoo | Lv.8 | 2×1 | 1,000 coins | 24 units | 35 coins/unit | ❌ | 2 XP |
| Vitamin Shelf | Lv.35 | 2×1 | 3,000 coins | 20 units | 60 coins/unit | +40% (Farm honey/herbs) | 2 XP |
| Skincare Display | Lv.25 | 2×2 | 5,000 coins | 16 units | 80 coins/unit | +70% (Farm cosmetics) | 2 XP |
| Makeup Counter | Lv.25 | 3×2 | 6,000 coins | 16 units | 90 coins/unit | ❌ | 2 XP |
| Perfume Display | Lv.40 | 2×2 | 10,000 coins | 12 units | 130 coins/unit | +80% (Farm perfume) | 2 XP |
| Natural Remedies | Lv.35 | 2×1 | 3,500 coins | 20 units | 65 coins/unit | +50% (Farm herbs) | 2 XP |
| Cosmetics Bar | Lv.45 | 3×2 | 9,000 coins | 14 units | 110 coins/unit | +75% (Farm cosmetics) | 2 XP |
| Luxury Beauty | Lv.50 | 3×2 | 15,000 coins | 12 units | 180 coins/unit | +85% (Farm orchid/lavender) | 2 XP |
| Perfume Atelier Display | Lv.72 | 4×2 | 25,000 coins | 10 units | 250 coins/unit | +90% (Farm perfume atelier) | 2 XP |

#### 🧹 Household & Cleaning

| Display | Unlock | Size | Build Cost | Stock Cap | Base Sell Value | Farm Mode | XP / Restock |
|---------|--------|------|-----------|----------|----------------|----------|-------------|
| Cleaning Supplies | Lv.6 | 2×1 | 700 coins | 24 units | 28 coins/unit | ❌ | 2 XP |
| Candle Display | Lv.62 | 2×1 | 6,000 coins | 20 units | 95 coins/unit | +55% (Farm candles) | 2 XP |
| Home Fragrance | Lv.30 | 2×2 | 4,500 coins | 18 units | 70 coins/unit | +60% (Farm perfume) | 2 XP |
| Kitchen Essentials | Lv.12 | 2×1 | 1,200 coins | 24 units | 35 coins/unit | ❌ | 2 XP |
| Laundry Section | Lv.15 | 2×1 | 1,000 coins | 24 units | 30 coins/unit | ❌ | 2 XP |
| Premium Homeware | Lv.55 | 3×2 | 10,000 coins | 14 units | 100 coins/unit | ❌ | 2 XP |

#### 📱 Electronics & Tech

| Display | Unlock | Size | Build Cost | Stock Cap | Base Sell Value | XP / Restock |
|---------|--------|------|-----------|----------|----------------|-------------|
| Battery Display | Lv.10 | 1×1 | 600 coins | 30 units | 25 coins/unit | 2 XP |
| Phone Accessories | Lv.20 | 2×1 | 2,500 coins | 22 units | 50 coins/unit | 2 XP |
| Small Appliances | Lv.50 | 3×2 | 12,000 coins | 14 units | 120 coins/unit | 2 XP |
| TV & Media | Lv.70 | 4×2 | 22,000 coins | 10 units | 200 coins/unit | 2 XP |
| Gaming Corner | Lv.80 | 4×2 | 28,000 coins | 10 units | 250 coins/unit | 2 XP |
| Computer Zone | Lv.90 | 4×2 | 35,000 coins | 10 units | 300 coins/unit | 2 XP |

#### 👗 Clothing & Apparel

| Display | Unlock | Size | Build Cost | Stock Cap | Base Sell Value | Farm Mode Bonus | XP / Restock |
|---------|--------|------|-----------|----------|----------------|----------------|-------------|
| Clothing Rack | Lv.45 | 3×2 | 9,000 coins | 14 units | 110 coins/unit | +50% (Textile Mill) | 2 XP |
| Accessories Counter | Lv.55 | 2×2 | 11,000 coins | 14 units | 130 coins/unit | ❌ | 2 XP |
| Premium Clothing | Lv.65 | 3×2 | 18,000 coins | 12 units | 180 coins/unit | +60% (Textile Mill) | 2 XP |
| Luxury Fashion | Lv.60 | 4×2 | 25,000 coins | 10 units | 280 coins/unit | +70% (Rabbit/Deer leather) | 2 XP |

#### 🧸 Toys, Baby & Books

| Display | Unlock | Size | Build Cost | Stock Cap | Base Sell Value | Farm Mode | XP / Restock |
|---------|--------|------|-----------|----------|----------------|----------|-------------|
| Toy Corner | Lv.8 | 2×2 | 2,000 coins | 20 units | 40 coins/unit | ❌ | 2 XP |
| Baby Section | Lv.18 | 2×2 | 3,000 coins | 20 units | 55 coins/unit | +30% (Farm baby food) | 2 XP |
| Kids Books | Lv.12 | 2×1 | 1,000 coins | 24 units | 35 coins/unit | ❌ | 2 XP |
| Board Games | Lv.20 | 2×2 | 2,500 coins | 18 units | 50 coins/unit | ❌ | 2 XP |
| Educational Toys | Lv.30 | 2×2 | 3,500 coins | 16 units | 65 coins/unit | ❌ | 2 XP |
| Stationery | Lv.10 | 2×1 | 800 coins | 24 units | 30 coins/unit | ❌ | 2 XP |
| Book Corner | Lv.15 | 3×2 | 3,000 coins | 20 units | 55 coins/unit | ❌ | 2 XP |

---

### 🎪 Attractions Master Table

| Attraction | Unlock | Size | Build Cost | LP Bonus | XP on Install | Customer Effect |
|-----------|--------|------|-----------|---------|--------------|----------------|
| 🎵 Music Corner | Lv.5 | 2×2 | 1,000 coins | 50 LP | 50 XP | All nearby spend +5% |
| 🌊 Aquarium | Lv.12 | 4×2 | 5,000 coins | 200 LP | 100 XP | +20% Family Shoppers; all stay 20% longer |
| 🎠 Kids Play Area | Lv.15 | 4×4 | 8,000 coins | 250 LP | 100 XP | +30% Family Shoppers, +15% customer count |
| ⛲ Fountain | Lv.30 | 3×3 | 15,000 coins | 350 LP | 150 XP | +15% all customers, +20% LP aura |
| 🌿 Farm Corner Display | Lv.20 | 4×4 | 12,000 coins | 350 LP | 150 XP | +25% Fresh badge interest, live farm feed |
| 🎸 Grand Piano | Lv.45 | 3×3 | 20,000 coins | 300 LP | 150 XP | +25% Socialite/Businessman spawns |
| 🌺 Indoor Garden | Lv.35 | 4×4 | 22,000 coins | 380 LP | 150 XP | +20% Health Nut/Foodie spawns, Fresh +10% |
| 🖼️ Art Gallery | Lv.40 | 4×3 | 25,000 coins | 400 LP | 200 XP | +30% luxury customer spawns |
| 🍳 Live Kitchen Demo | Lv.55 | 4×3 | 30,000 coins | 420 LP | 200 XP | +30% Foodie spawns, +15% food sales |
| 🎭 Stage | Lv.50 | 6×4 | 35,000 coins | 450 LP | 200 XP | During performance: +40% all customers |
| 🏆 Trophy Wall | Lv.60 | 3×2 | 18,000 coins | 300 LP | 100 XP | Prestige display; needs 10 achievements |
| 🛋️ VIP Lounge | Lv.60 | 4×4 | 50,000 coins | 500 LP | 200 XP | +50% Tycoon/Celebrity/Royalty spawns |

**Attraction Upgrade Costs (each attraction can be upgraded up to Tier 3):**

| Attraction | Tier 2 Upgrade | Tier 2 Effect | Tier 3 Upgrade | Tier 3 Effect |
|-----------|---------------|--------------|---------------|--------------|
| Aquarium | 5,000 coins | Add fish types, +100 LP | 15,000 coins | Live coral theme, +10% effect |
| Kids Play Area | 8,000 coins | Add slide, +50 LP | 20,000 coins | Full adventure zone, +carousel |
| VIP Lounge | 20,000 coins | Add bar service, +100 LP | 40,000 coins | Butler (auto-collect tips) |
| Fountain | 10,000 coins | Add lighting, +50 LP | 25,000 coins | Coin fountain (tap for bonus coins) |
| Grand Piano | 10,000 coins | Extended aura, +50 LP | 20,000 coins | Live Concert event unlocked |

---

### 🗺️ Store Zone Expansion

| Zone | Unlock Level | Size Added | Cost | Key Feature | XP on Unlock |
|------|-------------|-----------|------|------------|-------------|
| Zone 1 (Starter) | Lv.1 | 10×10 | Free | Basic food, beverages | — |
| Zone 2 | Lv.8 | +8×10 | 2,000 coins | Household, cleaning | 100 XP |
| Zone 3 | Lv.15 | +10×10 | 5,000 coins | Kids, toy section | 100 XP |
| Zone 4 | Lv.25 | +12×10 | 12,000 coins | Beauty, fashion | 100 XP |
| Zone 5 | Lv.35 | +12×12 | 25,000 coins | Electronics | 100 XP |
| Zone 6 | Lv.50 | +14×12 | 50,000 coins | Luxury section | 100 XP |
| Zone 7 | Lv.65 | +14×14 | 80,000 coins | VIP area, exclusive items | 100 XP |
| Zone 8 | Lv.80 | +16×14 | 150,000 coins | Royal Wing, premium only | 100 XP |

---

### 🏷️ Coin-Op Items Master Table

| Item | Unlock | Size | Build Cost | Earn Rate | XP on Install | Notes |
|------|--------|------|-----------|----------|--------------|-------|
| 📰 Newspaper Stand | Lv.1 | 1×1 | 200 coins | 15–25 coins / 15 min | 20 XP | Passive income |
| 🎰 Vending Machine | Lv.3 | 1×1 | 500 coins | 20–40 coins / 20 min | 20 XP | Passive income |
| 🏧 ATM | Lv.8 | 1×1 | 1,500 coins | 50–80 coins / 30 min | 50 XP | Attracts Businessman/Socialite |
| 🕹️ Arcade Cabinet | Lv.12 | 2×2 | 3,000 coins | 60–100 coins / 20 min | 50 XP | Synergy with Family Shoppers |
| ☕ Coffee Machine | Lv.18 | 1×1 | 2,000 coins | 40–60 coins / 15 min | 50 XP | Near checkout: +5% all budgets |
| 📸 Photo Booth | Lv.25 | 2×1 | 4,000 coins | 80–120 coins / 30 min | 75 XP | +15% LP when customers use it |
| 🎮 VR Pod | Lv.50 | 2×2 | 15,000 coins | 150–250 coins / 30 min | 150 XP | +Tech customer spawns |
| 🎵 Jukebox | Lv.30 | 1×1 | 3,500 coins | 70–110 coins / 25 min | 75 XP | +Customer happiness |
| 🎲 Prize Claw | Lv.20 | 2×2 | 5,000 coins | 100–160 coins / 30 min | 75 XP | +Family Shopper engagement |
| 🔭 Telescope | Lv.40 | 1×1 | 5,000 coins | 90–140 coins / 30 min | 75 XP | +LP score |

---

## 🔄 Farm → Store Supply Chain Summary

| Farm Output | Processing Step | Store Display | Base Sell Value | Fresh Bonus |
|------------|----------------|--------------|----------------|------------|
| Wheat (raw) | Bakery Oven → Bread | Bread Shelf | 45 coins/unit | +40% |
| Milk (raw) | Dairy Factory → Cheese | Cheese Counter | 70 coins/unit | +55% |
| Strawberry (raw) | Jam Kitchen → Jam | Honey & Jam Display | 65 coins/unit | +55% |
| Grapes (raw) | Winery → Wine | Wine Rack | 250 coins/bottle | +75% |
| Coffee Beans | Roastery → Roasted Coffee | Hot Drinks Corner | 75 coins/unit | +60% |
| Hops + Sugarcane | Brewery → Craft Beer | Craft Beer Corner | 180 coins/bottle | +75% |
| Lavender + Goat Milk + Beeswax | Cosmetics Lab → Skincare | Skincare Display | 130 coins/unit | +70% |
| Wool / Cotton | Textile Mill → Clothing | Clothing Rack | 180 coins/item | +60% |
| Sugarcane + Vanilla + Milk | Chocolate Factory → Artisan Choc. | Chocolate Display | 120 coins/unit | +60% |
| Honey + Beeswax | Honey Studio → Candles | Candle Display | 80 coins/candle | +55% |
| Grapes / Grain + Hops | Distillery → Whiskey | Whiskey Display | 300 coins/bottle | +80% |
| Lavender + Orchid + Vanilla | Perfume Atelier → Luxury Perfume | Perfume Atelier Display | 400 coins/unit | +90% |
| Truffle + Saffron + Velvet | Gourmet Kitchen → Luxury Meal | Royal Feast Counter | 500 coins/meal | +85% |

> 💡 **Fresh Bonus** applies only when supplied directly from the farm via the Supply Lane (Farm Mode). Goods sourced from external suppliers receive base value only.

---

## 📊 XP Progression Reference

| Level | Cumulative XP to Reach | XP Gap from Previous | Coin Reward | FT Reward |
|-------|------------------------|---------------------|------------|----------|
| 1 | 0 | — | — | — |
| 2 | 300 | 300 | — | — |
| 3 | 700 | 400 | — | — |
| 4 | 1,200 | 500 | — | — |
| 5 | 1,800 | 600 | 2,500 coins | — |
| 6 | 2,500 | 700 | — | — |
| 7 | 3,300 | 800 | — | — |
| 8 | 4,200 | 900 | — | — |
| 9 | 5,200 | 1,000 | — | — |
| 10 | 6,300 | 1,100 | 5,000 coins | 50 FT |
| 15 | 13,300 | 1,600 | 7,500 coins | — |
| 20 | 22,800 | 2,100 | 10,000 coins | 100 FT |
| 25 | 34,800 | 2,600 | 12,500 coins | — |
| 30 | 49,300 | 3,100 | 15,000 coins | 150 FT |
| 40 | 85,800 | 4,100 | 20,000 coins | 200 FT |
| 50 | 131,800 | 5,100 | 25,000 coins | 250 FT |
| 60 | 187,800 | 6,100 | 30,000 coins | 300 FT |
| 70 | 253,800 | 7,100 | 35,000 coins | 350 FT |
| 80 | 329,800 | 8,100 | 40,000 coins | 400 FT |
| 90 | 415,800 | 9,100 | 45,000 coins | 450 FT |
| 100 | 511,800 | 10,100 | 50,000 coins | 500 FT |

> See the [XP Calculator on the Index page](../index.html) to calculate your exact level from any XP total.

---

← [Previous — Technical Systems](systems/36-technical-systems.md) | [Back to README](../README.md)
