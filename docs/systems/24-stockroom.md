# 📦 24 — Stockroom

The stockroom is the inventory buffer between deliveries/farm production and the store floor. Managing stockroom capacity is a key mid-game challenge.

---

## 🏪 Store Stockroom

### Capacity
| Tier | Slots | Unlock | Cost |
|------|-------|--------|------|
| Starter | 30 slots | Lv.1 | Free |
| Expanded | 60 slots | Lv.10 | 2,000 coins |
| Large | 100 slots | Lv.25 | 8,000 coins |
| Warehouse | 200 slots | Lv.50 | 25,000 coins |
| Mega Warehouse | 500 slots | Lv.75 | 80,000 coins |
| Product Card bonus | +10 slots | Any level | 1 Product Card |

### Stockroom Mechanics:
- Items are grouped by category
- Each item type occupies 1 slot regardless of quantity
- Quantity per slot: unlimited (stacked)
- When stockroom is full, no new deliveries can be accepted and farm supply lane is blocked
- Visual indicator: percentage bar on stockroom icon in HUD

---

## 🌾 Farm Stockroom (Barn)

The farm has its own storage system (the Barn):

| Barn Tier | Slots | Unlock | Cost |
|-----------|-------|--------|------|
| Basic Barn | 50 slots | Lv.1 | Free |
| Extended Barn | 100 slots | Lv.12 | 500 FT |
| Farm Warehouse | 200 slots | Lv.30 | 2,000 FT |
| Grand Barn | 500 slots | Lv.60 | 10,000 FT |

### Barn vs. Stockroom:
| Feature | Barn (Farm) | Stockroom (Store) |
|---------|------------|------------------|
| Currency to upgrade | Farm Tokens | Coins |
| Blocked by | No processing building nearby | Accepting delivery when full |
| Shared with | Workers, processing buildings | Delivery runners, display restocking |
| Overflow | Items held in field (lose wilt protection) | Delivery truck turned away |

---

## 📋 Inventory Management

### Smart Sorting
Players can enable **Smart Sorting** at Lv.20:
- Automatically groups items by category
- Highlights low-stock items (red indicator)
- Suggests reorder points based on sell rate history

### Auto-Restock
At Lv.35, players unlock **Auto-Restock**:
- Set a minimum stock level per display
- System automatically orders from supplier when below threshold
- Costs coins but saves management effort

### Priority Queue
Players set a **Priority Queue** for which displays get restocked first when items are limited:
1. Custom priority (player sets manually)
2. Highest-value display first (auto)
3. Least-stocked display first (auto)
4. Fresh mode displays first (auto)

---

## 🔔 Stockroom Notifications

| Event | Notification |
|-------|-------------|
| Display runs empty | "Your Bread Shelf is empty!" |
| Stockroom 90% full | "Stockroom almost full!" |
| Farm delivery ready | "Farm goods ready for store!" |
| Shipment arrived | "Delivery from [Supplier] has arrived!" |
| Barn full | "Barn is full — harvest may be delayed!" |

---

← [Previous — Suppliers & Shipments](23-suppliers-shipments.md) | [Back to README](../../README.md) | [Next → Customer System](25-customer-system.md)
