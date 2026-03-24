# 🔄 16 — Supply Modes

Every display in Marketland+ supports three supply modes, giving players direct control over whether their shelves are stocked from the farm or from external suppliers. This is the central mechanic that connects the two halves of the game.

---

## 🏭 Mode 1: Supplier Mode

**Icon:** 🏭 | **Always available** | **Base coin value**

In Supplier Mode, the display is restocked by ordering from external suppliers via the shipment system. No farm involvement is required.

| Property | Value |
|----------|-------|
| Availability | Always (as long as player can afford shipment) |
| Restock time | Depends on supplier tier (30 min – 4 hr) |
| Fresh badge | ❌ No |
| Coin multiplier | 1× (base) |
| Stock limit | Unlimited (pay per shipment) |
| Best for | New players, products not grown on farm |

---

## 🌿 Mode 2: Farm Mode

**Icon:** 🌿 | **Requires active farm stock** | **30–90% coin bonus**

In Farm Mode, the display is restocked exclusively from the farm's supply lane. When farm stock runs out, the display sits empty until restocked.

| Property | Value |
|----------|-------|
| Availability | Requires farm to produce the relevant good |
| Restock time | Instant (from farm stockroom via Supply Lane) |
| Fresh badge | ✅ Yes — displayed prominently to customers |
| Coin multiplier | 1.3× to 1.9× (30–90% more) |
| Stock limit | Limited to what the farm produces |
| Best for | High-value items, attracting premium customers |

### Farm Mode Premium by Category:
| Product Category | Coin Multiplier |
|-----------------|----------------|
| Eggs, Raw Vegetables | ×1.30 |
| Dairy Products | ×1.40 – ×1.50 |
| Baked Goods | ×1.40 |
| Jams, Juices, Smoothies | ×1.50 |
| Craft Beer | ×1.70 |
| Wine | ×1.75 |
| Cosmetics, Skincare | ×1.80 |
| Luxury Perfume | ×1.90 |
| Gourmet Meals | ×1.85 |
| Artisan Chocolates | ×1.65 |

---

## 🔀 Mode 3: Hybrid Mode

**Icon:** 🔀 | **Recommended for most displays**

Hybrid Mode is the intelligent combination: the display uses farm stock first, and automatically falls back to supplier stock if the farm inventory runs dry.

| Property | Value |
|----------|-------|
| Availability | Always |
| Fresh badge | ✅ Yes (when farm stock available) / ❌ No (when supplier fallback active) |
| Coin multiplier | Farm rate when farm active; base rate on supplier fallback |
| Best for | Maximising revenue without risking empty shelves |

> 💡 **Design Note:** Hybrid Mode is the recommended setting for most mid-to-late-game players. It ensures revenue continuity while capturing the Fresh premium whenever possible.

---

## 🔧 Switching Modes

- Players can switch modes at any time by tapping the display → Supply Mode button
- Switching costs no coins or tokens
- Mode preference is saved per display
- **Delivery Runner** worker automatically routes goods to Farm Mode and Hybrid Mode displays first

---

## 📊 Revenue Comparison Example

**Scenario:** Dairy Fridge display, 20 units stocked

| Mode | Coins per Unit | Total Coins | Fresh Badge |
|------|---------------|-------------|-------------|
| Supplier | 60 | 1,200 | ❌ |
| Farm (Cow Milk → Dairy Factory → Cheese) | 90 | 1,800 | ✅ |
| Hybrid (farm available) | 90 | 1,800 | ✅ |
| Hybrid (farm empty → supplier fallback) | 60 | 1,200 | ❌ |

**Annual projection:** A fully farmed 20-display store earns approximately **65% more coins per day** than a fully supplier-stocked store.

---

## 👥 Customer Interaction With Fresh Badge

When a display has the 🌿 Fresh badge active:
- **Health Nut** customers: +25% chance to buy from this display
- **Foodie** customers: +20% chance, leave 5-star review
- **Tycoon** customers: Tips on all Fresh item purchases
- **Celebrity** customers: Only buy from Fresh or Gourmet displays
- **Royalty/VIP** customers: Only shop Fresh/Gourmet; skip all Supplier-only displays

---

← [Previous — Store Grid & Layout](15-store-grid-layout.md) | [Back to README](../../README.md) | [Next → Displays — All Categories](17-displays-all.md)
