# ⚙️ 36 — Technical Systems

This document describes the technical architecture of SuperStoreTycoon, covering the data, logic, and view layers for every major system in the game.

---

## 🏗️ Architecture Overview

SuperStoreTycoon follows an **MVC-inspired layered architecture**:
- **Data Layer** — Plain data classes (serialisable to JSON for save/load)
- **Logic Layer** — Manager classes that own state and enforce rules
- **View Layer** — Unity MonoBehaviour/UI components that display state

All communication between layers uses events and callbacks to maintain separation of concerns.

---

## 📊 Complete System Architecture Table

| System | Data Layer | Logic Layer | View Layer |
|--------|------------|-------------|------------|
| Store Grid | TileData[][] | GridManager | TileView |
| Farm Grid | FarmTileData[][] | FarmGridManager | FarmTileView |
| Store Zones | ZoneData[] | ZoneManager | ZoneView |
| Farm Zones | FarmZoneData[] | FarmZoneManager | FarmZoneView |
| Displays | DisplayData | DisplayManager | DisplayView |
| Crop Plots | CropPlotData[][] | CropManager | CropPlotView |
| Animal Pens | AnimalPenData[] | AnimalManager | AnimalPenView |
| Processing Buildings | BuildingData[] | ProcessingManager | BuildingView |
| Farm Workers | WorkerData[] | WorkerAI | WorkerView |
| Farm-to-Store Supply | FarmSupplyData | SupplyChainManager | SupplyLaneView |
| Farm Stockroom | FarmInventoryData | FarmInventoryManager | FarmInventoryUI |
| Store Stockroom | InventoryData | InventoryManager | InventoryUI |
| Customers | CustomerData | CustomerAI | CustomerView |
| Seasons/Weather | SeasonData | SeasonManager | WeatherView |
| Quests | QuestData[] | QuestManager | QuestPanelUI |
| Currency | WalletData | WalletManager | CurrencyHUD |
| Cards | CardData (4 types) | CardManager | CardHUD |
| Campaigns | CampaignData | CampaignManager | CampaignUI |
| Collections | CollectionData | CollectionManager | CollectionUI |
| Shipments | ShipmentData | ShipmentManager | ShipmentUI |
| Mastery (Store) | MasteryData[] | MasteryManager | MasteryStarUI |
| Mastery (Farm) | FarmMasteryData[] | FarmMasteryManager | FarmMasteryUI |
| Achievements | AchievementData | AchievementManager | AchievementUI |
| Farm Market Stand | MarketListingData[] | MarketManager | FarmMarketUI |
| Save/Load | SaveData (JSON) | SaveManager | LoadingScreen |
| Events | EventData | EventManager | EventBanner |
| Social/Neighbours | NeighbourData[] | SocialManager | NeighbourUI |

---

## 💾 Save System

The save system uses **JSON serialisation** for full cross-platform compatibility:

```
SaveData {
  version: string
  playerId: string
  timestamp: long
  wallet: WalletData
  level: int
  xp: float
  store: StoreData
  farm: FarmData
  quests: QuestSaveData
  achievements: AchievementSaveData
  collections: CollectionSaveData
  cards: CardSaveData
  settings: SettingsData
}
```

### Save Frequency:
- Auto-save: Every 2 minutes while playing
- Auto-save: On every state change (purchase, harvest, etc.)
- Cloud sync: Every 5 minutes (when online)
- Manual save: On app background/close

---

## ⏱️ Timer System

All time-based progression uses **server-side timestamps**:
- Crop timers, processing jobs, and shipments are tracked on the server
- Client side shows calculated remaining time from server timestamp
- **Offline progress** is calculated on next login (farm worked while offline)
- No timer cheating possible via device clock manipulation

---

## 🌿 Fresh Tag Propagation

The Fresh tag is implemented as a metadata flag:

```
ItemData {
  type: ItemType
  quantity: int
  origin: ItemOrigin.FARM | ItemOrigin.SUPPLIER
  freshTag: bool  // true only for FARM-origin
  harvestTime: timestamp
}
```

The fresh tag is preserved through:
- Barn storage (copied to stored item)
- Processing (preserved if any input is FARM-origin)
- Supply lane transfer (tag preserved in transit)
- Display placement (tag displayed as 🌿 badge)

---

## 🤖 Customer AI

Customers use a **simple goal-based AI**:

```
CustomerAI.Update() {
  if (hasTarget && !targetEmpty) → walk to target
  else findBestTarget()
    → filter by budget
    → filter by preference
    → weight by Fresh badge
    → weight by category preference
    → select highest-weighted display
  if (noTarget) → leave store
}
```

Pathfinding uses **A* on the store grid** with aisle width factored into movement cost.

---

## 🔧 Worker AI

Farm workers use a **priority-based task queue**:

```
WorkerAI.Tick() {
  currentTask = taskQueue.peek()
  if (currentTask != null) executeTask(currentTask)
  else {
    tasks = scanForAvailableTasks()
    taskQueue.addRange(prioritySort(tasks))
  }
}
```

Worker priorities are set by:
1. Player-set priority overrides
2. Urgency (wilting crops > ready crops > unwatered crops)
3. Value (high-value crops first)
4. Distance (closest first, unless overridden)

---

## 📱 Performance Targets

| Platform | Target FPS | Max Objects | Memory Budget |
|----------|-----------|-------------|--------------|
| iOS (iPhone 12+) | 60 FPS | 500 active | 512 MB |
| iOS (iPhone 8–11) | 30 FPS | 300 active | 384 MB |
| Android (High) | 60 FPS | 500 active | 512 MB |
| Android (Mid) | 30 FPS | 300 active | 256 MB |
| Android (Low) | 20 FPS | 150 active | 128 MB |

### Performance Optimisations:
- Object pooling for customers, items, and effects
- LOD system for off-screen objects
- Sprite atlasing for all in-game assets
- Background processing on separate threads
- Server-side timer calculations reduce client computation

---

## 🔒 Security

| Concern | Mitigation |
|---------|-----------|
| Timer cheating | Server-side timestamps; client cannot alter timers |
| Currency cheating | Wallet updates server-validated; client is display-only |
| Exploit prevention | All major actions validated server-side before applying |
| Save data integrity | Save file checksummed; tampering detected on load |
| Neighbour fraud | Social gifts server-authenticated per session |

---

← [Previous — Monetization](35-monetization.md) | [Back to README](../../README.md) | *End of GDD*
