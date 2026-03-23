# 👷 11 — Farm Workers

Farm workers are AI-controlled characters that automate repetitive farm tasks, freeing the player to focus on strategy and expansion. They are hired once (with coins) and work continuously without upkeep costs.

---

## 👨‍🌾 Complete Worker Table

| Worker | Unlock | Primary Task | Hire Cost | Max Assigned |
|--------|--------|-------------|-----------|-------------|
| 🧑‍🌾 Field Hand | Lv.20 | Waters + harvests crops, clears weeds | 500 coins | 3 per zone |
| 🐄 Animal Keeper | Lv.22 | Feeds animals, collects products, cleans pens | 700 coins | 2 per pen area |
| 🧑‍🍳 Kitchen Hand | Lv.25 | Queues processing jobs automatically | 800 coins | 1 per building |
| 🚚 Delivery Runner | Lv.30 | Moves farm goods to store via Supply Lane | 1,200 coins | 2 total |
| 🌿 Botanist | Lv.45 | Applies fertiliser, manages crop rotation | 1,500 coins | 1 per zone |
| 👩‍🔬 Master Crafter | Lv.70 | Manages full multi-step crafting chains | 3,000 coins | 1 total |

---

## 🤖 Worker AI Behaviour

### 🧑‍🌾 Field Hand
- Patrols assigned zone in a defined path
- Waters unwatered crops first (highest priority)
- Harvests ready crops and deposits in Barn
- Clears wilted crops (replants if seeds available)
- Clears weeds that appear randomly on unused tiles
- **Efficiency Tip:** Short patrol paths = more crops per hour

### 🐄 Animal Keeper
- Checks feed levels every cycle
- Collects products when ready and deposits in Barn
- Cleans pens to maintain happiness (every 3 cycles)
- Will not overfeed — smart scheduling prevents waste
- **Efficiency Tip:** Assign one keeper per animal pen cluster

### 🧑‍🍳 Kitchen Hand
- Checks Barn inventory every 5 minutes
- Identifies available recipe inputs
- Queues highest-value recipe first
- Collects finished goods and returns to Barn
- Respects player-set recipe priority order
- **Efficiency Tip:** Set priority to chain ingredients to enable Master Crafter

### 🚚 Delivery Runner
- Checks Barn for finished goods
- Checks store stockroom for available space
- Makes delivery runs: Barn → Supply Lane → Store Stockroom
- Can carry 20 items per run (upgradeable to 40/60)
- Makes up to 4 runs per hour
- **Efficiency Tip:** Upgrade Supply Lane to increase runner speed

### 🌿 Botanist
- Manages Compost Shed queue automatically
- Applies fertiliser to plots based on crop value (highest value first)
- Rotates which crops are planted to maximise seasonal bonuses
- Suggests optimal crop layout (info panel for player)
- **Efficiency Tip:** Pair with Field Hand for fully automated crop cycle

### 👩‍🔬 Master Crafter
- Understands all multi-step chains
- Coordinates Kitchen Hand workers across buildings
- Prioritises chains based on store demand data
- Manages intermediate storage between chain steps
- Sends alerts when a chain ingredient is running low
- **Efficiency Tip:** The only worker that requires a Tool Shed at Lv.3

---

## 🏡 Worker Facilities

| Building | Unlock | Effect |
|----------|--------|--------|
| Worker Hut | Lv.20 | Required before hiring any worker; max 3 workers |
| Extended Worker Hut | Lv.35 | Upgrade; max 6 workers |
| Tool Shed | Lv.30 | +20% all worker efficiency |
| Break Room | Lv.50 | Workers never lose efficiency (100% uptime) |
| Master Workshop | Lv.70 | Unlocks Master Crafter; further +10% efficiency |

---

## 📈 Worker Upgrades

Each worker can be upgraded individually for coins:

| Upgrade | Cost | Benefit |
|---------|------|---------|
| Speed Boost (Tier 1) | 300 coins | +20% movement speed |
| Speed Boost (Tier 2) | 800 coins | +40% movement speed |
| Capacity Boost | 500 coins | Carries 1.5× items per trip |
| Multi-task | 1,200 coins | Can manage 2 task types simultaneously |
| Expert Training | 2,000 coins | +25% efficiency bonus |

---

← [Previous — Crafting Chains](10-crafting-chains.md) | [Back to README](../../README.md) | [Next → Seasons & Weather](12-seasons-weather.md)
