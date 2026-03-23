# 🌐 05 — Unified Game World

The defining feature of Marketland+ is that the farm and the store are not separate modes or mini-games — they exist as **one continuous world**, visible at the same time, connected by a real supply lane. This document explains how the two worlds are designed to feel like a single, unified empire.

---

## 🗺️ World Layout

The game world is divided into two adjacent areas visible on the same map:

```
┌────────────────────────────────────────────────────┐
│                   FARM ZONE                        │
│  [Crop Plots] [Animal Pens] [Processing Buildings] │
│                                                    │
│         🚜──────Supply Lane──────🏭                │
│                                                    │
│                   STORE ZONE                       │
│  [Storefront] [Displays] [Stockroom] [Coin-Op]     │
└────────────────────────────────────────────────────┘
```

Players can scroll between zones or tap a **Map Button** to zoom out and see both zones simultaneously on a mini-map.

---

## 🔗 The Supply Lane

The Supply Lane is the physical, visible connection between farm and store. It is a short animated road or conveyor belt that shows:

- 📦 Crates moving from farm stockroom → store stockroom
- Colour-coded by product type (green = produce, yellow = dairy, brown = baked, etc.)
- Speed affected by worker assignment and level upgrades
- Visually upgradable from dirt track → paved road → glass conveyor → golden highway

### Supply Lane States:
| State | Visual | Player Action |
|-------|--------|---------------|
| Empty | Idle animation | N/A |
| Active (manual) | Crates moving | Player tapped "Send to Store" |
| Active (worker) | Automatic crate flow | Delivery Runner assigned |
| Blocked (full stockroom) | Red indicator | Clear store stockroom space |
| Blocked (no goods) | Yellow indicator | Harvest/process more goods |

---

## 💱 Economic Connection

| Farm Action | Store Effect |
|------------|--------------|
| Harvest wheat | Bakery can restock bread shelf (🌿 Fresh, +40%) |
| Collect eggs | Egg display available at +30% value |
| Process milk → cheese | Dairy Fridge restocked at +60% |
| Brew craft beer | Beer Fridge stocked at +75% |
| Process lavender → perfume | Luxury Beauty at +90% |
| All fresh goods | 🌿 Fresh badge shown to customers |

| Store Action | Farm Effect |
|-------------|------------|
| Earn coins | Fund new crop seeds |
| Earn coins | Buy animal pen upgrades |
| Earn coins | Hire farm workers |
| Earn coins | Expand farm zones |
| Complete quests | Earn Farm Tokens |

---

## 🌿 The Fresh Premium System

Any display can be switched between three supply modes:

1. **🏭 Supplier Mode** — Always available. Base coin value. No badge.
2. **🌿 Farm Mode** — Requires active farm stock. +30–90% coins. 🌿 Fresh badge visible to customers.
3. **🔀 Hybrid Mode** — Uses farm stock first; falls back to supplier if farm is empty.

The Fresh Premium multiplier depends on the product category:

| Product Category | Farm Premium |
|-----------------|-------------|
| Eggs, Vegetables | +30% |
| Dairy Products | +40–50% |
| Baked Goods | +40% |
| Jams, Juices | +50% |
| Craft Beer, Wine | +70–75% |
| Cosmetics, Skincare | +80% |
| Luxury Perfume | +90% |
| Gourmet Meals | +85% |

---

## 👁️ UI Integration

The game HUD reflects both worlds simultaneously:
- **Top Bar:** Coins 🪙 | Cash 💵 | Farm Tokens 🌿 | Level + XP bar
- **Bottom Tab Bar:** 🏪 Store | 🌾 Farm | 📋 Quests | 🎴 Cards | 👥 Social
- **Mini-map** (corner): Shows both zones, active workers, ready harvests
- **Supply Lane Indicator:** Shows what's in transit and ETA

---

← [Previous — Leveling & XP](04-leveling-xp.md) | [Back to README](../README.md) | [Next → Farm Overview](farm/06-farm-overview.md)
