# Toolbox — Complete In-Depth Reference
> **207 source files · 26 top-level packages · Every class documented**

---

## Package map

```
toolbox/
├── math3d/          — Maths, easing, vectors, waves, bounding volumes, directions
├── rng/             — Deterministic noise, Perlin noise, rich random generator
├── valueDrivers/    — Time-based animated float value system
├── hashIds/         — Typed ID + registry system (used by the whole entity system)
├── errors/          — Crash handler, pop-up, ProgramError
├── listeners/       — Safe observer pattern with concurrent-removal support
├── fileUtils/       — File I/O helpers, classpath-resource wrapper, root finder
├── byteWork/        — GPU-ready byte packing and buffer building
├── inputs/          — Developer console keyboard reader (dev tool only)
├── colours/         — Colour, HSV, gradients, palettes, colour repository
├── dataStructures/  — Bundle, SafeList, EasyArray, Registry, Tuple
├── fileWatcher/     — OS-level file change watcher for hot-reload
├── gameRegistry/    — Forward-reference (lazy) registry with Reference<T>
├── images/          — ImageData (AWT) and RawByteImage (STB) loaders
├── memory/          — GPU VAO memory slot allocator (MemorySlotChain)
├── misc/            — AsciiValues constants, generic Listener/ListenerSet
├── modifiers/       — Multiplier stack for moddable float values
├── objectPools/     — Thread-safe object pools for Vec2/3/4 reuse
├── readWrite/       — Serialization interfaces + CSV / CBA / tag binary format implementations
├── smoothValues/    — Exponential-smoothing wrappers for float, angle, colour, Vec2, Vec3
├── timing/          — Timer hierarchy: single, looping, random-looping, countdown, nano
├── mesh3d/          — Indexed mesh primitives (IndexedMesh, Mesh3d, Corner)
├── meshBuilding/    — Vertex → packed byte[] pipeline for GPU upload
├── meshGeneration/  — High-level shape generators (curves, road cross-sections, fills)
├── modelFormats/    — 3D model I/O: OBJ, streamline CSV, textured OBJ, SmoothPoly CBA
└── version/         — Version value object with save/load serializer
```

---

## 1 · `math3d` — The Math Foundation

### `Maths.java` (827 lines — the biggest utility class)

The central static math class. Everything uses it.

**Categories inside:**

| Category | Key methods | Purpose |
|---|---|---|
| **General utils** | `clamp`, `clamp0to1`, `difference`, `angleDifference` | Safe numeric operations |
| **Waves** | `sineWave`, `sineWave0to1`, `triangleWave`, `quickSin` | Periodic oscillation without instantiating objects |
| **Formatting** | `formatSeconds`, `formatAbbreviatedNumber`, `intToRoman`, `format` | Display strings for UI (e.g. `1234567 → "1.2M"`, `8 → "VIII"`) |
| **Matrix maths** | `createModelMatrix`, `updateModelMatrix` (many overloads), `updateViewMatrix`, `calculateProjectionMatrix`, `calculateFittingProjectionMatrix` | Build TRS (translate-rotate-scale) matrices used by the renderer every frame |
| **Vector maths** | `distance`, `distance2d`, `distanceSquared`, `projectionScalarProportion`, `getFacingAngle`, `getDirectionFromAngle`, `capVectorLength`, `calculateEdgeNormal` | Spatial queries for collision, AI, spawning |
| **Geometry** | `calcNormalOfTriangle`, `normalizeAngle`, `randomPointOnCircle`, `generateRandomUnitVector`, `generateRandomUnitVectorWithinCone`, `rotateVec3` | Used by particle systems, rendering, physics |
| **Interpolation** | `mix`, `map0to1Range`, `mapRanges`, `smoothInterpolate`, `smoothStep`, `smootherStep`, `lerpTowards` | Every animation and transition |

Two important **globals** live here:
```java
public static final RandomGenerator RAND = new RandomGenerator();
public static final Noise NOISE = new Noise(10); // seed 10
```
Shared random + noise instances used everywhere, so seed-dependent behaviour is consistent per session.

**`calculateFittingProjectionMatrix`** — Unique projection that keeps vertical FOV fixed at normal aspect ratios but locks *horizontal* FOV once the window becomes wider than `wideAspectRatio`. This prevents ultra-wide monitors from stretching the game into a fisheye view.

---

### `Easing.java` (258 lines)

Pure easing functions, all take `t ∈ [0,1]` → return `[0,1]` (or a derived range).

| Function | Shape | Use case |
|---|---|---|
| `smoothStart2/3/4/5` | `tⁿ` — slow start, fast end | UI elements sliding in |
| `smoothStop2/3/4/5` | `1-(1-t)ⁿ` — fast start, slow end | UI elements decelerating |
| `smoothstep2` | `t²(3-2t)` — S-curve | Standard smooth transitions (also used by `Maths.smoothInterpolate`) |
| `smoothstep3` | `t³(6t²-15t+10)` — smoother S-curve | Higher quality animations |
| `arch` | `4t(1-t)` — inverted parabola (0 at both ends, 1 at peak) | Jump/hop arcs |
| `bounceArch` | arch + small tail bounce | Melee swings, bouncing items |
| `popAndWobble` | Exponentially damped sine | Item pickup animations, UI confirmation |
| `easeOutBounce` | 3-segment quadratic | Objects landing with a bounce |
| `elasticBounce` | `2^(-10t)*sin(...)` | Spring-like overshoot |
| `fadeInOut` | 0 → 1 → 0 with linear edges | Particle opacity, transition overlays |
| `fadeInfadeOut` | Smooth cubic ramp in, constant, ramp out | Long-duration transitions that need smooth edges |
| `jumpUp` / `jumpOff` | Quadratic arc for exactly one peak | Crops, animals jumping |
| `bellCurve` | Symmetric arch using `smoothStart3` + `smoothStop3` | Distribution effects |
| `softBounce` | Ping-pong with smooth reversal | Wind/sway effects |

---

### `RollingAverage.java`

A circular sliding window average using a `LinkedList<Float>`.

```
[v1, v2, ... v20] → sum / count
```

- Used by `FrameTimer` for delta smoothing.
- `addValue` drops the oldest entry once the window is full.
- O(n) per `getAverage()` — fine for n=20.

---

### `RollingAverageCounter.java`

Extends `RollingAverage` for **counting events per frame** (e.g. draw calls, entities rendered).

- `increment()` — call each time an event occurs
- `update()` — call once per frame; snapshots the count into the rolling window
- `getRecentMax()` — peak value in the last `framesPerMaxUpdate` frames — useful for debug overlays

---

### `RampFunction.java`

A stateful ramp that goes from 0→1 when `activate()` is called, and 1→0 when `activate()` stops being called.

```
Every frame where activate() IS called:     value += gradient * delta  (up to 1)
Every frame where activate() IS NOT called: value -= gradient * delta  (down to 0)
```

`activate` must be called every frame while the condition is true — it self-resets. Great for smooth transitions on held keys, wind gusts, etc.

---

### `Wave.java` / `SineWave.java` / `TriangleWave.java`

Abstract `Wave` with two concrete implementations for animated values. Every wave has:
- `period` — how long one full cycle takes (seconds)
- `min` / `max` — output range
- `randomize()` — jump to a random phase (used for variety in particle effects)
- `update(delta)` — advance time and return the new value

`SineWave` uses `sin(2π·t)`, scaled to `[min, max]`.
`TriangleWave` uses `|t·2 - 1|`, scaled to `[min, max]` — a linear sawtooth with no trig overhead.

**Factory patterns:**
```java
SineWave.create(2.0f)         // period=2s, output -1 to 1
SineWave.create(2.0f, 5f)     // period=2s, amplitude=5
SineWave.create0to1(1.0f)     // period=1s, output 0 to 1
```

---

### `Aabb.java` (Axis-Aligned Bounding Box)

A mutable 3D AABB that supports:
- `includeVertex` / `includeVertices` — expand bounds to include a point
- `recalculate(vertices[])` — rebuild from scratch
- `completelyContains(other)` — containment test (quad-tree use)
- `getVolume()`, `calculateCenter()`, `generateVertices()` — 8 corner points
- `getPercentageVolumeOf(parent)` — ratio of this volume vs parent
- `fromBoxes(BoundingBox[])` — merge multiple oriented boxes into one AABB

Initializes with "inside-out" bounds (`mins=MAX_VALUE, maxs=NEGATIVE_INFINITY`) so the first vertex always sets both.

---

### `BoundingBox.java`

An **oriented** bounding box — unlike `Aabb`, its 8 vertices can be transformed to any position/rotation via `transform(Matrix4f)`. Holds both the raw vertices and a `TransformBox` (for rendering the wireframe outline of the box).

`BoundingBox.fromAabb(aabb)` — convert a world-aligned box into a transformable one.

---

### `TransformAabb.java`

A live AABB that tracks an entity transform. Stores the **original** un-transformed AABB and recomputes the world-space bounds every time `transform(Transform)` is called by projecting all 8 corner vertices through the model matrix and re-fitting the AABB around them.

---

### `TransformBox.java`

A `Matrix4f` wrapper that stores a center+scale transform. `fromAabb(aabb)` creates a matrix positioned at the AABB center and scaled to its dimensions — used to render the visible outline box in debug views.

---

### `Direction.java`

An enum of all 8 compass directions (N, NE, E, SE, S, SW, W, NW) with integer XZ deltas:

```java
NORTH(0, -1)  EAST(1, 0)  SOUTH(0, 1)  WEST(-1, 0)
NW(-1,-1)     NE(1,-1)    SE(1,1)      SW(-1,1)
```

Helpers:
- `opposite()` — reverse direction using ordinal arithmetic (index 7 - ordinal)
- `translate(point, distance)` — move a Vec2 or Vec3 by a distance in this direction
- `randomCardinal()` / `random()` — used by entity AI
- `getByOrdinal(int)` — cached, avoids `values()` array allocation
- `getDirection(relX, relZ)` — reverse lookup from delta values

---

### `Rotation.java`

Four tile rotations (UP=0°, RIGHT=270°, DOWN=180°, LEFT=90°) with embedded logic for how they transform coordinates.

Each rotation stores: `swapCoords`, `negateX`, `negateZ` — enabling fast bit-flag-like transform without matrix math.

Key uses:
- `applyTileRotation(Vector3f pos)` — rotates a point within a 1×1 tile grid (around centre 0.5, 0.5)
- `applyRotation(Direction)` / `undoRotation(Direction)` — convert entity-facing directions when a structure is rotated
- `getRotationFromNorth(Direction)` — maps a cardinal Direction to the matching Rotation

---

### `Coords.java`

An immutable `(int x, int z)` pair for tile grid coordinates. Implements `Exportable` so it can be binary serialized to a save file as 8 bytes (2 × `writeInt`).

---

### `Vec2i.java`

A **mutable** `(int x, int z)` pair (no `y` — this is always a 2D grid). Use `Coords` for read-only storage, `Vec2i` when you need to modify coordinates in place.

---

### `Triangle.java` / `Vertex.java`

Simple geometric structs. `Vertex` holds `position + normal` (both `Vector3f`). `Triangle` holds three `Vertex` instances. `Triangle.newTriangle(p0, p1, p2, normal)` creates a flat-shaded triangle where all vertices share the same normal — used by geometry builders.

---

## 2 · `rng` — Random & Noise Generation

### `RandomGenerator.java`

A rich wrapper around Java's `java.util.Random`.

| Method | What it does |
|---|---|
| `randInt(max)` | 0 to max-1 |
| `randNewInt(max, prev)` | Like randInt but guaranteed different from previous (uses modulo trick) |
| `randFloat()` / `randFloat(max)` | Standard 0-1 or 0-max |
| `randFloatBetween(min, max)` | Explicit range |
| `varyFloat(avg, variance)` | avg ± random amount within variance |
| `varyFloatByPercent(avg, factor)` | avg ± (avg * factor) |
| `triangularRand(lowest, highest, mode)` | Triangle distribution — biased toward `mode` |
| `randomGauss(mean, stdDevFactor)` | Gaussian / normal distribution, clamped to ≥0 |
| `roundBasedOnChance(float)` | 2.7 → 2 (30%) or 3 (70%) probabilistically |
| `takeChance(float)` | Returns true with probability `float` |
| `randSubset(list, size)` | Random sub-list using shuffle |
| `randUnitVec2()` | Random unit vector on a circle |
| `randDirectionVec2(scale)` | Random unit vec scaled to radius |
| `randPosInRectangle` | Random 2D point in a defined rectangle |
| `randomPointInElipsoid` | Random 3D point inside an ellipsoid (used by particle spawners) |
| `generateRandomUnitVector()` | Uniformly distributed on sphere (spherical coordinate method) |

Seeded constructor `RandomGenerator(int seed)` enables reproducible procedural generation.

---

### `Noise.java`

**Deterministic integer-keyed noise** using squirrel hashing (not Perlin):

```java
// Squirrel hash constants
int noise1 = 0xB5297A4D;
int noise2 = 0x68E31DA4;
int noise3 = 0x1B56C4E9;
```

The same `noise(x)` input always produces the same output for the same `seed`. No state — purely functional.

- `noise(int)` → 0 to 1
- `noiseSigned(int)` → -1 to 1
- `noise(int x, int y)` → 2D hash using a prime multiplier (`198491317`)
- `smoothNoise(float)` — interpolates between two integer-keyed noise values using `smoothstep2`

`Maths.NOISE` is a shared instance with seed=10.

---

### `PerlinNoise.java`

Multi-octave Perlin noise for terrain generation.

```
total = Σ (octave i → amplitude=roughnessⁱ, frequency∝2ⁱ)
```

- `sample(x, y, scale)` — outputs roughly in [-1, 1] range
- `sample0To1` — mapped to [0, 1]

Smoothing: each grid point's value is blurred using a 3×3 kernel before bilinear interpolation.

---

### `SmoothNoiseFunction.java`

A **time-based** noise sampler. Call `update(delta)` every frame and it returns a smoothly wandering value in [0, 1].

```java
time += delta * roughness;
return noise.smoothNoise(time);
```

`roughness` controls how fast the noise "drifts". Used for organic randomness: wind variation, eye movement, idle animation jitter.

---

## 3 · `valueDrivers` — Animated Float Values

This package provides a **strategy pattern** for driving float values over time. All concrete drivers extend `ValueDriver`.

### `ValueDriver.java` — Abstract base

Manages:
- `currentTime` — accumulated delta time
- `startTime` — optional delay before animation begins
- `length` — period length in seconds
- `stopAfterPeriod` — if true, freezes at end value after one cycle
- `stopped` flag

`update(delta)` → advances time, computes `relativeTime ∈ [0,1]`, calls `calculateValue(relativeTime)`.

---

### Concrete Drivers

| Class | Shape | `calculateValue(t)` formula | Use case |
|---|---|---|---|
| `ConstantDriver` | Flat line | `return value` | Particles with fixed speed/size; mutable via `setValue` |
| `LinearDriver` | Straight ramp | `start + t * (end - start)` | Linear fades, gradual changes |
| `SlideDriver` | S-curve (one shot) | `smoothInterpolate(start, end, t)` | UI panels sliding in/out, camera moves |
| `BounceDriver` | Up-then-down (one shot) | smooth up to peak, smooth down to end | Item pickups, hop animations |
| `FadeDriver` | Trapezoid | linear in → peak → linear out | Particle alpha, sound volume envelopes |
| `WaveDriver` | Cosine wave (loops) | `0.5 + cos(t*2π)*(-0.5)` mapped to range | Wind sway, bobbing UI elements |
| `SinWaveDriver` | Sine wave (loops) | `0.5 + sin(t*2π)*0.5` mapped to range | Volume, brightness, idle oscillation |
| `KeyFrameDriver` | Arbitrary curve | Binary-search interpolation between `KeyFrame[]` | Complex custom animations |

### `KeyFrame.java`

A `(time, value)` pair where `time ∈ [0,1]` and `value` is any float. Used by `KeyFrameDriver` to define arbitrary animation curves. `KeyFrameDriver` uses binary search (`O(log n)`) to find the two surrounding keyframes.

---

## 4 · `hashIds` — The ID & Registry System

### `Id.java`

A namespaced identifier with the format `"namespace:localName"` (e.g. `"game:wheat"`, `"mymod:custom_crop"`).

Internally stores:
- `fullHash` — `"namespace:localName".hashCode()` — primary map key
- `modHash` — `"namespace".hashCode()` — allows filtering by mod
- `name` — the full string (only in "generation" mode)

**Two modes:**
- `Id.gen("game:wheat")` — creates a full ID with name (for registration)
- `Id.genForAccess("wheat")` — creates a hash-only ID for lookups (cheaper)
- `Id.load(reader)` — deserializes 8 bytes from a save file

**Serialization:** stored as 8 bytes (4 for fullHash + 4 for modHash) in save files.

---

### `HashId.java`

A simpler, older ID type that stores only `String.hashCode()`. Mostly legacy — predecessor to `Id`.

---

### `Registrable.java`

Interface: anything that can be registered in a `HashRegistry` must implement `getId(): Id`.

---

### `HashRegistry<T extends Registrable>`

The **typed, named, iterable registry** for `Registrable` objects.

- **Duplicate protection:** throws `ProgramError` on overwrite
- `getNotNull(...)` — throws rather than returning null (fail-fast)
- `getAll(Predicate<T>)` — filtered list
- `Iterable<T>` — supports enhanced for loops over all registered values

---

### `SimpleHashRegistry<T>`

Like `HashRegistry` but for types that don't implement `Registrable`. The caller provides the `Id` manually at registration time (`register(id, item)`).

---

## 5 · `errors` — Crash Handling

### `ProgramError.java`

A `RuntimeException` for expected programming errors (registry overwrites, null lookups).

---

### `ErrorManager.java`

Static crash handler that:
1. Installs itself as `Thread.setDefaultUncaughtExceptionHandler` on `init(folder)`
2. Shows a `JFrame` pop-up with the stack trace (via `ErrorPopUp`)
3. Writes a timestamped `.txt` log file to the `ErrorLogsTM/` folder
4. Sleeps the main thread for 100,000 s to keep the Swing pop-up alive

Log file naming: `"2026-03-13_20-33-47 Error_5207.txt"` — visible in your workspace `ErrorLogsTM/`.

---

### `ErrorPopUp.java`

A Swing `JFrame` pop-up with:
- A bold top message (user-facing explanation)
- A scrollable red `JTextArea` with the raw stack trace

This is the red error window players see when the game crashes.

---

## 6 · `listeners` — Observer Pattern

### `AbstractListenerSet<T>`

A generic listener set with **concurrent-removal safety**. If a listener removes itself during notification, the removal is deferred until after the notification loop completes.

### `BoolListenerSet` / `BoolListener`

A concrete listener set for `boolean` events (toggle changes, window resize). `BoolListener` is a functional interface: `listener.eventOccurred(boolean value)`.

---

## 7 · `fileUtils` — File & Resource I/O

### `MyFile.java`

A classpath-resource path builder. Provides `getInputStream()` via `Class.getResourceAsStream(path)` — for loading shaders, textures, language files inside the JAR.

### `FileUtils.java`

Static file utility methods:
- `getNameNoExt`, `deleteFile` (recursive), `openInputStream`/`openOutputStream`
- `renameFile` — atomic move via `Files.move`
- `generateTimeStampString()` — `"2026-03-13_20-33-47"` format for log names
- `readBoolean` / `booleanToInt` — integer-coded booleans for save file parsing

### `RootFolderFinder.java`

Tries 4 different methods in order to find the game's root folder:
1. `ClassLoader.getSystemClassLoader().getResource(".")`
2. `getProtectionDomain().getCodeSource().getLocation()` parent
3. Class resource URL, handling `jar:file:` prefix
4. `new File(".")` — current working directory fallback

If all 4 fail, `ErrorManager.crashWithUserAlert` is called. The `DefaultErrorLogs/` folder in your workspace contains crashes from when this detection was failing during development.

---

## 8 · `byteWork` — GPU Buffer Packing

### `DataUtils.java`

Low-level byte-packing utilities for vertex data sent to the GPU:

| Method | Purpose |
|---|---|
| `pack_2_10_10_10_REV_int(x,y,z,w)` | Packs 3 × signed 10-bit normals + 1 × 2-bit indicator into a 32-bit int. Saves 75% bandwidth vs 3 floats for normals |
| `quantizeNormalized` | Maps a float to `[0, highestLevel]` integer range |
| `packNormalizedFloatInShort` | Maps [0,1] float to [0, 65535] short — for UV coordinates |
| `createDirectByteBuffer` | Off-heap LWJGL memory via `MemoryUtil.memAlloc` |
| `releaseBuffer` | Frees off-heap memory via `MemoryUtil.memFree` |
| `intToByteArray` / `byteArrayToInt` | Big-endian int ↔ 4-byte array (used in `Id` serialization) |

### `ByteArrayBuilder.java`

A fluent writer backed by a `ByteBuffer`. Provides typed `store*` methods so vertex construction code reads naturally:

```java
builder.storeFloatVector(position);           // 12 bytes
builder.store_10_10_10_2_Vector(normal, 0);   // 4 bytes (packed)
builder.storeShortUvCoords(uvCoords);         // 4 bytes (packed)
// Total: 20 bytes per vertex instead of 32
```

---

## 9 · `inputs` — Developer Keyboard Console

### `UserKeyboard.java`

A **console input reader** for developer tools and editor scripts — not for in-game player input. Wraps `System.in` with a `BufferedReader` and provides blocking read methods: `getResponse`, `getNumber`, `getFloat`, `getVector`, `getYesOrNo`.

Used in internal build tools (e.g. `.obj → .cba` conversion scripts with user prompts). Not used during live gameplay.

---

## How the packages connect

```
                 ┌──────────────────────┐
                 │       Maths          │
                 │  (global RAND/NOISE) │
                 └──────────┬───────────┘
                            │ used by
         ┌──────────────────┼──────────────────┐
         ▼                  ▼                  ▼
      rng/             valueDrivers/      math3d primitives
  (Noise, Perlin,   (Drivers use Maths   (Aabb, Direction,
  RandomGenerator)   .smoothInterpolate)   Rotation, Coords)
         │                  │                  │
         └──────────────────┴──────────────────┘
                            │
                     hashIds/  ←──── errors/ProgramError
                  (Id, HashRegistry)
                            │
                     Used by entity system
                  (BlueprintRepositoryLoader,
                   GameRepository, EntitySystem)
```

`byteWork/` feeds the rendering pipeline directly.
`fileUtils/` is used during startup and save/load.
`listeners/` is used by the UI and input systems.

---

## 10 · `readWrite` — Serialization & I/O Framework

The central I/O layer. All game save/load and asset-loading code talks to `Reader`/`Writer` interfaces, with multiple format backends swappable underneath.

### Core interfaces (`readWrite/`)

| Type | Purpose |
|---|---|
| `Reader` | `readInt/Float/Boolean/String/Long/Short/Byte/Bytes/Vec3/Vec2/readByteArray/skipBytes/skipByteArray/close` |
| `Writer` | Symmetric write methods + `writeObject(Exportable)`, `writeObjectList`, `writeAsynchronousChunk` |
| `Exportable` | Anything that can be written. Default `getSerializer()` returns the `NO_EXPORT` no-op. |
| `Serializer` | Functional interface: `export(Writer)`. `NO_EXPORT` constant is a no-op lambda. |
| `StateSerializer` | Extends `Serializer` adding `loadState(Reader)`. `NO_SAVE` constant is a two-way no-op. |
| `LineSplitter` | Positional tokenizer: splits a string on a separator and exposes `getNextString/Int/Long/Float/Double/Bool/Vec2/Vec3`, `peek()`, `hasMoreValues()`. Used by CSV + CBA readers. |

### `binary/` — Java DataStream binary

- **`BinaryReader`** — Wraps `DataInputStream`. Open from `File`, `FileInputStream`, or `byte[]`. Big-endian Java binary format.
- **`BinaryWriter`** — Wraps `DataOutputStream`. Open from `File` or any `OutputStream` (including `ByteArrayOutputStream` for in-memory writes). Factory `openByteArrayWriter()`. `writeAsynchronousChunk(ByteArrayOutputStream)` writes a size-prefixed byte blob — used for save-file sections assembled concurrently.

### `csvSimplified/` — Single-separator CSV

Custom tabular format using `FileUtils.SEPARATOR` (not a real comma-CSV).

- **`CsvReader`** — Implements `Reader`. `nextLine()` reads the next row; subsequent `readInt/Float/String/Bool/Vec2/Vec3/readByteArray` calls consume tokens from that row via a `LineSplitter`.
- **`CsvWriter`** — Implements `Writer`. `nextLine()` emits a line break and resets the first-value flag. Booleans written as `0`/`1`.

### `realCsv/` — RFC-style comma CSV

Proper comma-separated, with quoted fields when a value contains a comma.

- **`RealCsvLine`** — Parsed CSV row. `next()` reassembles values that span multiple commas (quoted with `"`).
- **`RealCsvReader`** — `nextLine()` → parse into `RealCsvLine`; `getNextValue/Int/Long/Float/Bool/IntArray/FloatArray/Vector`.
- **`RealCsvWriter`** — Auto-quotes values with commas; `writeValue/Int/Float/Bool/writeVector/nextLine`.

### `misc/`

- **`ClipboardPrintWriter`** — A `PrintWriter` that mirrors all output to a `StringBuilder`. `copyToClipBoard()` pushes the buffer to the system clipboard — used in dev-time data-export tools.

### `cbaFiles/` — CBA format (human-readable structured text)

The primary format for blueprint/entity definition files (`.cba`). Indented brace blocks, `key = value` attributes, `[…]` arrays.

- **`CbaObject`** — In-memory node. Stores: `valueAttributes` (String), `objectAttributes` (nested `CbaObject`), `arrayAttributes` (`List<CbaObject>`), `bigStringArrayAttributes` (`List<String>` for multi-line `(…)` blocks). Rich typed getters: `getString/Int/Float/Boolean/getVector3f/getVector2f/getId/getColour/getIntArray/getFloatArray/getHexColourArray/getVec3Array/getStringArray/getObjectArray` — all with default-value overloads.
- **`CbaObjectReader`** — Parses `.cba` files line-by-line into a `CbaObject` tree. Handles `{ }` objects, `[ ]` arrays, `( )` large strings.
- **`CbaWriter`** — Writes `.cba` files. Tab-indented. `writeObjectStart/End`, `writeObjectArrayStart/End`, typed `writeString/Int/Float/Boolean/Colour/Vec3/FloatArray/IntArray`.
- **`CbaLoaderRegistry<T>`** — Typed loader registry backed by a `HashRegistry<RegistrableCbaLoader<T>>`. `load(CbaObject)` reads the `id` attribute and dispatches to the matching registered loader. Optional `DefaultCreator` used when the object is absent.
- **`RegistrableCbaLoader<T>`** — Interface: `Registrable` + `T load(CbaObject)`. Implement and register to support a new CBA-loadable type.

### `tagFormat/` — Tag binary format

Self-describing binary format with `HashId`-keyed tags. Field names are stored as 4-byte hashes — more efficient than CBA for save files.

- **`DataObject`** — In-memory tree node. Three `Map<HashId, …>` buckets: primitives, child objects, object arrays. Typed getters (`getFloat/Int/Long/Short/Boolean/Vec2/Vec3/String/Colour/IntArray`) all with defaults. `getSerializableReader(id)` returns a `BinaryReader` over a stored `byte[]` primitive — bridges old `Exportable` code.
- **`binaryReadWrite/Identifiers`** — Byte sentinels: `START (-1)`, `END (-2)`, `OBJ_ARRAY (-3)`.
- **`DataObjectReader`** — Reads the binary tag stream: byte identifier → HashId int → nested object, array, or typed primitive.
- **`DataObjectWriter`** — Writes the binary tag stream. `writeFloat/Int/Long/Boolean/String/IntArray`, `writeObject/writeObjectArray`, `writeSerializable/writeSerializableArray` (wraps legacy `Exportable` objects as `BYTE_ARRAY` primitives).
- **`HashedSerializer`** — Abstract: `writeData(DataObjectWriter)`.
- **`HashedStateSerializer`** — Adds `loadState(DataObject)`.
- **`HashedIdSerializer`** — Carries a `HashId` identifying this object within its parent.
- **`HashedIdStateSerializer`** — Adds `loadFromParentData(DataObject)` — looks up its own `HashId` key in the parent, then calls `loadStateFromThisData`.
- **`HashedSerializingUtils`** — Bridge: `saveHashedStateObject` / `loadHashedStateObject` connect the new tag format with legacy `Writer`/`Reader` streams.
- **`primitives/PrimitiveType`** — Enum (ordinal = byte identifier): `FLOAT, INT, SHORT, BOOLEAN, STRING, VEC2, VEC3, BYTE, LONG, INT_ARRAY, BYTE_ARRAY, COLOUR`. **Order must never change** (save file compatibility).
- Each primitive class (`FloatData`, `IntData`, `ShortData`, `BooleanData`, `StringData`, `Vec2Data`, `Vec3Data`, `ByteData`, `LongData`, `IntArrayData`, `ByteArrayData`, `ColourData`) implements `loadValue(Reader)` and `write(Writer)`.
- **`PrimitiveLoader.load(Reader)`** — reads one identifier byte → creates the matching subclass → calls `loadValue`.
- **`tagReadWrite/TagReader`** — Reads a human-readable tag text file into a `DataObject`. Auto-detects type: `"..."` → String, `#...` → Colour, `$...` → reference lookup, `.` in value → Float, else Int. Intended as a future CBA replacement.

---

## 11 · `mesh3d` — Indexed Mesh Primitives

- **`Corner`** — Enum of 4 tile corners (TOP_LEFT, TOP_RIGHT, BOTTOM_RIGHT, BOTTOM_LEFT) with 2D `(x, z)` offsets and a 1:1 mapping to `Rotation` values. `fromRotation` / `getCorrespondingRotation` convert between the two. `opposite()` returns the diagonally opposite corner.
- **`IndexedMesh`** — A `List<Vertex>` + `List<Integer>` indices base class. Supports sections: `startNewSection` / `startNewSection(colour)` advances the `indexOffset`. `generateTriangle` / `generateQuad` emit offset-adjusted indices. `getSectionVertex(localIndex)` addresses vertices within the current section. `getCurrentSectionVertexCount` counts vertices added since the last section start.
- **`Mesh3d`** — Extends `IndexedMesh` with high-level construction helpers:

| Method | What it does |
|---|---|
| `transformSection(translate, rotation)` | In-place TRS transform of all vertices in the current section |
| `rotateSection(rotation)` | Rotate the current section in place |
| `copyAndRotateSection(rotation)` | Duplicate the current section then rotate the copy |
| `append(Mesh3d)` / `append(Mesh3d, Rotation)` | Merge another mesh (with optional rotation) |
| `fan(center, points...)` / `fan(center, start, count)` / `fanLoop` | Triangle fan connectivity |
| `fill(topRow, bottomRow)` / `fill(topStart, perRow)` / `fill(top, bottom, perRow)` / `fillLoop` | Wall of quads between two rows of equal-count vertices |
| `storeVerticesAtHeight(y, normal, Vector2f...)` | Batch add 2D XZ vertices at a fixed Y |
| `generateQuadWithFaceNormal` | Generate a quad and compute the face normal from the geometry |

---

## 12 · `meshBuilding` — Vertex Buffer Assembly

Converts `Vertex` data into packed `byte[]` arrays ready for GPU upload. 20 bytes per vertex: 12 (float×3 position) + 4 (packed 10-10-10-2 normal) + 4 (packed RGBA colour).

- **`Vertex`** — Mutable struct: `Vector3f position`, `Vector3f normal`, `Colour colour`.
- **`MeshBuilder3d`** (interface) — Abstract 3D building contract: `addVertex`, `setCurrentColour`, `generateQuad/Triangle`, `startNewSection`, `repeatPreviousVertices`, `setHeightOfPreviousVertices`, `getCurrentSectionVertexCount`.
- **`MeshBuilder`** — `ArrayDeque<Vertex>` accumulator. `generateByteData()` flushes all vertices through `VertexByteArrayBuilder`. Subclasses override `initByteArrayBuilder()` to inject transform logic.
- **`MeshTransformBuilder`** — Subclass of `MeshBuilder`; uses `VertexTransformByteArrayBuilder` — applies rotation + translation on byte flush.
- **`MeshTranslateBuilder`** — Subclass; uses `VertexTranslateByteArrayBuilder` — translation only.
- **`ArrayMeshBuilder3d`** — Implements `MeshBuilder3d`. Buffers a `List<Vertex>` internally; forwards completed triangles to an inner `MeshBuilder`.
- **`QuadBuilder`** (meshBuilding) — Stores a `List<Vector3f>` position pool. `generateQuad/generateTriangle` calculate the face normal on-the-fly (`Maths.calcNormalOfTriangle`) and submit complete triangles to a `MeshBuilder`.
- **`IntArrayBuilder`** — `IntBuffer` wrapper for index arrays. `addInt`, `putIntArray`, `getArray`.
- **`VertexByteArrayBuilder`** — Extends `ByteArrayBuilder`. Stores 20 bytes/vertex. `storeVertex(Vertex)`, `storeIndexedMesh(IndexedMesh)` (iterates indices and stores each referenced vertex). `BYTES_PER_VERTEX = 20`.
- **`VertexTransformByteArrayBuilder`** — Extends `VertexByteArrayBuilder`. Overrides `storeVertex` to apply `Rotation.applyTileRotation` + translate to position and `applyRotationToVec3` to normal, using `Vec3Pool` to avoid allocations.
- **`VertexTranslateByteArrayBuilder`** — Extends `VertexByteArrayBuilder`. Adds `globalPos` to vertex position only.
- **`TransformByteArrayBuilder`** / **`TranslateByteArrayBuilder`** — Lower-level variants of the above that extend `ByteArrayBuilder` directly and expose `storeTransformedPosition/storeTransformedNormal` for callers that control the byte layout manually.

---

## 13 · `meshGeneration` — High-Level Mesh Shape Helpers

Utilities that generate specific geometry shapes from 2D profiles, curves, and procedural rules.

- **`ModelUtils`** — Static direction constants (`UP`, `RIGHT`, `LEFT`, `FORWARD`, `BACKWARD`), `copyVertices`, `reverseOrder`, `mirror(Vector2f[], Mirror)`, `processQuad(positions, normal, colour, Processor)`, `generateFlatQuad(xMin, xMax, zMin, zMax, colour, Processor)`, `canReduceInnerRoadCurve`.
- **`Processor`** (interface) — `processVertex(pos, normal, colour)` — the single consumer vertex is emitted to. Decouples shape generation from buffer writing.
- **`QuadBuilder`** (meshGeneration) — Fixed-size `Vector3f[]` position pool; `processQuad(i0,i1,i2,i3, norm, col)` emits 6 vertices (two triangles) to a `Processor`. *Distinct from `meshBuilding.QuadBuilder`.*
- **`CurveGenerator`** — Generates 2D arc vertices in polar coordinates: `calculateCurveVertices(radius, segmentCount)` → `segmentCount+1` points sweeping from `(radius, 0)` to `(0, radius)` (quarter-circle). `calculateRoundedCorner` offsets this into a box corner of size `cornerSize`.
- **`Mirror`** (enum) — `X_AXIS`, `Z_AXIS`, `BOTH`, `NONE`. `mirrorVec2(pos)` flips X and/or Z (BOTH additionally swaps the two coordinates).
- **`VertexFiller`** — Takes a 1D `Vector2f[]` profile, mirrors it horizontally, and fills in a strip of quads between the two lines using `ModelUtils.processQuad`. Used for symmetric road/path cross-sections.
- **`IndexEdge`** — An edge between two 2D vertex indices. `extend(height, triangles)` extrudes it vertically into two wall triangles. `hashCode/equals` treat the same pair regardless of winding order as equal — safe for `Set` deduplication.
- **`IndexTriangle`** — Three index references into a 2D vertex array. `getIndexEdge(i)` returns one of the 3 edges; `getTriangle(height)` lifts all three into 3D at the given Y.
- **`RoadVertex`** — A pre-built vertex (position + normal + colour). `storeInstanceData(buffer, gridX, gridZ, rotation)` transforms and packs it directly into a `ByteBuffer` — used for road tile GPU instancing without going through a `MeshBuilder`.

---

## 14 · `modelFormats` — 3D Model File I/O

Four sub-systems covering every 3D asset format used in the game.

### `objects/` — Shared intermediate representation

- **`MaterialInfo`** (interface) — `getColour(): Colour`
- **`ColourMat`** — Solid colour material.
- **`PaletteMat`** — Palette-indexed: `ColourPalette palette + uvX, uvY` → `palette.get(uvX, uvY)`.
- **`GroupMat`** — Stub returning `null` colour (placeholder for group-level materials).
- **`ModelSection`** — List of `Triangle` + integer `sectionId` + `MaterialInfo`. `getVertexCount() = triangles.size() * 3`.
- **`Model`** — List of `ModelSection` + optional min/max bounds. `getTotalVertexCount()`, `getSectionColours(Colour[])`.

### `objImporter/` — Wavefront OBJ import

- **`RawObjData`** — Mutable lists of positions, normals, tex coords accumulated during parsing.
- **`ObjMaterial`** — name, colour, alpha, specularFactor, shinyness, iqr — from `.mtl` file.
- **`ObjVertex`** — index + position + normal + optional UV.
- **`ObjModelSection`** — Named section: `List<ObjVertex>` + index list + `indicesOffset`.
- **`ObjModel`** — Named list of `ObjModelSection`. `getVertexCount()` / `getIndicesCount()`.
- **`MtlFileImporter`** — Reads `.mtl`: for each `newmtl`, parses shinyness, ambient, diffuse colour, specular, IQR, alpha.
- **`ObjImporter`** — Reads `.obj`: scans for `mtllib`, processes `v/vn/vt/o/usemtl/f` lines. Deduplicates vertices with a `HashMap<String, ObjVertex>`. Returns `List<ObjModel>`. Entry point: `ObjImporter.importModels(File)`.

### `streamlineFormat/` — Game's custom streamline CSV format

- **`StreamlineExporter`** — Writes a `Model` to `CsvWriter`. Header (total verts, section count), then per section: metadata (id, vertex count, material type + colour), then triangle data (position×3 + normal×3 per vertex). Material prefixes: `$` = colour, `&` = palette.
- **`StreamlineImporter`** — Reads back from `CsvReader`. Supports `$`, `*` (colour + alpha), `&` (palette) material types.
- **`ByteDataExtractor`** — Converts a `Model` directly to packed `byte[]` via `VertexByteArrayBuilder` — for runtime loading without an intermediate CSV pass.
- **`ModelDataExtractor`** — Abstract template: subclass provides `storeVertex(model, section, vertex, byteArray)` and the base handles all triangle iteration.

### `texturedObj/` — UV-mapped OBJ (no normals, texture coords only)

- **`Vertex`** — `Vector3f position` + `Vector2f textureCoords`.
- **`Triangle`** — Three `Vertex` instances.
- **`TexturedModel`** — A `Set<Triangle>`.
- **`TexturedObjLoader`** — Parses `.obj` keeping `v` and `vt` only. UV Y is flipped (`1 - y`). Entry point: `TexturedObjLoader.loadModel(File)`.
- **`TexturedModelDataExtractor`** — 20 bytes/vertex: `float×3 position` + `float×2 UV`.

### `smoothPoly/` — The game's primary 3D model format (`.cba` / `.obj`)

**Model data classes:**

| Class | Contents |
|---|---|
| `SmoothPolyVertex` | `final position + normal`. `getTextureCoords()` returns `(0,0)` |
| `SmoothPolyUvVertex` | Extends with actual `Vector2f uvCoords` |
| `SmoothPolyMaterial` | colour, `customMatFactor` (0→1 blend to runtime custom colour), `customMaterialIndex` (0–3), `specularFactor`, `shinyness`, `flexibility` (wind sway), `flexAnchorHeight` |
| `SmoothPolyModelSection` | id + material + `SmoothPolyVertex[]` + `hasUvCoords` flag |
| `BoundingInfo` | `xzRadius` (footprint circle) + `height` — for culling |
| `SmoothPolyModel` | Implements `Registrable`. Sections + shared index array + `BoundingInfo`. Flags: `hasTransparency`, `usesMultipleCustomColours`, `hasShadow`. `merge(other)` appends sections and offset-adjusts indices. |

**Importers:**
- **`BoundsProcessor`** — Accumulates `maxHeight` and max `xzRadius²` across vertices. If a pre-calculated `BoundingInfo` is provided, it passes through unchanged.
- **`AttributeData`** / **`AttributeExtractor`** — Parse Blender material name suffixes encoded as `!key:value` pairs (e.g. `myMat!flex:0.3!part:2`).
- **`SmoothPolyObjImporter`** — Chains `ObjImporter` → `SmoothPolyModel`. Reads attribute tags from material names: `flex`, `uvs`, `mat` (material factor), `part` (custom mat index), `alpha`, `anchor`. Converts Blender Phong shinyness to the game's 0–100 range.
- **`SmoothPolyCbaImporter`** — Reads `.cba` files. Loads bounds, sections, index array, per-section vertex float arrays (6 floats/vertex, or 8 with UV), and material properties.
- **`SmoothPolyModelImporter`** — Router: dispatches to `SmoothPolyObjImporter` (`.obj`) or `SmoothPolyCbaImporter` (`.cba`) based on file extension.

**Exporter:**
- **`SmoothPolyCbaExporter`** — Writes a `SmoothPolyModel` to `.cba`: bounds block (`xzRadius`, `height`), `indices` int array, and per-section vertex float array (interleaved px/py/pz/nx/ny/nz[/u/v]) + material fields.

**Utility:**
- **`SmoothPolyAabbExtractor`** — Projects all model vertices through a `Matrix4f` and includes them in an `Aabb`. `calculateAabb(transform)` returns the world-space bounding box for a transformed model instance — used for shadow frustum fitting and entity culling.

---

## 15 · `colours` — Colour Math & Palette System

- **`Colour`** — The universal colour value object (RGBA floats). Mutable. Key operations:

| Method | Purpose |
|---|---|
| `Colour(r,g,b)` / `(r,g,b,a)` / `(int r,g,b)` / `(Colour)` / `(Colour, alpha)` | Many constructors |
| `hex(String)` | Parse `#RRGGBB` hex string |
| `toLinearSpace()` | Apply gamma 2.2 — call once when loading sRGB textures |
| `asByteArray()` | RGBA as 4 bytes — used for GPU vertex packing |
| `getAlphaByte()` | Alpha as a single byte |
| `convertToHsv()` | Returns `HsvColour` via `Color.RGBtoHSB` |
| `getLuminance()` | Perceptual brightness `0.2126r + 0.7152g + 0.0722b` |
| `scale(f)` / `multiplyBy(Colour)` / `increaseColour(r,g,b)` | In-place math |
| `mix(c1, c2, blend, dest)` | Linear blend; writes to `dest` (or new object if null) |
| `add(c1, c2, dest)` / `sub(c1, c2, dest)` | Component-wise add/subtract |
| `hsvToRgb(h,s,v)` | Static HSV → RGB conversion |
| `fromBytes(byte[])` / `getAsDirectFloatBuffer()` | GPU upload helpers |
| `isEqualTo(Colour)` / `duplicate()` | Comparison and copy |

- **`HsvColour`** — Mutable hue/saturation/value triple. `convertToRgb()` delegates to `Colour.hsvToRgb`.
- **`ColourGradient`** (interface) — `get(float t)` for `t ∈ [0,1]` → `Colour`. 1D gradient abstraction.
- **`GradientPoint`** — Immutable `(position ∈ [0,1], colour)` pair for defining gradient stops.
- **`ColourGradientMulti`** — Implements `ColourGradient` with N `GradientPoint`s. Points are sorted by position at construction. `get(t)` binary-linear-searches for the surrounding pair and linearly interpolates.
- **`ColourPalette`** — A 2D grid of `Colour` objects stored in linear space. Loaded from a PNG via `ImageData`; each pixel becomes one palette entry. `get(x, y)` returns the colour at column x, row y.
- **`ColourRepository`** — A `Map<String, ColourPalette>`. `addPalette`, `getColourPalette(id)`, `getColour(paletteId, x, y)` (returns a duplicate).

---

## 16 · `dataStructures` — Custom Data Structures

- **`Bundle<T>`** — A `Collection<T>` that wraps a `Set<Collection<? extends T>>`. `addAll(collection)` adds an entire existing collection reference in O(1) — no copying. `merge(bundle)` merges two bundles. Iteration uses `BundleIterator`. `add(single item)` is unsupported (logs an error). Useful for gathering entities from multiple subsystem lists without flattening.
- **`BundleIterator<T>`** — Two-level iterator: outer iterates the inner collection references; inner iterates each collection. `hasNext` is true if any inner iterator has more elements.
- **`EasyArray<T>`** — A fixed-capacity generic array with a write pointer. `add(item)` appends at the pointer; `isFull()` checks capacity; `getArray()` returns the backing array.
- **`Registry<T>`** — A `HashMap<String, T>` with `register(id, item)`, `get(id)`, `clear()`. Simpler alternative to `HashRegistry` when `Id` hashing is not needed.
- **`SafeList<T>`** — A list safe to mutate during iteration (single-threaded). Defers `add`/`remove` calls to waiting queues during iteration; applies them automatically when `hasNext()` returns false at the end of a full sweep.
- **`Tuple<T,S>`** — Immutable `(key, value)` pair. `getKey()` / `getValue()`.

---

## 17 · `fileWatcher` — Hot-Reload File Monitoring

- **`FileChangeWatcher`** — Wraps Java's `WatchService` to monitor specific files for modifications at runtime. `registerFileToWatch(File)` watches the file's parent folder. `getChangedFiles()` polls the watch service and returns a `Set<File>` of modified registered files since the last call. Used by dev tools for shader/asset hot-reload. `FileChangeWatcher.init()` is the factory — gracefully falls back to a no-op instance if the watch service cannot start.

---

## 18 · `gameRegistry` — Lazy Forward-Reference Registry

Extends `HashRegistry<T>` to handle assets that reference other assets which may not yet be loaded at parse time.

- **`GameRegistry<T>`** — Subclass of `HashRegistry<T>`. Overrides `register(item)` to also resolve any pending `Reference` objects waiting for that `Id`. `getReference(id)` returns a `Reference<T>` immediately — if the item is already loaded, the reference is populated at once; otherwise it queues the reference and populates it when the item is eventually registered. `completeLoading()` logs any IDs that were requested but never fulfilled.
- **`Reference<T>`** — Holds an `Id` and (optionally) the resolved item `T`. `onAvailable(ReferenceListener<T>)` fires the callback immediately if already resolved, or stores it for later. Static helper `referenceArray(references[], itemArray[])` wires up an array of references to fill a parallel item array.
- **`ReferenceListener<T>`** — Functional interface: `onAvailable(T item)`.

---

## 19 · `images` — Image Loading

Two complementary image loaders for different use cases:

- **`ImageData`** — AWT-based (`BufferedImage`). Loaded via `ImageIO.read`. `getColour(x, y)` extracts `int RGB` → `Colour`. `getPixelColours(boolean convertToLinearSpace)` extracts the entire image as a `Colour[width][height]` array. Used to load palette PNGs into `ColourPalette`.
- **`RawByteImage`** — STB-based (via `STBImage.stbi_load`). Loads image file directly into a `ByteBuffer` with 4 channels (RGBA). Keeps the width and height. Used for textures sent directly to OpenGL.

---

## 20 · `memory` — GPU Memory Slot Allocator

A doubly-linked-list allocator that tracks which regions of a GPU buffer (VAO) are in use and which are free gaps — enabling re-use of freed slots without full buffer rebuilds.

- **`MemorySlotChain`** — The allocator. Manages a linked list of `MemorySlot`s. `allocateMemory(length)` finds the first gap large enough and splits it (first-fit strategy), or appends to the end. `appendMemory(length)` always appends. `remove(slot)` converts a data slot back into a gap. `getCurrentByteSize()` returns the total size (including gaps) by reading the tail slot's end index.
- **`MemorySlot`** — A node in the linked list. Holds `startIndex`, `length`, and `previous`/`next` pointers. `getEndIndex() = startIndex + length`. `remove()` replaces itself with a `GapSlot`. `isGap()` returns false for data slots.
- **`GapSlot`** — Extends `MemorySlot`. Represents a free region. `fillWith(dataSlot)` places a data slot at the start of the gap, shrinking or eliminating the gap. Adjacent gaps are automatically merged via `connectToNext/connectToPrevious` overrides. When a gap is reduced to zero length it removes itself from the chain entirely.

---

## 21 · `misc` — Miscellaneous Utilities

- **`AsciiValues`** — Named constants: `ENTER (13)`, `BACK (8)`, `SPACE (32)`. Static helpers `isLetter(ascii)` and `isNumber(ascii)` — used by in-game text input boxes.
- **`Listener`** — Functional interface: `eventOccurred()` — zero-payload event notification.
- **`ListenerSet`** — A concurrent-safe `Listener` set. Defers `addListener`/`removeListener` calls made during `notifyListeners()` to `toAdd`/`toRemove` sets, flushing them after the notification loop completes. Older, simpler sibling of `listeners.AbstractListenerSet` (which carries a typed value).

---

## 22 · `modifiers` — Stackable Float Modifiers

Pattern for moddable game values (e.g. crop speed, sell price). Multiple sources can each contribute a multiplier; the final value is their product applied to a base.

- **`Multiplier`** (interface) — `getValueMultiplier(): float`. Inner `DefaultMultiplier` always returns `1`.
- **`FloatModifier`** — A constant-value `Multiplier` wrapping a `final float`.
- **`Multipliers`** — Holds a `Set<Multiplier>`. `addMultiplier` / `removeMultiplier` / `getMultiplier()` (product of all). Safe for any number of sources.
- **`ModifiableValue`** — Extends `Multipliers`. Stores a `baseValue` and a cached `modifiedValue`. Overrides `addMultiplier`/`removeMultiplier` to immediately recalculate `modifiedValue = baseValue * getMultiplier()`. `get()` returns the cached result — zero-cost reads.

---

## 23 · `objectPools` — Allocation-Free Vector Pools

Avoid per-frame `new Vector*f()` heap allocations in hot render/physics paths by recycling instances.

- **`ObjectPool<T>`** — Abstract thread-safe pool backed by a `Stack<T>`. `get()` pops (or calls `createNewObject()` if empty). `release(T)` pushes back (drops silently if at `maxSize`). Pool size cap defaults to 100 in all concrete pools.
- **`Vec3Pool`** — Static pool of `Vector3f`. `get(x,y,z)`, `get(ReadableVector3f)`, `get()` (zeroed). `release(Vector3f...)` releases varargs.
- **`Vec2Pool`** — Static pool of `Vector2f`. Same pattern; `release(Vector2f)` and `releaseAll(Vector2f...)`.
- **`Vec4Pool`** — Static pool of `Vector4f`. Extra `get(Vector3f, w)` for quick 4D promotion. `release(Vector4f)` and `releaseAll(Vector4f...)`.

---

## 24 · `smoothValues` — Exponential Interpolation Wrappers

All smooth values share the same `agility`-based approach: every frame, `actual` moves a fraction `min(delta * agility, 1)` of the remaining distance to `target`. Higher agility = faster tracking.

| Class | Tracks | Key extras |
|---|---|---|
| `SmoothFloat` | `float` | `cancelTarget()` (snap target to actual), `force(v)` (instant jump), `increaseTarget(dt)` |
| `LinearSmoothFloat` | `float` | Moves at constant `speed` units/sec instead of exponential; clamps at target |
| `SmoothAngle` | `float` angle | Uses `Maths.angleDifference` so interpolation wraps correctly across the 0°/360° boundary |
| `SmoothColour` | `Colour` | Uses `Vec3Pool` internally; `setTarget(Colour)` / `force(Colour)` |
| `SmoothVec3` | `Vector3f` | `increaseTarget/increaseAll`, `forceOnlyActualValue` (shift both by same delta), `reached()` |
| `SmoothVector2f` | `Vector2f` | `getDistanceToTarget()`, `forcePreserveTarget` (shift actual, keep relative offset), `reached()` |

---

## 25 · `timing` — Timer Hierarchy

All timers extend abstract `Timer`, which implements `Exportable` (save/load via `TimerSerializer`).

**`Timer` base:**
- `check(delta)` — advances `time`; calls `targetReached()` and returns `true` when `time >= duration`.
- `restart()` / `stop()` / `pause()` / `continueOn()` — lifecycle control.
- `randomizeStartTime()` — jump to a random phase within `[0, duration)`.
- `TimerSerializer` (inner class) — saves/loads `duration`, `time`, `running` as 3 values.

**Concrete timers:**

| Class | Behaviour |
|---|---|
| `SingleTimer` | Fires once then stops (`running = false`) |
| `LoopingTimer` | Wraps: `time %= duration` on trigger — loops forever at fixed period |
| `RandomLoopingTimer` | Like `LoopingTimer` but picks a new random `duration ∈ [minTime, maxTime]` after each trigger |
| `Countdown` | Counts **down** from a given time. `check(delta)` decrements; returns true at zero. `getProgress()` → 0→1 over the countdown. Implements `Exportable` (saves `time` + `startTime`). |
| `NanoTimer` | Wall-clock timer using `System.nanoTime()`. Useful for performance budgets: `check()` subtracts elapsed nanos; returns true when budget is exhausted. `restart()` resets. |

---

## 26 · `version` — Version Value Object

- **`Version`** — Immutable `majorVersion.minorVersion.update[patch]` (e.g. `"1.4.2"` or `"1.4.2b"`). `patch` defaults to `'a'` (omitted from `toString`). `isNewerThan(Version)` compares in order: major → minor → update → patch char. Implements `Exportable`.
- **`Version.VersionSerializer`** — Writes/reads 4 `int`s (major, minor, update, patch char as int). Static `VersionSerializer.load(Reader)` reconstructs a `Version` from a save stream.

