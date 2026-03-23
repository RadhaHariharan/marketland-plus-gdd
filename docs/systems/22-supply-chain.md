# 🔗 22 — Supply Chain

The Supply Chain is the living connection between the farm and the store. It encompasses how goods move from crop plot to store shelf, and what happens to them at each stage of the journey.

---

## 🗺️ Full Supply Chain Flow

```
Stage 1: PRODUCTION
   Crop Plot (harvest) → Barn Storage
   Animal Pen (collect) → Barn Storage

Stage 2: PROCESSING (optional, adds value)
   Barn Storage → Processing Building → Processed Goods → Barn Storage

Stage 3: STAGING
   Barn Storage → Farm Stockroom (sorted by type)

Stage 4: TRANSPORT
   Farm Stockroom → Supply Lane → Store Stockroom

Stage 5: SHELVING
   Store Stockroom → Display Shelf (manual or by Delivery Runner)

Stage 6: SALE
   Customer purchases from shelf → Coins earned → Player collects
```

---

## 📦 Supply Lane Details

The Supply Lane is the visible road/conveyor between farm and store:

| Property | Default | Upgrades Available |
|----------|---------|------------------|
| Capacity per run | 20 items | 40 / 60 / 100 |
| Transit time | 5 minutes | 3 min / 2 min / 1 min |
| Runs per hour (manual) | 2 | 3 / 4 |
| Runs per hour (with Delivery Runner) | 4 | 6 / 8 |
| Visual | Dirt track | Paved / Glass / Golden |

### Supply Lane Upgrades:
| Tier | Cost | Capacity | Speed | Visual |
|------|------|---------|-------|--------|
| Basic | Free | 20 items | 5 min | Dirt track |
| Improved | 3,000 coins | 40 items | 3 min | Paved road |
| Advanced | 10,000 coins | 60 items | 2 min | Cobblestone |
| Premium | 30,000 coins | 100 items | 90 sec | Glass conveyor |
| Golden | 100,000 coins | Unlimited | 60 sec | Golden highway |

---

## 🌿 Fresh Badge Tracking

The supply chain system tracks the origin of each batch of goods:
- Items tagged as **FARM-ORIGIN** at harvest retain their tag through processing
- Farm-origin items receive the 🌿 Fresh badge when placed on a display
- Supplier-origin items never receive the Fresh badge
- In **Hybrid Mode**, the system automatically distinguishes origin

### Fresh Tag Chain:
```
Wheat (FARM-ORIGIN) → Bakery Oven → Bread (retains FARM-ORIGIN) → Display → 🌿 Fresh Badge
Wheat (SUPPLIER-ORIGIN) → Bakery Oven → Bread (no tag) → Display → No badge
```

---

## 📊 Supply Chain Optimisation Tips

| Problem | Solution |
|---------|----------|
| Display always empty | Add Delivery Runner, upgrade Supply Lane capacity |
| Farm goods not reaching store | Check supply lane isn't blocked (full stockroom) |
| Processing bottleneck | Upgrade building to Tier 3+, add Kitchen Hand |
| Farm producing faster than store sells | Increase store display count or run a campaign |
| Store selling faster than farm produces | Add more crop plots, hire Field Hand |

---

## 🔄 Supply Chain vs. Supplier System

Both systems coexist:

| Aspect | Farm Supply Chain | Supplier System |
|--------|------------------|-----------------|
| Cost | Farm Tokens (seeds/animals) + time | Coins per shipment |
| Revenue | +30–90% vs. supplier | Base rate |
| Speed | Continuous flow | Delivery every 30 min–4 hr |
| Risk | Weather, wilting | Shipment delays |
| Best for | Premium goods, Fresh badge | Gap-filling, non-farm items |

---

← [Previous — Store Expansion](../store/21-store-expansion.md) | [Back to README](../../README.md) | [Next → Suppliers & Shipments](23-suppliers-shipments.md)
