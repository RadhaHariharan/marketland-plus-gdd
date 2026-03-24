# 🚚 23 — Suppliers & Shipments

The supplier system is the external supply chain that keeps the store stocked when farm production is insufficient or for items not produced on the farm. Shipments arrive by delivery truck on a timer.

---

## 🏭 Supplier Tiers

| Tier | Unlock | Products | Delivery Time | Cost per Shipment |
|------|--------|---------|--------------|------------------|
| Local Supplier | Lv.1 | Basic food, beverages | 30 min | 100–300 coins |
| Regional Supplier | Lv.15 | Extended food, household | 1 hr | 300–600 coins |
| National Supplier | Lv.30 | Electronics, clothing basics | 2 hr | 600–1,200 coins |
| Premium Supplier | Lv.50 | Luxury items, specialty goods | 3 hr | 1,200–3,000 coins |
| Global Supplier | Lv.70 | Rare items, exotic goods | 4 hr | 3,000–8,000 coins |

---

## 🚛 Delivery Truck System

Delivery trucks bring shipments to the store:
- **Default:** 2 truck slots (2 simultaneous shipments in transit)
- Upgrades available: 3 / 4 / 5 truck slots (via coins or Cash)
- Each truck can carry up to 50 items per delivery
- Trucks have a **cooldown** of 30 minutes after unloading before reuse

### Truck Upgrades:
| Upgrade | Cost | Benefit |
|---------|------|---------|
| Extra Truck Slot | 10 Cash | +1 concurrent shipment |
| Bigger Truck | 5,000 coins | +25 items per delivery |
| Express Truck | 8 Cash | −30 min all delivery times |
| Fleet Upgrade | 3,000 coins | All trucks +20% capacity |

---

## 📦 Shipment Process

1. Player opens the **Supplier Panel**
2. Selects supplier tier and items
3. Pays coins upfront
4. Truck dispatched → timer starts
5. Notification when truck arrives
6. Player accepts delivery → items go to stockroom
7. Items placed on displays manually or by Delivery Runner

### Shipment Repair:
If a storm hits while a shipment is in transit:
- 25% chance of damaged goods
- Damaged goods arrive at 50% quantity
- Player can pay **1 Cash** to repair/insure the shipment before it arrives

---

## 📋 Product Cards & Shipments

Product Cards interact with the shipment system in four ways:
1. **Instant Stock** — Immediately fills a display without a truck delivery
2. **Shipment Insurance** — Protects next shipment from storm damage
3. **Stockroom Upgrade** — Permanently increases stockroom capacity by 10 slots
4. **Fifth Display Unlock** — Unlocks a bonus 5th display slot for a chosen aisle

---

## ⏰ Quick Delivery Cards

Quick Delivery Cards speed up shipment timers:
- Each card reduces 1 active shipment timer by **1 hour**
- Multiple cards can be stacked on one shipment
- Earn: +5 per level-up, neighbour gifts, achievements

---

## 🤝 Supplier Relationships

Each supplier has a **Relationship Score** (0–100):
- Increases by ordering regularly (+5 per order)
- Decreases if shipments are cancelled (−10)
- High relationship (80+): 5% discount on all orders
- Max relationship (100): Access to exclusive supplier items not available otherwise

---

← [Previous — Supply Chain](22-supply-chain.md) | [Back to README](../../README.md) | [Next → Stockroom](24-stockroom.md)
