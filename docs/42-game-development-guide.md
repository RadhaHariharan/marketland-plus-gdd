# 🌾 HomeGrown — Complete Game Development Guide

> **An advanced, in-depth reference for creating game scenes, menus, entities, mods, and gameplay systems inside the HomeGrown / LowPolyEngine codebase.**

---

## 📋 Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Project Structure](#2-project-structure)
3. [Application Entry Point](#3-application-entry-point)
4. [GameManager — The Central Hub](#4-gamemanager--the-central-hub)
5. [Sessions — Your Game Save Slot](#5-sessions--your-game-save-slot)
6. [Creating a Game Scene](#6-creating-a-game-scene)
7. [The World Grid & Tile System](#7-the-world-grid--tile-system)
8. [Entity System — Blueprints & Components](#8-entity-system--blueprints--components)
9. [All Built-in Components](#9-all-built-in-components)
10. [Creating a Custom Entity (Mod or Built-in)](#10-creating-a-custom-entity-mod-or-built-in)
11. [Items System](#11-items-system)
12. [UI & Menu System](#12-ui--menu-system)
13. [Menus — Main Menu & In-Game UI](#13-menus--main-menu--in-game-ui)
14. [Audio System](#14-audio-system)
15. [Rendering Pipeline](#15-rendering-pipeline)
16. [Camera System](#16-camera-system)
17. [Gameplay Systems](#17-gameplay-systems)
18. [Save System](#18-save-system)
19. [Modding Guide — Complete Reference](#19-modding-guide--complete-reference)
20. [Controls & Input System](#20-controls--input-system)
21. [Particles & Visual Effects](#21-particles--visual-effects)
22. [Terrain Generation](#22-terrain-generation)
23. [Debugging & Configuration](#23-debugging--configuration)
24. [Step-by-Step: Make a Full Game Scene from Scratch](#24-step-by-step-make-a-full-game-scene-from-scratch)

---

## 1. Architecture Overview

HomeGrown is built on the **LowPolyEngine** (a custom OpenGL engine using LWJGL 3). The game is split across three namespaces:

```
thinmatrix.toolbox          → General-purpose utilities (math, file I/O, timing, RNG…)
thinmatrix.lowPolyEngine    → The engine itself (windowing, rendering, audio, UI framework…)
thinmatrix.farmGame         → The actual game logic (entities, scenes, items, gameplay…)
```

### Core Loop

```
FarmGameApp.main()
    └── GameManager.init(configs, mods)       ← one-time setup
    └── while (!readyToClose())
            └── GameManager.update()          ← called every frame
                    ├── SessionManager.updatePublicSession()
                    ├── AmbientSoundPlayer.update()
                    ├── MusicPlayer.update()
                    ├── HomegrownUi.update()
                    └── if (active session)
                            ├── Session.update()
                            │    └── Scene.update()
                            │         ├── SceneSystems (in order)
                            │         └── EntityManager.update()
                            ├── Scene.render()
                            └── AutoSaver.update()
    └── GameManager.cleanUp()
```

---

## 2. Project Structure

```
FarmGame/
├── res/                       ← All game resources (loaded at runtime)
│   ├── entities/              ← Entity blueprint folders (one folder = one entity type)
│   │   ├── Plants/
│   │   │   ├── carrot/
│   │   │   │   ├── EntityInfo_carrot.cba   ← Main blueprint definition
│   │   │   │   ├── carrot1.cba             ← Growth stage 1 model
│   │   │   │   └── carrot2.cba             ← Growth stage 2 model
│   │   │   └── turnip/ …
│   │   ├── Trees/
│   │   ├── Fences/
│   │   └── Misc/
│   ├── items/                 ← Item blueprint folders
│   │   └── Tools/
│   │       ├── fork/
│   │       │   ├── ItemInfo_fork.cba       ← Item definition
│   │       │   └── fork0.cba … fork7.cba   ← Tiered models
│   │       └── shovel/ …
│   ├── sounds/                ← .ogg audio files
│   ├── particleFx/            ← .cba particle effect definitions
│   ├── fonts/                 ← Font files
│   ├── GUIs/                  ← PNG images used in the UI
│   ├── soilTextures/          ← Terrain textures
│   ├── lang/                  ← Localisation files
│   └── cursors/               ← Cursor images
└── src/
    └── thinmatrix/
        ├── farmGame/          ← Game code
        └── lowPolyEngine/     ← Engine code
```

---

## 3. Application Entry Point

**File:** `thinmatrix/farmGame/main/FarmGameApp.java`

This is where everything starts. You will almost never need to modify this file unless you are adding global startup logic.

```java
public class FarmGameApp {
    public static void main(String[] args) {
        // 1. Discover all mods (including the main game mod)
        Mod[] mods = TempModSetup.getAvailableMods();

        // 2. Boot the engine, load all resources, open the window
        GameManager.init(new BuildConfigs(), mods);

        // 3. Optional — set initial volume
        AudioMaster.instance().volumeLevels
            .getVolumeControl(GameVolume.MUSIC_SLIDER).setVolume(0.7f);

        // 4. Main game loop
        while (!GameManager.readyToClose()) {
            GameManager.update();
        }

        // 5. Save everything and close
        GameManager.cleanUp();
    }
}
```

### Key Config Classes

| Class | Purpose |
|---|---|
| `BuildConfigs` | Production settings (version string, no cheats) |
| `DevConfigs` | Developer settings (cheats enabled, faster speed) |
| `GlobalConfigs` | Shared between dev and build configs |
| `GameConfigs` | Interface — your config class must implement this |

To switch to dev mode, change `new BuildConfigs()` → `new DevConfigs()`.

---

## 4. GameManager — The Central Hub

**File:** `thinmatrix/farmGame/main/GameManager.java`

`GameManager` is a static singleton that provides global access to all major systems. You will use it constantly.

### Key Static Fields

| Field | Type | Description |
|---|---|---|
| `configs` | `GameConfigs` | Current game configuration |
| `ambientPlayer` | `AmbientSoundPlayer` | Controls background ambient sounds |
| `musicPlayer` | `MusicPlayer` | Controls background music |
| `gameControls` | `GameControls` | Keyboard/mouse control bindings |
| `DEBUG` | `GameDebug` | Enable/disable debug overlays |

### Key Static Methods

```java
// Get the currently active session (player's farm)
Session session = GameManager.getCurrentSession();

// Get the global entity/item/sound repository
GameRepository repo = GameManager.getRepository();

// Get frame delta time (seconds since last frame, device-independent)
float dt = GameManager.getDelta();

// Get gameplay delta (dt * gameSpeed config multiplier)
float gdt = GameManager.getGameplayDelta();

// Spawn entities at runtime
Blueprint blueprint = GameManager.getRepository().entitySystem.get("carrot");
blueprint.createInstance(scene, new EntityTransform(x, 0, z));
```

### Delta Time — Device Independence

`getDelta()` returns the time (in seconds) since the last frame. **Always multiply movement, growth timers, and animations by delta** to make them frame-rate independent:

```java
// BAD — speed depends on frame rate
position += 5f;

// GOOD — consistent on all devices
position += 5f * GameManager.getDelta();
```

---

## 5. Sessions — Your Game Save Slot

**File:** `thinmatrix/farmGame/main/sessions/Session.java`

A `Session` represents one player's game save (one farm). Multiple sessions can exist (different save files), but only one is **active** at a time.

### Session Contents

```java
public class Session {
    public final PlayerInventory inventory;   // What the player is holding
    public final MoneyCount moneyCount;       // Player's gold/currency
    // scenes are managed internally
}
```

### Switching Between Scenes Within a Session

A session can host multiple scenes (e.g. "Garden Scene" and "Town Scene"). Switching is done via the `SceneSystem`:

```java
// Inside a SceneSystem or gameplay code:
session.switchToScene(townSceneId);  // triggers endActivity() → makeActive()
```

### Creating a New Session

Sessions are created by a `SessionCreator` implementation. The default is `StandardSessionCreator`.

To customise the starting inventory, look at `StartInventoryBuild.java`:
```java
// Give the player starting items
inventory.addItem("hoe", 1);
inventory.addItem("wateringCan", 1);
inventory.addItem("carrotSeed", 10);
```

---

## 6. Creating a Game Scene

A **Scene** is the full 3D world the player sees and interacts with. It contains:
- A **Camera**
- An **Environment** (sun, lighting)
- An **EntityManager** (all living entities)
- A list of **SceneSystems** (terrain, land management, flying items, etc.)

### The Two Built-in Scene Types

| Scene | Creator Class | Description |
|---|---|---|
| Garden Scene | `GardenSceneCreator` | The farm itself — tiles, entities, land plots |
| Town Scene | `TownSceneCreator` | The shop town — fixed viewpoints, NPC entities |

### Step-by-Step: Create a Brand New Scene Type

#### Step 1 — Create the Scene Creator

```java
package thinmatrix.farmGame.scene.prefabs.myScene.creation;

import thinmatrix.farmGame.main.GameManager;
import thinmatrix.farmGame.main.sessions.Session;
import thinmatrix.farmGame.rendering.SceneRenderSystem;
import thinmatrix.farmGame.scene.Scene;
import thinmatrix.farmGame.scene.creation.SceneCreator;
import thinmatrix.lowPolyEngine.engineMain.gameObjects.Environment;
import thinmatrix.lowPolyEngine.engineMain.gameObjects.Light;
import thinmatrix.toolbox.colours.Colour;
import thinmatrix.toolbox.readWrite.Reader;
import org.lwjgl.util.vector.Vector3f;

public class MySceneCreator implements SceneCreator {

    // How far shadows are rendered
    private static final float SHADOW_DISTANCE = 150f;

    // Sun direction (x,y,z) — negative Y = sun above
    private static final Light SUN =
        new Light(new Vector3f(0.4f, -0.8f, -0.6f), new Colour(1f, 0.85f, 0.7f));

    @Override
    public Scene createNew(Session session) {
        // 1. Create a camera
        MySceneCamera camera = new MySceneCamera(Engine.instance().window);

        // 2. Initialise the renderer for this scene
        SceneRenderSystem renderSystem =
            GameManager.getRenderEngine().initSceneRenderSystem(256, SHADOW_DISTANCE);

        // 3. Environment (lighting)
        Environment environment = new Environment(SUN, 0f); // 0f = no fog

        // 4. Create the scene object
        Scene scene = new Scene(session, renderSystem, camera, GameSounds.MY_AMBIENT, environment);

        // 5. Add SceneSystems (order matters — they update in registration order)
        scene.addSystem(new MySandboxGrid(scene, renderSystem));
        scene.addSystem(new MyCustomSystem(scene));

        // 6. (Optional) systems after entity manager update
        scene.switchToAddingAfterEntityManager();
        scene.addSystem(new AnotherSystem());

        return scene;
    }

    @Override
    public Scene load(Session session, Reader reader) throws Exception {
        // Deserialise the scene from a save file
        MySceneCamera camera = MySceneCamera.Serializer.load(reader);
        SceneRenderSystem renderSystem =
            GameManager.getRenderEngine().initSceneRenderSystem(256, SHADOW_DISTANCE);
        Environment environment = new Environment(SUN, 0f);
        Scene scene = new Scene(session, renderSystem, camera, GameSounds.MY_AMBIENT, environment);
        // … load state from reader …
        return scene;
    }
}
```

#### Step 2 — Register Your Scene Creator in SessionCreator

In `StandardSessionCreator` (or your custom `SessionCreator`), tell the session what scenes to create:

```java
public class MySessionCreator implements SessionCreator {
    @Override
    public Session createSession(SessionArgs args) {
        Session session = new Session(/* … */);
        // garden scene
        session.addScene(new GardenSceneCreator().createNew(session));
        // your new scene
        session.addScene(new MySceneCreator().createNew(session));
        return session;
    }
}
```

#### Step 3 — Implement SceneSystem (optional custom systems)

```java
public class MyCustomSystem extends SceneSystem {

    private final Scene scene;

    public MyCustomSystem(Scene scene) {
        super(Id.of("myCustomSystem"));
        this.scene = scene;
    }

    @Override
    public void update() {
        // Called every frame while this scene is active
    }

    @Override
    public void initActiveState() {
        // Called when the player enters this scene
    }

    @Override
    public void endActiveState() {
        // Called when the player leaves this scene
    }

    @Override
    public void cleanUp() { }

    @Override
    public Serializer getSerializer() {
        return writer -> { /* write state to save file */ };
    }
}
```

---

## 7. The World Grid & Tile System

**Files:**
- `thinmatrix/farmGame/scene/sandboxGrid/WorldGrid.java`
- `thinmatrix/farmGame/scene/sandboxGrid/Tile.java`
- `thinmatrix/farmGame/scene/sandboxGrid/TileContents.java`
- `thinmatrix/farmGame/scene/sandboxGrid/SandboxGrid.java`

### Concepts

| Term | Meaning |
|---|---|
| **WorldGrid** | The 2D grid of tiles representing the terrain |
| **Tile** | One grid cell — stores terrain type, entity slots, and tile contents |
| **TileContents** | What is sitting on a tile (entities, decorations) |
| **SandboxGrid** | A `SceneSystem` wrapping the world grid + terrain mesh generator |

### Grid Coordinates

The garden scene uses a 256×256 tile grid (`WORLD_SIZE = 256`).

```java
// Get a tile at grid position (x, z)
Tile tile = worldGrid.getTile(x, z);

// Get the 3D world position of the center of tile (x, z)
// By convention: 1 tile = 1 world unit
float worldX = x + 0.5f;
float worldZ = z + 0.5f;
```

### Terrain Types

Each tile has a terrain type (dirt, grass, path, soil, etc.). Terrain types determine:
- What the tile looks like (texture atlas index)
- Whether crops can be planted
- What entities can be placed

```java
// Change a tile's terrain type
tile.setTerrainType(TerrainType.SOIL);

// Notify the mesh generator to regenerate this chunk
terrainMeshManager.markDirty(x, z);
```

### Iterating Neighbours

```java
// 4-directional neighbours (N, E, S, W)
for (Tile neighbour : new TileNeighbour4Iterable(worldGrid, tile)) {
    // process neighbour
}

// 8-directional neighbours (including diagonals)
for (Tile neighbour : new TileNeighbour8Iterable(worldGrid, tile)) {
    // process neighbour
}
```

### Grid Placement & Blocking

The `TileObjectComponent` is responsible for placing an entity on one or more tiles and marking them as "blocked" (nothing else can be placed there):

```java
// In entity blueprint's EntityInfo.cba:
// tileObject: { width: 1, height: 1, blocking: true }
```

Entities that span multiple tiles (e.g. a 2×2 barn) declare their footprint in the `TileObjectComponent` blueprint.

---

## 8. Entity System — Blueprints & Components

This is the most important system in the game. Everything in the world (plants, trees, fences, machines) is an **Entity** defined by a **Blueprint**.

### Architecture

```
Blueprint  (loaded from disk, shared — acts like a class definition)
    └── ComponentBlueprint[]  (one per component type)
            ↓  createInstance()
Entity  (live in the scene, unique — acts like an object instance)
    └── Component[]  (actual runtime state)
```

### Entity Blueprint Folder Structure

Each entity type is a folder inside `res/entities/`. The engine detects entity folders by the presence of a file named `EntityInfo_<name>.cba`.

```
res/entities/Plants/carrot/
    EntityInfo_carrot.cba    ← Required. Defines all components.
    carrot1.cba              ← 3D model (growth stage 1)
    carrot2.cba              ← 3D model (growth stage 2)
    carrotSeed.cba           ← Seed model
```

### EntityInfo CBA Format

The `.cba` file format is the game's custom binary/tag format. Here is what an `EntityInfo` typically contains (conceptually):

```
entity {
    savingEnabled: true

    tileObject {
        width: 1
        height: 1
        blocking: true
    }

    render {
        part "main" {
            mesh: "carrot1.cba"
        }
    }

    growth {
        stages: 2
        stageDuration: 120.0   # seconds per stage
        meshes: ["carrot1.cba", "carrot2.cba"]
    }

    harvestable {
        item: "carrot"
        minAmount: 1
        maxAmount: 3
    }

    seed {
        seedModel: "carrotSeed.cba"
    }

    health {
        factors: [WATER, SOIL_QUALITY]
    }
}
```

### How the Engine Loads Entities

```
GameRepository.loadGameResources()
    └── EntitySystem.loadEntities()
            └── BlueprintRepositoryLoader.loadEntityFolder()
                    └── For each sub-folder that is an entity folder:
                            └── BlueprintLoader.loadBlueprint()  ← reads EntityInfo_*.cba
```

---

## 9. All Built-in Components

These are the component types defined in `GameComp.java`. Each entity can have any combination of them.

| Component | Purpose |
|---|---|
| **TileObjectComponent** | Places the entity on tiles, handles blocking |
| **RenderComponent** | Defines the 3D meshes to draw |
| **GrowthComponent** | Multi-stage growth over time |
| **HarvestableComponent** | Entity produces items when interacted with |
| **SeedComponent** | Entity spawns from a seed item |
| **HealthComponent** | Entity has health affected by environment factors |
| **AgeComponent** | Entity tracks age in game-time |
| **FruiterComponent** | Cyclic fruit production (like apple trees) |
| **ConnectorComponent** | Entity changes shape based on neighbours (fences) |
| **ClimberComponent** | Entity climbs support poles (beans, tomatoes) |
| **SupportPoleComponent** | Provides a pole for climbers |
| **StorageComponent** | Entity stores items (chest, crate) |
| **ShopComponent** | Entity opens a shop UI when clicked |
| **InfoComponent** | Entity shows an info panel when examined |
| **DecoComponent** | Pure decoration, no interaction |
| **ParticleComponent** | Entity emits particle effects |
| **SounderComponent** | Entity plays sounds at its location |
| **PreviewComponent** | Entity has a placement preview ghost |
| **TieredModelComponent** | Entity model changes based on tier/level |
| **OnClickComponent** | Custom click interaction |
| **PlasticMeltComponent** | Plastic melter machine logic |

### Component Blueprint Parameters (CBA tags)

Each component blueprint reads its configuration from the EntityInfo CBA file using tag-based reading:

```java
// GrowthCompBlueprint reads:
//   - stageDuration  (float)
//   - stageCount     (int)
//   - meshNames      (string array)
```

---

## 10. Creating a Custom Entity (Mod or Built-in)

### Step 1 — Create the Entity Folder

```
res/entities/MyCategory/myPlant/
    EntityInfo_myPlant.cba
    myPlant_stage1.cba
    myPlant_stage2.cba
```

### Step 2 — Write the 3D Models

Export your models as `.cba` (SmoothPoly format). The engine reads:
- `.cba` files exported by the `SmoothPolyCbaExporter`
- Vertex positions, normals, UVs, and palette material data

To convert from OBJ: Use `SmoothPolyObjImporter` → `SmoothPolyCbaExporter` toolchain.

### Step 3 — Write EntityInfo_myPlant.cba

Create the blueprint definition file declaring every component your entity needs.

### Step 4 — If adding to the main game

The entity will be auto-discovered by `BlueprintRepositoryLoader` scanning `res/entities/` recursively. No code registration required.

### Step 5 — Spawn the entity at runtime

```java
// Get the blueprint
Blueprint blueprint = GameManager.getRepository().entitySystem.get("myPlant");

// Spawn at a tile position (tile 50, 70)
EntityTransform transform = new EntityTransform(50.5f, 0f, 70.5f, 0f, 1f);
blueprint.createInstance(scene, transform, TileObjectParams.auto());
```

### Step 6 — Custom Component (Advanced)

If your entity needs brand-new behaviour, create a custom component:

```java
// 1. Define the type enum value
public enum MyGameComp implements ComponentType {
    MY_COMPONENT;
    // implement required methods
}

// 2. Create the blueprint (loaded from CBA)
public class MyCompBlueprint implements ComponentBlueprint<MyComponent> {
    private final float myParam;

    public MyCompBlueprint(float myParam) {
        this.myParam = myParam;
    }

    @Override
    public MyComponent createInstance(Entity entity, ComponentBundle bundle) {
        return new MyComponent(entity, myParam);
    }
}

// 3. Create the runtime component
public class MyComponent implements Component {
    private final Entity entity;
    private float timer;
    private final float duration;

    public MyComponent(Entity entity, float duration) {
        this.entity = entity;
        this.duration = duration;
    }

    @Override
    public void update() {
        timer += GameManager.getDelta();
        if (timer >= duration) {
            // do something
            timer = 0;
        }
    }

    @Override
    public ComponentType getType() {
        return MyGameComp.MY_COMPONENT;
    }
}

// 4. Create the loader (reads CBA tags)
public class MyCompLoader implements RegistrableCbaLoader<ComponentBlueprint> {
    @Override
    public ComponentBlueprint load(CbaObjectReader reader) throws Exception {
        float duration = reader.readFloat("duration");
        return new MyCompBlueprint(duration);
    }
}
```

---

## 11. Items System

Items are things that can be in the player's **inventory** and **hotbar**. Seeds, tools, harvested crops — all items.

### Item Folder Structure

```
res/items/Tools/fork/
    ItemInfo_fork.cba   ← Main item definition
    fork0.cba           ← Tier 0 model (held in hand)
    fork7.cba           ← Tier 7 model (max tier)
```

### Item Definition (CBA)

```
item {
    name: "fork"
    maxStack: 1
    tier: 0

    toolComp {
        toolType: HOE
        useSound: "digging"
    }

    render {
        mesh: "fork0.cba"
    }
}
```

### Item Tiers

Many tools (fork, hoe, shovel, watering can) have tiers 0–7 (`fork0.cba` through `fork7.cba`). Upgrading in the shop advances the tier and swaps the mesh.

### Registering Item Loaders

Item components (like `toolComp`) need a registered loader. In your `Mod`:

```java
@Override
public void registerItemCompLoaders(HashRegistry<ItemCompLoader> registry) {
    registry.register(new MyItemCompLoader());
    // The main game already registers all built-in item comp loaders
    // via GameItemComps.registerLoaders(registry)
}
```

---

## 12. UI & Menu System

The UI system is built into the LowPolyEngine using a constraint-based layout (similar to Android `ConstraintLayout`).

### Key Classes

| Class | Description |
|---|---|
| `Ui` | Static access point — `Ui.getContainer()` is the root |
| `UiBlock` | A rectangular UI panel (background, image, etc.) |
| `UiText` | Renders text |
| `UiButton` | Clickable button with hover and press states |
| `ConstraintUtils` | Helper for positioning (fill, center, align edges…) |
| `HomegrownUiStyle` | The game's style sheet (colours, fonts, sizes) |

### Adding a UI Element

```java
// Create a panel
UiBlock panel = new UiBlock(Colour.WHITE);
panel.setLevel(2);   // higher = drawn on top

// Add it to the container with constraints
Ui.getContainer().add(panel, ConstraintUtils.center(200, 100));
// or
Ui.getContainer().add(panel, ConstraintUtils.fill());  // full screen

// Show/hide with optional transition
panel.displayer.setTransition(Transitions.fade(0.4f));
panel.setDisplayed(true);
panel.setDisplayed(false);
```

### Creating a Button

```java
UiButton myButton = new UiButton(style.buttonStyle());
myButton.setText("Click Me");
myButton.setOnClick(() -> {
    // do something
});
Ui.getContainer().add(myButton, ConstraintUtils.below(otherElement, 10));
```

### UI Layers (Levels)

UI elements draw in ascending level order. Typical conventions:

| Level | Usage |
|---|---|
| 0 | Background panels |
| 1 | Main game UI (hotbar, HUD) |
| 2 | Pop-up panels (inventory, shop) |
| 3 | Dialogue boxes |
| 4 | Full-screen overlays (white flash on scene transition) |

---

## 13. Menus — Main Menu & In-Game UI

### Main Menu

**File:** `thinmatrix/farmGame/ui/gameMenu/GameMenuUi.java`

The main menu is created by `HomegrownUi.initGameMenu()` after loading is complete.

Structure:
```
GameMenuUi
    ├── New Game button → SessionManager.createNewSession()
    ├── Load Game button → SessionManager.loadSession(saveFile)
    └── Quit button → Engine.instance().requestClose()
```

To **add a new button to the main menu**, extend `GameMenuUi` or modify it directly:

```java
UiButton myButton = new UiButton(style.buttonStyle());
myButton.setText("My Feature");
myButton.setOnClick(() -> { /* open my feature screen */ });
this.add(myButton, ConstraintUtils.below(lastButton, 8));
```

### In-Game UI (HUD)

**File:** `thinmatrix/farmGame/ui/GameUi.java`

The `GameUi` is the HUD displayed while a session is active:
- Hotbar (tool slots)
- Money counter
- Time display
- Tool tooltips
- Examine panel (click on entity → info panel)

### Examine / Info Panels

When a player clicks an entity with the `InfoComponent`, an info panel is shown. You can provide custom panel content by implementing `InfoPanelProvider`:

```java
public class MyInfoPanelProvider implements InfoPanelProvider {
    @Override
    public UiBlock createPanel(Entity entity, HomegrownUiStyle style) {
        UiBlock panel = new UiBlock(style.panelColour());
        UiText label = new UiText("My Entity Info", style.bodyFont());
        panel.add(label, ConstraintUtils.center());
        return panel;
    }
}
```

### Scene Transition (White Flash)

When switching between scenes, the engine fades to white and back:

```java
// Internally done by HomegrownUi:
whiteScreen.setDisplayed(true);   // fade to white
// ... after transition ...
whiteScreen.setDisplayed(false);  // fade back
```

The `sceneSwitchAudioFader` also ducks audio during this transition.

---

## 14. Audio System

### Playing Sounds on an Entity

Use `SounderComponent`. Declare it in the EntityInfo CBA:
```
sounder {
    sound: "mySound.ogg"
    radius: 10.0
    volume: 1.0
    loop: false
}
```

### Ambient Sounds

```java
// In your SceneCreator, pass an ambient sound to the Scene constructor:
AmbientSound ambient = GameSounds.GARDEN_AMBIENT;
Scene scene = new Scene(session, renderSystem, camera, ambient, environment);

// The scene's makeActive() automatically starts playing it:
GameManager.ambientPlayer.playSound(sceneAmbientSound);
```

### Background Music

```java
// Music is controlled through:
GameManager.musicPlayer.playTrack("myTrack.ogg");

// Volume is controlled via:
AudioMaster.instance().volumeLevels
    .getVolumeControl(GameVolume.MUSIC_SLIDER)
    .setVolume(0.7f);
```

### 3D Positional Audio

The listener position (the "ears") is tied to the camera:
```java
AudioMaster.instance().listenerManager.setListener(camera);
```

Any sound node placed at a world position will attenuate based on distance to the camera.

---

## 15. Rendering Pipeline

The game uses a custom multi-pass OpenGL renderer.

```
Scene.render()
    └── SceneRenderSystem.render(scene)
            ├── Shadow Pass     (depth map from sun's perspective)
            ├── Geometry Pass   (all 3D objects, entities, terrain)
            ├── Post-Processing (optional — bloom, colour grading)
            └── UI Pass         (2D UI elements on top)
```

### Render Component

Every visible entity needs a `RenderComponent` with one or more `RenderablePart`s. Each part references a mesh (`.cba` file) and a material.

### Mesh Atlas

For performance, all entity meshes are packed into a **Mesh Atlas** — a single large VBO shared across all entities. The engine logs this:
```
Updated mesh atlas size to 1,464 vertices and 5,562 indices.
```

This means draw calls are batched by material, greatly reducing GPU overhead.

### Shadow Distance

Set in your `SceneCreator`:
```java
// Larger = more shadow coverage but more GPU cost
private static final float SHADOW_DISTANCE = 200f;
```

---

## 16. Camera System

### Garden Scene Camera (StandardCamera)

The farm view uses an isometric-style camera that pans, zooms, and rotates:

```
CameraConfigs
    ├── minZoom, maxZoom
    ├── panSpeed
    ├── rotationSpeed
    └── clampBounds (CameraClamp)
```

Camera movement is bound to `CameraControls` (WASD or arrow keys, scroll to zoom, middle mouse to rotate).

### Town Scene Camera (TownCamera)

The town uses fixed **ViewPoints** — discrete camera positions the player snaps between:

```java
public class TownViewPoints {
    public static final ViewPoint SHOP = new ViewPoint(
        new Vector3f(50f, 20f, 80f),   // position
        new Vector3f(0f, 1f, 0f),       // look-at target
        60f                              // FOV
    );
}
```

Transitioning between viewpoints uses `SmoothCameraMover` (lerps position and orientation over time).

### Creating a Custom Camera

Extend `GameCamera` and implement:
```java
public class MyCamera extends GameCamera {
    @Override
    public void update() {
        // update position/rotation based on input
    }

    @Override
    public Matrix4f getViewMatrix() {
        // return the view matrix
    }
}
```

---

## 17. Gameplay Systems

### Land Management (Farm Plots)

**File:** `thinmatrix/farmGame/gameplay/landManagement/LandManager.java`

The player starts with two unlocked plots (`STARTING_PLOTS`). Additional plots must be purchased. Each plot is a rectangular area of tiles the player can develop.

```java
// In GardenSceneCreator:
public static final Coords[] STARTING_PLOTS = {
    new Coords(5, 9),
    new Coords(4, 9)
};
LandManager landManager = LandManagerCreator.init(scene, worldGrid, STARTING_PLOTS);
```

### Flying Items (Item Pickup Animations)

**File:** `thinmatrix/farmGame/gameplay/flyingItems/FlyingItemManager.java`

When an entity is harvested, items "fly" from the entity to the inventory UI. This is a `SceneSystem` that manages these animated arcs.

```java
// Spawn a flying item from world position to inventory
FlyingItemManager.instance().spawnFlyer(itemId, worldPos);
```

### Automation Machines

**File:** `thinmatrix/farmGame/gameplay/automation/machines/groups/MachineGroupManager.java`

Machines (auto-planter, auto-harvester, sprinkler) are grouped into machine groups that manage their shared behaviour. This is added to every garden scene:

```java
scene.addSystem(new MachineGroupManager());
```

### Shop System

**Files:** `thinmatrix/farmGame/gameplay/shops/`

Shops are registered in `MainGameMod.createEmptyShops()`. Each shop is a `ShopBlueprint` with:
- A list of items for sale (with prices)
- Lock conditions (e.g. "unlock after selling 50 carrots")

```java
@Override
public void createEmptyShops(HashRegistry<ShopBlueprint> shopRegistry) {
    GameShops.registerGameShops(shopRegistry);
    ShopInfoLoader.LOCK_CONTROL_LOADERS.register(new AmountSoldLockLoader());
}
```

### Time System

Game time runs through `GameManager.getGameplayDelta()`, which is `frameDelta × gameSpeed`. You can pause or speed up game time by modifying `configs.gameSpeed`.

The town scene has a `TimePauser` that stops game time while the player is in town.

---

## 18. Save System

**Files:** `thinmatrix/lowPolyEngine/resourceManagement/saveSystem/`

Saves are stored in `FarmGame/saves/` as `.dat` binary files.

```
saves/
    6506_SAVE_2026-03-18_17-35-59_My_First_Farm.dat
```

### How Saving Works

Every major object implements `Exportable` (which provides a `Serializer`) and `StateSerializer` (which has a `loadState(Reader)` method).

The save order **must match** the load order exactly:

```java
// Saving (in SceneSerializer):
writer.writeObject(camera);
writer.writeObject(worldGrid);
writer.writeObject(entityManager);
writer.writeObject(landManager);

// Loading (in SceneCreator.load()):
StandardCamera camera = CameraSerializer.load(reader);
worldGrid.getSerializer().loadState(reader);
scene.entityManager.getSerializer().loadEntities(scene, reader);
LandManager landManager = LandManagerCreator.load(scene, worldGrid, reader);
```

### Auto-Save

`AutoSaver` triggers a save every N minutes. Configure in `GameConfigs`:
```java
autoSaveEnabled = true;
autoSaveIntervalMinutes = 5;
```

### Save Versioning

When the save format changes between game versions, increment `SAVE_VERSION` in `GameManager`:
```java
private static final int SAVE_VERSION = 2;  // was 1
```

Mismatched versions show the player an error rather than corrupting the save.

---

## 19. Modding Guide — Complete Reference

The game is designed to be extended through **Mods**. A Mod is a Java class + a resource folder.

### What a Mod Can Do

| Feature | How |
|---|---|
| Add new entities | Drop folders in `mods/<modId>/entities/` |
| Add new items | Drop folders in `mods/<modId>/items/` |
| Register item component loaders | Override `registerItemCompLoaders()` |
| Add new entity component types | Override `getEntityComponentTypes()` |
| Create new shops | Override `createEmptyShops()` |
| Add sounds/textures | Drop files in mod's `res/` folder |

### Step-by-Step: Create a Mod

#### 1. Create the Mod Class

```java
package com.example.mymod;

import thinmatrix.farmGame.main.modSupport.Mod;
import thinmatrix.farmGame.entities.architecture.ComponentType;
import thinmatrix.farmGame.items.loading.ItemCompLoader;
import thinmatrix.farmGame.gameplay.shops.ShopBlueprint;
import thinmatrix.toolbox.hashIds.HashRegistry;
import java.io.File;

public class MyMod extends Mod {

    public MyMod() {
        super("mymod", new File("mods/mymod"));
    }

    /**
     * Register any custom item component loaders your mod adds.
     * The loader ID must match the tag name used in your ItemInfo CBA files.
     */
    @Override
    public void registerItemCompLoaders(HashRegistry<ItemCompLoader> registry) {
        registry.register(new MySpecialItemCompLoader());
    }

    /**
     * Register any custom entity component types your mod adds.
     * These are enum values implementing ComponentType.
     */
    @Override
    public ComponentType[] getEntityComponentTypes() {
        return MyModComponents.values();
    }

    /**
     * Create empty shop blueprints. Don't add items here — they aren't loaded yet.
     * Items are added to the shop during the item-loading phase.
     */
    @Override
    public void createEmptyShops(HashRegistry<ShopBlueprint> shopRegistry) {
        shopRegistry.register(new ShopBlueprint(Id.of("mymod", "myShop")));
    }
}
```

#### 2. Create the Mod Folder Structure

```
mods/mymod/
    entities/
        MyPlants/
            mySpecialPlant/
                EntityInfo_mySpecialPlant.cba
                stage1.cba
                stage2.cba
    items/
        MyItems/
            mySpecialSeed/
                ItemInfo_mySpecialSeed.cba
                seed.cba
    sounds/
        myAmbient.ogg
    particleFx/
        myEffect.cba
```

#### 3. Register the Mod at Startup

In `TempModSetup.getAvailableMods()` (or your own setup class):

```java
public static Mod[] getAvailableMods() {
    return new Mod[] {
        new MainGameMod(),      // Always first!
        new MyMod(),            // Your mod
    };
}
```

#### 4. Namespace Convention

All IDs in your mod should use your mod's namespace to avoid conflicts:

```
Entity IDs:    "mymod:mySpecialPlant"
Item IDs:      "mymod:mySpecialSeed"
Shop IDs:      "mymod:myShop"
Sound IDs:     "mymod:myAmbient"
```

In CBA files, use `namespace:name`. In code:
```java
Id.of("mymod", "mySpecialPlant")
```

The `DEFAULT_NAMESPACE` (for the base game) is `"homegrown"`.

#### 5. Entity Component Types in Your Mod

```java
public enum MyModComponents implements ComponentType {

    MY_SPECIAL_COMP {
        @Override
        public String getTagName() { return "mySpecialComp"; }

        @Override
        public ComponentBlueprint loadBlueprint(CbaObjectReader reader) throws Exception {
            return new MySpecialCompLoader().load(reader);
        }
    };
}
```

#### 6. Item Components in Your Mod

```java
public class MySpecialItemComp implements ItemComp {
    // your item behaviour
}

public class MySpecialItemCompLoader implements ItemCompLoader {
    @Override
    public String getTagName() { return "mySpecialItemComp"; }

    @Override
    public ItemComp load(CbaObjectReader reader) throws Exception {
        float power = reader.readFloat("power");
        return new MySpecialItemComp(power);
    }
}
```

### Mod Loading Order

Resources are loaded in mod order. If two mods define the same ID, the **last one wins**. To override a base-game entity, create a mod with the same entity folder name and the correct namespace.

---

## 20. Controls & Input System

**File:** `thinmatrix/farmGame/main/gameControls/GameControls.java`

Controls are grouped into logical sets:

| Class | Controls |
|---|---|
| `CameraControls` | Pan, zoom, rotate camera |
| `BasicToolControls` | Use tool, cancel, cycle hotbar |
| `HotbarControls` | Number keys for hotbar slots |
| `DialogueControls` | Advance dialogue, close |
| `MiscControls` | Fullscreen toggle, cash-in cheat, plant spawn |
| `TownCamKeyboardControls` | Keyboard navigation in town scene |

### Reading Input

```java
// Is a key currently held down?
boolean held = Engine.instance().keyboard.isKeyDown(GLFW.GLFW_KEY_W);

// Was a key just pressed this frame?
boolean pressed = Engine.instance().keyboard.keyPressEvent(GLFW.GLFW_KEY_SPACE);

// Mouse button
boolean leftClick = Engine.instance().mouse.isButtonDown(GLFW.GLFW_MOUSE_BUTTON_LEFT);
boolean leftPressed = Engine.instance().mouse.buttonPressEvent(GLFW.GLFW_MOUSE_BUTTON_LEFT);

// Mouse position (screen pixels)
float mouseX = Engine.instance().mouse.getX();
float mouseY = Engine.instance().mouse.getY();
```

### Defining a New Control

```java
public class MyControls {
    private final Control myAction;

    public MyControls(Keyboard keyboard) {
        myAction = new Control(keyboard, GLFW.GLFW_KEY_F);
    }

    public boolean isMyAction() {
        return myAction.isPressed();
    }
}
```

Add your controls class to `GameControls`:
```java
public final MyControls myControls;

public GameControls(Mouse mouse, Keyboard keyboard, StateManager stateManager) {
    // ... existing ...
    this.myControls = new MyControls(keyboard);
}
```

---

## 21. Particles & Visual Effects

**File:** `thinmatrix/lowPolyEngine/particles/ParticleMaster.java`

Particle effects are defined as `.cba` files in `res/particleFx/`.

### Playing a Particle Effect

```java
// Get a global effect by name
ParticleEffect effect = ParticleMaster.instance().getGlobalEffect("myEffect.cba");

// Update it each frame at a world transform
effect.update(new Transform(worldX, worldY, worldZ));

// Create a variant with a position offset
ParticleEffect variant = effect.createVariant(
    new Vec3Param("offset", new Vector3f(0f, 1.5f, 0f))
);
```

### Entity Particle Component

Use `ParticleComponent` in EntityInfo CBA:
```
particle {
    effect: "leafFall.cba"
    offsetY: 2.0
}
```

---

## 22. Terrain Generation

**Files:**
- `thinmatrix/farmGame/scene/sandboxGrid/TerrainGeneratorCreator.java`
- `thinmatrix/farmGame/terrain/meshGeneration/TerrainMeshGenerator.java`

The terrain mesh is generated procedurally from the `WorldGrid`. Each chunk of tiles is meshed together using the soil textures from `res/soilTextures/`.

### Initial Generation

```java
// Called once when creating a new game:
populator.generateTerrainTiles(sandboxGrid.worldGrid);
sandboxGrid.terrainMeshManager.doInitialFullGridGeneration();
```

### ScenePopulator

The `ScenePopulator` interface allows you to customise what's on the map when a new game starts:

```java
public interface ScenePopulator {
    void generateTerrainTiles(WorldGrid worldGrid);
    void generateNewSessionScenery(Scene scene, WorldGrid worldGrid);
}
```

Default implementation is `EmptyScenePopulator` (flat grass).

Custom implementation example:
```java
public class MyScenePopulator implements ScenePopulator {
    @Override
    public void generateTerrainTiles(WorldGrid worldGrid) {
        // Set all tiles to grass
        for (int x = 0; x < worldGrid.getSize(); x++) {
            for (int z = 0; z < worldGrid.getSize(); z++) {
                worldGrid.getTile(x, z).setTerrainType(TerrainType.GRASS);
            }
        }
        // Add a path down the middle
        for (int z = 0; z < worldGrid.getSize(); z++) {
            worldGrid.getTile(worldGrid.getSize()/2, z)
                     .setTerrainType(TerrainType.PATH);
        }
    }

    @Override
    public void generateNewSessionScenery(Scene scene, WorldGrid worldGrid) {
        // Spawn some decorative trees
        Blueprint tree = GameManager.getRepository().entitySystem.get("tree");
        for (int i = 0; i < 10; i++) {
            int x = 10 + i * 20;
            int z = 5;
            tree.createInstance(scene,
                new EntityTransform(x + 0.5f, 0, z + 0.5f, 0, 1),
                TileObjectParams.auto());
        }
    }
}
```

---

## 23. Debugging & Configuration

### GameDebug

**File:** `thinmatrix/farmGame/main/GameDebug.java`

```java
// Enable various debug overlays at startup:
GameManager.DEBUG.showEntityBounds = true;
GameManager.DEBUG.showTileGrid = true;
GameManager.DEBUG.logFrameTime = true;
```

### DevConfigs

Use `new DevConfigs()` instead of `new BuildConfigs()` to enable:
- Cheat keys (Alt+N to spawn items)
- Faster time progression
- Dev-only debug UI

### Error Logs

Errors are written to `FarmGame/ErrorLogsTM/`. Each file is timestamped and contains the full stack trace. The `DefaultErrorLogs/` folder (in the project root) catches errors that occur before the game folder is found.

### Common Errors

| Error | Cause | Fix |
|---|---|---|
| `NullPointerException in BlueprintRepositoryLoader.isEntityFolder` | Entity folder has a null file listing (permissions issue or missing folder) | Ensure `res/entities/` exists and is readable |
| `GLFW_FEATURE_UNAVAILABLE: Cocoa: Regular windows do not have icons` | macOS doesn't support window icons — harmless | Wrap `glfwSetWindowIcon` in an OS check |
| `unit 1 GLD_TEXTURE_INDEX_2D is unloadable` | OpenGL texture unit issue on some macOS drivers — harmless warning | No fix needed |

---

## 24. Step-by-Step: Make a Full Game Scene from Scratch

Here is a complete walkthrough to add a brand-new scene (e.g. a "Cave Scene") to the game.

### Phase 1 — Resources

```
res/entities/CaveEntities/
    crystalFormation/
        EntityInfo_crystalFormation.cba
        crystal_small.cba
        crystal_large.cba
    stalagmite/
        EntityInfo_stalagmite.cba
        stalagmite.cba
```

### Phase 2 — Scene Creator

```java
// thinmatrix/farmGame/scene/prefabs/caveScene/creation/CaveSceneCreator.java
public class CaveSceneCreator implements SceneCreator {

    private static final int CAVE_SIZE = 128;
    private static final float SHADOW_DISTANCE = 80f;
    private static final Light AMBIENT_LIGHT =
        new Light(new Vector3f(0f, -1f, 0f), new Colour(0.2f, 0.2f, 0.4f));

    @Override
    public Scene createNew(Session session) {
        CaveCamera camera = new CaveCamera(Engine.instance().window);
        SceneRenderSystem renderSystem =
            GameManager.getRenderEngine().initSceneRenderSystem(CAVE_SIZE, SHADOW_DISTANCE);
        Environment environment = new Environment(AMBIENT_LIGHT, 0.05f); // slight fog

        Scene scene = new Scene(session, renderSystem, camera,
                                GameSounds.CAVE_AMBIENT, environment);

        WorldGrid worldGrid = new WorldGrid(scene, CAVE_SIZE);
        TerrainMeshGenerator terrainMesh =
            TerrainGeneratorCreator.create(worldGrid, renderSystem);
        SandboxGrid sandboxGrid = new SandboxGrid(worldGrid, terrainMesh);

        scene.addSystem(sandboxGrid);
        scene.addSystem(new EntityEffectManager());

        // Populate the cave with crystals
        new CavePopulator().generateTerrainTiles(worldGrid);
        new CavePopulator().generateNewSessionScenery(scene, worldGrid);
        terrainMesh.doInitialFullGridGeneration();

        return scene;
    }

    @Override
    public Scene load(Session session, Reader reader) throws Exception {
        // Load from save file
        CaveCamera camera = CaveCamera.Serializer.load(reader);
        // ... rest of load logic
    }
}
```

### Phase 3 — Cave Populator

```java
public class CavePopulator implements ScenePopulator {

    @Override
    public void generateTerrainTiles(WorldGrid worldGrid) {
        int size = worldGrid.getSize();
        for (int x = 0; x < size; x++) {
            for (int z = 0; z < size; z++) {
                worldGrid.getTile(x, z).setTerrainType(TerrainType.STONE);
            }
        }
    }

    @Override
    public void generateNewSessionScenery(Scene scene, WorldGrid worldGrid) {
        Blueprint crystal = GameManager.getRepository().entitySystem.get("crystalFormation");
        RandomGenerator rng = new RandomGenerator(12345L);
        for (int i = 0; i < 30; i++) {
            int x = rng.nextInt(5, worldGrid.getSize() - 5);
            int z = rng.nextInt(5, worldGrid.getSize() - 5);
            crystal.createInstance(scene,
                new EntityTransform(x + 0.5f, 0f, z + 0.5f, rng.nextFloat()*360f, 1f),
                TileObjectParams.auto());
        }
    }
}
```

### Phase 4 — Add Scene to Session

```java
// In your SessionCreator:
@Override
public Scene createScenes(Session session) {
    // Garden scene (first = starting scene)
    session.addScene(new GardenSceneCreator().createNew(session));
    // Cave scene
    session.addScene(new CaveSceneCreator().createNew(session));
    return session;
}
```

### Phase 5 — Add a Button to Travel to Cave

```java
// In your game UI, add a "Go to Cave" button:
UiButton caveButton = new UiButton(style.buttonStyle());
caveButton.setText("Enter Cave");
caveButton.setOnClick(() -> {
    Session s = GameManager.getCurrentSession();
    s.switchToScene(Id.of("caveScene"));
});
Ui.getContainer().add(caveButton, ConstraintUtils.alignRight(hotbar, 8));
```

### Phase 6 — Add a Cave Ambient Sound

In `GameSounds.java`:
```java
public static final AmbientSound CAVE_AMBIENT =
    new AmbientSound("sounds/cave_drips.ogg", 0.6f, true);
```

### Phase 7 — Test

1. Run `FarmGameApp.main()`
2. Create a new game
3. Press your "Enter Cave" button
4. The scene transitions to the cave with crystals and dripping sounds

---

## Quick Reference Card

```
New Entity     → res/entities/<Category>/<name>/EntityInfo_<name>.cba + models
New Item       → res/items/<Category>/<name>/ItemInfo_<name>.cba + models
New Scene      → Implement SceneCreator, add to SessionCreator
New SceneSystem → Extend SceneSystem, scene.addSystem()
New Component  → Implement ComponentType, ComponentBlueprint, Component
New Mod        → Extend Mod, add to TempModSetup.getAvailableMods()
New UI Panel   → new UiBlock(), add to Ui.getContainer() with ConstraintUtils
New Shop       → ShopBlueprint in Mod.createEmptyShops()
New Sound      → .ogg in res/sounds/, reference by filename
New Particle   → .cba in res/particleFx/, ParticleMaster.instance().getGlobalEffect()
Delta Time     → Always multiply movement by GameManager.getDelta()
Spawn Entity   → GameManager.getRepository().entitySystem.get("id").createInstance(scene, transform)
Spawn Item     → GameUtils.spawnItem("itemId", count)
Get Money      → GameManager.getCurrentSession().moneyCount
```

---

*This guide was generated from the full source code of HomeGrown. Last updated: April 2026.*

