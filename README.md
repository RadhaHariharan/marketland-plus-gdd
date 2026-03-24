# 🏪🌾 Marketland+ — Farm & Supermarket Empire

> **Complete Game Design Document** — Version 3.0

![Version](https://img.shields.io/badge/Version-3.0-blue?style=for-the-badge)
![Engine](https://img.shields.io/badge/Engine-Unity-black?style=for-the-badge&logo=unity)
![Genre](https://img.shields.io/badge/Genre-Casual%20Simulation-green?style=for-the-badge)
![No Energy](https://img.shields.io/badge/No%20Energy%20System-%E2%9C%85-brightgreen?style=for-the-badge)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-orange?style=for-the-badge&logo=github)

---

## 🎮 About the Game

**Marketland+** is a single unified casual simulation game where you own both a **supermarket** AND a **farm** as one connected business empire. Grow crops, raise animals, and process raw goods in factory buildings on your farm — then watch them travel via a visible Supply Lane to your store's stockroom. Stock shelves, serve customers, run marketing campaigns, and reinvest profits to expand both sides of your empire. Farm goods sell for **30–90% more** than supplier goods and display a 🌿 **Fresh badge**, rewarding players who invest in farming. Everything earned in the store funds the farm; everything grown on the farm enriches the store.

📄 **[View the Live GDD on GitHub Pages](https://radhahariharan.github.io/marketland-plus-gdd/)**

---

## 📚 Table of Contents

### 🌐 Core Systems
| # | Document | Description |
|---|----------|-------------|
| 01 | [Game Overview](docs/01-game-overview.md) | Concept, pillars, USPs |
| 02 | [Core Game Loop](docs/02-core-game-loop.md) | Minute / hour / session loops |
| 03 | [Currency System](docs/03-currency-system.md) | Coins, Cash, Farm Tokens, Luxury Points |
| 04 | [Leveling & XP](docs/04-leveling-xp.md) | XP sources, level rewards |
| 05 | [Unified Game World](docs/05-unified-game-world.md) | Farm ↔ Store connection |

### 🌾 Farm
| # | Document | Description |
|---|----------|-------------|
| 06 | [Farm Overview](docs/farm/06-farm-overview.md) | Farm structure, zones |
| 07 | [Crop System](docs/farm/07-crop-system.md) | All 19 crops, growth, wilting |
| 08 | [Animal Husbandry](docs/farm/08-animal-husbandry.md) | All 9 animals, pens, products |
| 09 | [Processing Buildings](docs/farm/09-processing-buildings.md) | All 16 buildings |
| 10 | [Crafting Chains](docs/farm/10-crafting-chains.md) | Multi-step production chains |
| 11 | [Farm Workers](docs/farm/11-farm-workers.md) | 6 worker types, AI tasks |
| 12 | [Seasons & Weather](docs/farm/12-seasons-weather.md) | 4 seasons, 5 weather events |
| 13 | [Farm Mastery](docs/farm/13-farm-mastery.md) | Star system, bonuses |
| 14 | [Farm Expansion](docs/farm/14-farm-expansion.md) | Zones, greenhouse, unlocks |

### 🏪 Store
| # | Document | Description |
|---|----------|-------------|
| 15 | [Store Grid & Layout](docs/store/15-store-grid-layout.md) | Grid, zones, floor types |
| 16 | [Supply Modes](docs/store/16-supply-modes.md) | Supplier / Farm / Hybrid modes |
| 17 | [Displays — All Categories](docs/store/17-displays-all.md) | Every display item |
| 18 | [Coin-Op Items](docs/store/18-coin-op-items.md) | ATM, vending, ticket machines |
| 19 | [Attractions](docs/store/19-attractions.md) | Aquarium, play area, live music |
| 20 | [Decorations](docs/store/20-decorations.md) | Floors, walls, lighting, plants |
| 21 | [Store Expansion](docs/store/21-store-expansion.md) | Zone unlocks, size upgrades |

### ⚙️ Systems
| # | Document | Description |
|---|----------|-------------|
| 22 | [Supply Chain](docs/systems/22-supply-chain.md) | Farm → Store pipeline |
| 23 | [Suppliers & Shipments](docs/systems/23-suppliers-shipments.md) | External suppliers, trucks |
| 24 | [Stockroom](docs/systems/24-stockroom.md) | Storage, capacity, management |
| 25 | [Customer System](docs/systems/25-customer-system.md) | All 12 customer types |
| 26 | [Card System](docs/systems/26-card-system.md) | 4 card types, earning, spending |
| 27 | [Quest System](docs/systems/27-quest-system.md) | Daily, story, farm quests |
| 28 | [Collections](docs/systems/28-collections.md) | 8 collection sets |
| 29 | [Campaigns](docs/systems/29-campaigns.md) | 5 campaign types |
| 30 | [Luxury Points](docs/systems/30-luxury-points.md) | LP accumulation, tiers |
| 31 | [Mastery Stars](docs/systems/31-mastery-stars.md) | Store & farm mastery |
| 32 | [Special Events](docs/systems/32-special-events.md) | Seasonal events, festivals |
| 33 | [Achievements](docs/systems/33-achievements.md) | Full achievement list |
| 34 | [Level Unlock Table](docs/systems/34-level-unlock-table.md) | Complete unlock timeline |
| 35 | [Monetization](docs/systems/35-monetization.md) | Fair monetization principles |
| 36 | [Technical Systems](docs/systems/36-technical-systems.md) | Architecture, data layers |

---

## 🚀 Quick Start

1. **Browse online** → [GitHub Pages GDD](https://radhahariharan.github.io/marketland-plus-gdd/) — each section is its own page.
2. **Browse by topic** → Use the Table of Contents above to jump to any section.
3. **Start here** → Read [01-game-overview.md](docs/01-game-overview.md) then [02-core-game-loop.md](docs/02-core-game-loop.md).
4. **Farm systems** → Explore the [farm/](docs/farm/) folder.
5. **Store systems** → Explore the [store/](docs/store/) folder.
6. **Game mechanics** → Explore the [systems/](docs/systems/) folder.

---

## 📊 Game at a Glance

| Feature | Value |
|---------|-------|
| 🎯 Target Genre | Casual Simulation (Mobile-first) |
| 🔢 Max Levels | 200+ (Prestige beyond 100) |
| 💰 Currencies | 4 (Coins, Cash, Farm Tokens, Luxury Points) |
| 🌾 Crops | 19 (Wheat → Exotic Orchid) |
| 🐄 Animals | 9 (Chicken → Deer) |
| 🏭 Processing Buildings | 16 (Barn → Gourmet Kitchen) |
| 👨‍💼 Customer Types | 12 (Bargain Hunter → Royalty/VIP) |
| 🎴 Card Types | 4 (Shopper, Quick Delivery, Product, Harvest) |
| 🏪 Display Categories | 8 major categories, 70+ displays |
| 📋 Campaign Types | 5 (Flash Sale → VIP Night) |
| 🏆 Collections | 8 curated sets |
| 👷 Farm Workers | 6 specialised AI workers |
| 🌸 Seasons | 4 (Spring, Summer, Autumn, Winter) |
| ⛈️ Weather Events | 5 (Rain, Storm, Heatwave, Fog, Rainbow) |
| ⚡ Energy System | **None — play freely, always** |
| 💎 Paywall | **None — all content reachable through play** |

---

## 🗺️ Repository Layout

```
marketland-plus-gdd/
├── README.md                ← You are here
├── generate_html.py         ← Builds one HTML page per GDD section
├── index.html               ← Navigation hub (GitHub Pages)
├── docs/
│   ├── 01–05 Core systems   (*.md + *.html per section)
│   ├── farm/   06–14        (*.md + *.html per section)
│   ├── store/  15–21        (*.md + *.html per section)
│   └── systems/ 22–36       (*.md + *.html per section)
└── .github/workflows/pages.yml
```

---

*Marketland+ GDD · Version 3.0 · Built for Unity · Mobile-first Casual Simulation*
