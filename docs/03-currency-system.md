# 💰 03 — Currency System

SuperStoreTycoon uses **three distinct currencies**, each with a clear role in the economy. This layered approach keeps the economy balanced, prevents inflation, and ensures that each type of progression feels distinct and rewarding.

> 💡 **Design Change:** Farm Tokens have been removed. Players now use **Coins and Cash** for all farm and store operations, keeping the economy unified and simple.

---

## 🪙 Currency 1: Coins (Soft Currency)

**Symbol:** 🪙 | **Type:** Soft (earnable through play) | **Starting Amount:** 500

Coins are the primary currency and the backbone of all farm and store operations.

### Earn Coins By:
- Customers purchasing from displays (main source)
- Coin-op items (ATM, vending machines, ticket machines)
- Completing daily quests
- Campaign bonuses
- Selling overstock from stockroom
- Completing collections
- Neighbour visits
- Harvesting crops (bonus coin yield on harvest)
- Collecting animal products

### Spend Coins On:
**Store:**
- Buying new display units
- Upgrading displays to higher tiers
- Purchasing supplier shipments
- Unlocking store zones
- Buying decorations and attractions
- Replenishing display stock (in Supplier mode)

**Farm:**
- Buying seeds (all crops)
- Hiring and paying farm workers
- Upgrading processing buildings
- Unlocking farm zones
- Purchasing animal food upgrades
- Unlocking greenhouse slots

### Farm Coin Costs:
| Item | Coin Cost |
|------|-----------|
| Wheat seeds (×10) | 50 coins |
| Exotic Orchid seeds (×5) | 600 coins |
| Animal food upgrade | 200–1,000 coins |
| Processing building upgrade | 500–5,000 coins |
| Farm zone unlock | 1,000–10,000 coins |
| Worker hire | 200–800 coins |
| Greenhouse slot unlock | 2,000 coins |

### Crop Coin Yield (on harvest):
| Crop | Coins per Harvest |
|------|------------------|
| Wheat, Tomato, Carrot, Corn, Potato, Cucumber | 5–10 coins |
| Strawberry, Sunflower, Sugarcane, Chilli | 10–20 coins |
| Coffee Beans, Cotton | 20–30 coins |
| Grapes, Lavender, Hops | 30–40 coins |
| Vanilla | 50–70 coins |
| Exotic Orchid | 100–130 coins |
| Saffron | 90–110 coins |
| Truffle | 120–160 coins |

> 💡 **Design Note:** Coins should always feel abundant but never surplus — there should always be a meaningful upgrade to spend them on, both in the farm and the store.

---

## 💵 Currency 2: Cash (Premium Currency)

**Symbol:** 💵 | **Type:** Premium (real money OR earned in-game) | **Starting Amount:** 10

Cash is the premium currency but is intentionally earnable through regular play to avoid paywalls.

### Earn Cash By:
- Leveling up (+1 Cash per level)
- Completing achievements (variable)
- Watching optional rewarded ads (small amounts)
- Purchasing with real money (optional)

### Spend Cash On:
| Action | Cash Cost |
|--------|-----------|
| Instant crop harvest | 1–3 Cash |
| Skip processing timer | 1–5 Cash |
| Instant supplier delivery | 2–5 Cash |
| Repair storm-damaged crops | 1 Cash |
| Premium decoration items | 5–20 Cash |
| Extra delivery truck slot | 10 Cash |
| Unlock farm/store zone immediately | 10–30 Cash |
| Skip quest | 3 Cash |
| Rare animal direct purchase | 15–50 Cash |
| Instant processing building upgrade | 5–20 Cash |

> 💡 **Design Note:** Cash **never** gates core content. It only speeds up timers or provides cosmetic/convenience options. All content is reachable without spending Cash.

---

## 💎 Currency 3: Luxury Points (LP Score)

**Symbol:** 💎 | **Type:** Score (accumulated, never spent) | **Starting Amount:** 0

Luxury Points are a **score**, not a spendable currency. They accumulate as players place decorations, attractions, and premium displays. A higher LP score unlocks wealthier customer types who spend significantly more per visit.

### Earn Luxury Points By:
- Placing decorations (1–50 LP each)
- Installing attractions (50–500 LP each)
- Placing coin-op items (5–30 LP each)
- Upgrading display tiers (5–25 LP each upgrade)
- Completing store expansions (100–500 LP per zone)

### LP → Customer Unlock Tiers:
| LP Threshold | Unlocked Customer | Budget Range |
|-------------|-------------------|-------------|
| 0 | Bargain Hunter | 50–100 coins |
| 100 | Daily Shopper | 80–150 coins |
| 300 | Family Shopper | 120–200 coins |
| 600 | Health Nut | 150–250 coins |
| 1,000 | Foodie | 200–350 coins |
| 2,000 | Office Worker | 250–400 coins |
| 4,000 | Fashionista | 300–500 coins |
| 7,000 | Businessman | 400–700 coins |
| 11,000 | Socialite | 500–900 coins |
| 16,000 | Tycoon | 700–1,200 coins |
| 22,000 | Celebrity | 1,000–2,000 coins |
| 30,000 | Royalty/VIP | 2,000–5,000 coins |

> 💡 **Design Note:** LP is purely accumulative — players never lose LP. This means a beautifully decorated store permanently attracts premium customers, rewarding long-term investment.

---

← [Previous — Core Game Loop](02-core-game-loop.md) | [Back to README](../README.md) | [Next → Leveling & XP](04-leveling-xp.md)