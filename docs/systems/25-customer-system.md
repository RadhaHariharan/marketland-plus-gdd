# 👥 25 — Customer System

Customers are the revenue engine of SuperStoreTycoon. With 12 distinct customer types spanning from the penny-pinching Bargain Hunter to the lavish Royalty/VIP, the customer system creates a clear progression ladder tied to the player's Luxury Points score.

---

## 👤 Complete Customer Type Table

| # | Customer Type | Budget Range | LP Required | Fresh Bonus | Special Behaviour |
|---|--------------|-------------|-------------|-------------|-------------------|
| 1 | Bargain Hunter | 50–100 coins | 0 LP | None | Only buys cheapest items; ignores displays over 50 coins |
| 2 | Daily Shopper | 80–150 coins | 100 LP | None | Regular visits; buys variety |
| 3 | Family Shopper | 120–200 coins | 300 LP | None | Buys baby, food, and toy displays; affected by Kids Play Area |
| 4 | Health Nut | 150–250 coins | 600 LP | +25% more likely to buy Fresh | Prefers organic, health displays; Fresh badge increases visit chance |
| 5 | Foodie | 200–350 coins | 1,000 LP | +20% more likely | Buys food & bev; leaves 5-star review; Fresh badge obsession |
| 6 | Office Worker | 250–400 coins | 2,000 LP | Slight preference | Buys electronics, convenience food; fast visits |
| 7 | Fashionista | 300–500 coins | 4,000 LP | None | Clothing, beauty, accessories; ignores food entirely |
| 8 | Businessman | 400–700 coins | 7,000 LP | None | Electronics, wine, premium food; tips in VIP zone |
| 9 | Socialite | 500–900 coins | 11,000 LP | Mild preference | Buys wide variety; leaves positive reviews; attracted to Stage events |
| 10 | Tycoon | 700–1,200 coins | 16,000 LP | Tips on Fresh | Premium everything; tips on all Fresh badge items |
| 11 | Celebrity | 1,000–2,000 coins | 22,000 LP | Fresh only | ONLY buys from Fresh displays or Royal Feast; leaves 5-star review |
| 12 | Royalty/VIP | 2,000–5,000 coins | 30,000 LP | Fresh/Gourmet only | Only shops Fresh and Gourmet displays; skips everything else |

---

## 🧠 Customer AI Behaviour

### Pathfinding
- Customers enter through the store entrance
- They walk to displays their budget can reach
- They stay for 1–5 display visits per session (based on budget)
- Wealthier customers walk further into the store (higher patience)

### Purchase Decision
Each customer evaluates a display based on:
1. **Is it stocked?** (empty → skip)
2. **Can they afford it?** (base price within budget)
3. **Is it their preferred category?** (+30% purchase chance)
4. **Fresh badge preference?** (varies by type)
5. **Campaign active?** (budget boosted by campaign modifier)

### Satisfaction Score
Each customer leaves with a satisfaction score (1–5 stars):
- 5 stars: Found Fresh items, loved the store decor
- 4 stars: Found preferred categories
- 3 stars: Basic visit
- 2 stars: Empty shelves, or no preferred items
- 1 star: Nothing to buy

High satisfaction → return visits more frequent → more coins per day.

---

## 🌟 Special Customers

### Mystery Shopper
- Appears randomly (3× more likely in Fog weather)
- Unknown to the player until they leave
- If satisfied (5 stars), rewards: 500–2,000 bonus coins + 1 Product Card
- If unsatisfied: no penalty, but missed opportunity

### Inspector Customer (unlocks Lv.30)
- Appears monthly
- Evaluates store quality rigorously
- Score affects store Star Rating for the next month

### Neighbour Customer (social feature)
- Friend's avatar visits your store
- Buys 1 item from your most expensive display
- Leaves a gift (coins/card) as a return visit reward

---

## 🎪 Campaign Effects on Customers

| Campaign | Customer Effect |
|---------|----------------|
| Flash Sale | All budgets +20% for 4 hours |
| Farm Fresh Festival | Farm display customer count +40% for 8 hours |
| Grand Sale | All budgets +50% for 12 hours |
| Harvest Mega Event | All budgets +65% (farm displays +90%) for 24 hours |
| VIP Night | VIP/Celebrity/Tycoon only; budgets +60% for 6 hours |

---

← [Previous — Stockroom](24-stockroom.md) | [Back to README](../../README.md) | [Next → Card System](26-card-system.md)
