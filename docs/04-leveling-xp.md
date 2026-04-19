# ⭐ 04 — Leveling & XP System

The leveling system is the backbone of progression in SuperStoreTycoon. Every meaningful action earns XP, and every level unlocked opens new content across both the farm and the store. With 200+ levels, there is always something just ahead on the horizon.

---

## 📈 XP Sources

| Action | XP Earned |
|--------|-----------|
| Customer purchase (per visit) | 1–5 XP |
| Restock a display shelf | 2 XP |
| Complete a daily quest | 50–200 XP |
| Complete a story quest | 100–500 XP |
| Harvest a crop | 3–15 XP |
| Collect animal product | 2–8 XP |
| Complete a processing job | 5–25 XP |
| Complete a collection | 50–300 XP |
| Run a campaign (completion) | 10% bonus XP on all earnings |
| Place a new decoration | 5–20 XP |
| Install an attraction | 50–200 XP |
| Unlock a farm zone | 100 XP |
| Unlock a store zone | 100 XP |
| First-time milestones | 50–1,000 XP |

---

## 📊 Level Progression Curve

| Level Range | XP per Level | Estimated Time |
|-------------|-------------|----------------|
| 1–10 | 500–2,000 | Minutes per level |
| 11–25 | 2,000–8,000 | 30–60 min per level |
| 26–50 | 8,000–25,000 | 1–3 days per level |
| 51–75 | 25,000–80,000 | 3–7 days per level |
| 76–100 | 80,000–200,000 | 1–2 weeks per level |
| 101–200 | 200,000+ | Prestige pace |

---

## 🧮 XP Formula & Mathematical Calculations

### Master Formula — XP required to reach level `n` (cumulative from level 1)

```
XP_to_reach(n) = floor( 50 × n² + 150 × n − 200 )    for n ≥ 2
XP_to_reach(1) = 0  (everyone starts at level 1 with 0 XP)
```

**Sample values:**
- XP to reach level 2 = floor(50×4 + 150×2 − 200) = floor(200 + 300 − 200) = **300**
- XP to reach level 3 = floor(50×9 + 150×3 − 200) = floor(450 + 450 − 200) = **700**
- XP to reach level 5 = floor(50×25 + 150×5 − 200) = floor(1250 + 750 − 200) = **1,800**
- XP to reach level 10 = floor(50×100 + 150×10 − 200) = floor(5000 + 1500 − 200) = **6,300**

---

### Delta Formula — XP required to go from level `n` to level `n+1`

```
XP_delta(n → n+1) = XP_to_reach(n+1) − XP_to_reach(n)
                  = floor(50(n+1)² + 150(n+1) − 200) − floor(50n² + 150n − 200)
                  ≈ 100n + 200   (simplified linear approximation)
```

Each level costs approximately **100 more XP** than the one before it, giving the curve a steady ramp-up feel.

---

### Reverse Formula — Given total XP, find current level

Starting from the master formula `XP = 50n² + 150n − 200`, rearranging as a quadratic in `n`:

```
50n² + 150n − (XP + 200) = 0
```

Applying the quadratic formula (taking the positive root):

```
n = (−150 + sqrt(150² + 4 × 50 × (XP + 200))) / (2 × 50)
  = (−150 + sqrt(22500 + 200 × (XP + 200))) / 100
  = (−150 + sqrt(22500 + 200×XP + 40000)) / 100
  = (sqrt(200×XP + 62500) − 150) / 100
```

Taking the floor gives the current level:

```
level = floor( (sqrt(200 × XP + 62500) − 150) / 100 )
```

---

### 📐 Worked Example — Player has 100 total XP

**Step 1 — Find current level:**

```
level = floor( (sqrt(200 × 100 + 62500) − 150) / 100 )
      = floor( (sqrt(20000 + 62500) − 150) / 100 )
      = floor( (sqrt(82500) − 150) / 100 )
      = floor( (287.23 − 150) / 100 )
      = floor( 137.23 / 100 )
      = floor( 1.3723 )
      = 1
```

➡ **Player is at Level 1**

**Step 2 — XP required to reach Level 2:**

```
XP_to_reach(2) = floor(50 × 2² + 150 × 2 − 200)
               = floor(50 × 4 + 300 − 200)
               = floor(200 + 300 − 200)
               = floor(300)
               = 300 XP
```

**Step 3 — XP already accumulated toward next level:**

```
XP_in_current_level = 100 − XP_to_reach(1) = 100 − 0 = 100 XP
```

**Step 4 — XP still needed for next level:**

```
XP_needed = XP_to_reach(2) − current_total_XP
           = 300 − 100
           = 200 XP
```

➡ **Answer: Player is Level 1, needs 200 more XP to reach Level 2** (has 100/300 XP = 33.3% of the way there).

---

### 📋 Reference Table — First 10 Levels

| Level | Cumulative XP to reach | XP gap from previous level |
|-------|------------------------|---------------------------|
| 1     | 0                      | —                         |
| 2     | 300                    | 300                       |
| 3     | 700                    | 400                       |
| 4     | 1,200                  | 500                       |
| 5     | 1,800                  | 600                       |
| 6     | 2,500                  | 700                       |
| 7     | 3,300                  | 800                       |
| 8     | 4,200                  | 900                       |
| 9     | 5,200                  | 1,000                     |
| 10    | 6,300                  | 1,100                     |

---

### 💻 Pseudocode Implementation

```pseudocode
function getCurrentLevel(totalXP):
    return floor( (sqrt(200 * totalXP + 62500) - 150) / 100 )

function xpToReachLevel(n):
    if n <= 1: return 0
    return floor(50 * n * n + 150 * n - 200)

function xpNeededForNextLevel(totalXP):
    currentLevel = getCurrentLevel(totalXP)
    nextLevelThreshold = xpToReachLevel(currentLevel + 1)
    return nextLevelThreshold - totalXP
```

---

## 🎁 Level-Up Rewards

Every level grants rewards from the following pool:

| Reward | Always? | Amount |
|--------|---------|--------|
| 💵 Cash | Yes | +1 Cash every level |
| 🎴 Quick Delivery Cards | Yes | +5 per level |
| 🎴 Product Cards | Yes | +5 per level |
| 🎴 Harvest Cards | Lv.10+ | +3 per level |
| 🎴 Shopper Cards | Yes | +2 per level |
| New unlock (display/crop/animal) | Milestone levels | See unlock table |
| Bonus coins | Every 5 levels | 500 × level |
| Farm Token bonus | Every 10 levels | 50 × (level/10) |

---

## 🔓 Campaign XP Bonuses

Campaigns boost XP earnings during their duration:

| Campaign | XP Bonus |
|----------|----------|
| Flash Sale | +10% |
| Farm Fresh Festival | +25% |
| Grand Sale | +30% |
| Harvest Mega Event | +50% |
| VIP Night | +40% |

---

## 🌟 Prestige System (Level 100+)

At Level 100, players unlock **Prestige Mode**:
- XP requirements reset but scale differently
- New Prestige-exclusive displays and decorations unlock
- A **Prestige Star** badge appears on the player's store
- Each prestige tier (P1, P2...) grants permanent bonuses:
  - P1: +5% all coin earnings
  - P2: +10% Farm Token yield
  - P3: +15% customer budget boost
  - P4: Exclusive Royal Tier decorations
  - P5+: Legendary status + exclusive seasonal content

---

← [Previous — Currency System](03-currency-system.md) | [Back to README](../README.md) | [Next → Unified Game World](05-unified-game-world.md)
