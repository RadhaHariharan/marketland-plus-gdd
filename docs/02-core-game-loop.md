# 🔄 02 — Core Game Loop

The core game loop is designed around three nested cycles: the **Minute Loop** (active play), the **Hour Loop** (background progress), and the **Session Loop** (strategic decisions). Together they ensure players always have something rewarding to do, whether they play for two minutes or two hours.

---

## ⏱️ The Minute Loop (Active Play)

This is what happens every time a player opens the game and actively engages:

1. **Check store** — customers are browsing; tap to collect coins from completed shelves
2. **Restock shelves** — drag items from stockroom to empty display slots
3. **Check farm** — harvest ready crops, collect animal products
4. **Queue processing** — send raw goods to bakery, dairy, jam kitchen, etc.
5. **Complete quests** — tick off daily tasks for XP and card rewards
6. **Run campaigns** — spend Shopper Cards to boost customer budgets
7. **Upgrade** — spend coins/tokens to level up displays, plant new crops, hire workers

> 💡 **Design Note:** Every tap in the minute loop generates visible, satisfying feedback — coin pop-ups, harvest animations, supply lane movement.

---

## ⏰ The Hour Loop (Background Progress)

While the player is away, the game continues working:

| Background Process | Duration | Player Action on Return |
|-------------------|----------|------------------------|
| Crop Growth | 5 min – 12 hr | Harvest → send to stockroom |
| Animal Production | 10 min – 6 hr | Collect → feed → collect again |
| Processing Jobs | 10 min – 6 hr | Collect finished goods |
| Supplier Shipment | 30 min – 4 hr | Accept delivery → stockroom |
| Farm Supply Lane | Continuous | Automatically stocked if worker present |
| Quest Reset | 24 hr | New daily quests refresh |

---

## 📅 The Session Loop (Strategic Decisions)

Each play session, players make medium-term decisions:

1. **Which crops to plant** — balancing growth time vs. store demand
2. **Which display to stock with Farm vs. Supplier mode**
3. **When to launch a Campaign** — timing for maximum revenue
4. **Which buildings to upgrade** — unlocking higher-tier processing
5. **Which zones to expand** — farm zones vs. store zones vs. greenhouse
6. **Which workers to assign** — optimising idle production

---

## 🗺️ Full Loop Diagram

```
FARM SIDE                         STORE SIDE
─────────────────────────────────────────────────────
Plant Crops → Grow → Harvest       Customers Arrive
     ↓                                    ↑
Collect Animal Products        Stock Displays ← Stockroom
     ↓                                    ↑
Queue Processing Jobs ──► Finished Goods ──► Supply Lane
     ↓                                    ↑
Spend Farm Tokens      Earn Coins → Upgrade Displays
     ↓                                    ↑
Upgrade Farm Buildings ←──── Reinvest Profits ────────
```

---

## 🎯 Retention Hooks

| Hook | Mechanism |
|------|-----------|
| 📬 Return Notification | "Your wheat is ready to harvest!" |
| 🎁 Daily Bonus | Login streak rewards (coins + cards) |
| 📋 Daily Quests | Fresh tasks every 24 hours |
| 🏆 Collection Progress | Tantalisingly close collection completions |
| 🎪 Seasonal Events | Time-limited festivals every 2 weeks |
| 👥 Neighbour Gifts | Social layer sends daily gifts |

---

← [Previous — Game Overview](01-game-overview.md) | [Back to README](../README.md) | [Next → Currency System](03-currency-system.md)
