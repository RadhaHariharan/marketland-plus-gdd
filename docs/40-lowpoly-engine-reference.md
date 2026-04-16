# LowPolyEngine — Complete In-Depth Reference
> **13 top-level domains · Every class, interface, and design pattern documented**
> Package root: `thinmatrix.lowPolyEngine`

---

## Package Directory

```
lowPolyEngine/
├── audio/
│   ├── core/                    ← OpenAL context, master, sound loading, source pools
│   │   ├── emptyShells/         ← No-op fallbacks when OpenAL fails
│   │   ├── globalVolume/        ← Volume modifier system
│   │   ├── loading/             ← OGG/PCM loading, streaming factory
│   │   ├── openAlObjects/       ← Direct OpenAL wrappers (buffers, sources, listener)
│   │   ├── soundPlaying/        ← Playthrough objects, play parameters
│   │   ├── sourcePools/         ← AL source pooling per AudioType
│   │   └── streaming/           ← Background streaming service
│   └── gameConcepts/            ← High-level gameplay audio
│       ├── ambient/             ← Ambient sound player
│       ├── compoundSounds/      ← Multi-track compound sounds + prefabs
│       ├── misc/                ← AudioFader
│       ├── music/               ← Sequential music player
│       ├── sound2d/             ← 2D non-positional sounds
│       ├── sound3d/             ← 3D positional sounds + emitter
│       └── soundBuilding/       ← Builder/provider pattern for sounds
├── engineMain/
│   ├── gameObjects/             ← Camera, GameCamera, Light, Environment, MouseRay
│   ├── master/                  ← Engine, EngineCreator, EngineConfigs, EngineFiles, EngineMod
│   └── splashScreen/            ← Splash screen UI and minimal boot engine
├── features/
│   ├── behaviours/              ← Behaviour-tree action system
│   │   └── standardNodes/       ← Composite, sequence, selector, wait, loop nodes
│   │       └── newComposites/   ← Newer condition/selector/sequence nodes
│   ├── debugSystem/             ← Typed debug data (float, count, count-total)
│   ├── debugger/                ← Global Debugger singleton + DebugFormat
│   ├── frustumCulling/          ← Frustum planes, sphere/AABB tests
│   └── movement/                ← Steering, path-following, move animations
├── guis/
│   ├── components/              ← Clickable, checkbox, toggle, tooltip, drag detection
│   ├── constraints/             ← 38 constraint types for layout
│   ├── customCursor/            ← Cursor loading and manager
│   ├── gardenUiPrefabs/         ← Ready-made UI widgets (buttons, sliders, scroll panels…)
│   ├── grids/                   ← Grid layout helpers
│   ├── layout/                  ← BaseLayout, ValueSheet
│   ├── scalingAlgorithms/       ← UI scaling strategies
│   ├── text/                    ← Bitmap-font pipeline (load → generate mesh → render)
│   ├── transitions/             ← Animator, Animation, Effect, Transition + blueprints
│   ├── uiComponent/             ← UiComponent base class, positioning, alpha, displayer
│   ├── uiMain/                  ← Ui static facade, UiContainer, UiConfigs
│   ├── uiRendering/             ← OpenGL UI shader + renderer
│   ├── uiResources/             ← UiStyle, resource manager, hot-loader
│   └── utils/                   ← Effects, Padding, Transitions helpers
├── inputsOutputs/
│   ├── stateControl/            ← State interface, StateManager, InputUser, priority queue
│   ├── timing/                  ← FrameTimer (delta + current time)
│   ├── userInputs/              ← Keyboard, Mouse, MouseButton, click checkers
│   └── windowing/               ← GLFW Window, WindowBuilder, Sync, IconLoader
├── openglWrapper/
│   ├── fbos/                    ← FBO, FboBuilder, attachments
│   ├── openglObjects/           ← Vao, Vbo, Attribute + standard attribute types
│   ├── openglUtils/             ← OpenglUtils, GlRenderConfigs, FullScreenQuad, VaoUtils
│   ├── shaders/                 ← ShaderProgram base + Uniform* types
│   └── textures/                ← Texture, TextureBuilder, ArrayTexture, TexData
├── particles/
│   ├── batches/                 ← Insertion-sort batching for mesh and quad particles
│   ├── loading/                 ← .cba particle effect file loader + hot-loader
│   ├── particleEffects/         ← Emitter, component system, 20+ components, params
│   └── rendering/               ← Instanced mesh + quad particle renderers
├── postProcessing/              ← PostProcessingFilter base + common GLSL vertices
├── renderData/
│   ├── byteExtracting/          ← ByteFormat, multi-model byte extractors
│   ├── instancing/              ← InstancedDataVao, RenderInstance
│   ├── meshAtlas/               ← SmoothPolyMeshAtlas, updater
│   └── vboMemoryMapping/        ← VboMemoryManager, ResizingArrayVbo, DataBundle
├── rendering/
│   ├── boxRenderer/             ← Wire-box debug renderer
│   ├── entityRenderer/          ← Per-entity transform renderer
│   ├── simpleMeshRenderer/      ← Simple unlit mesh renderer
│   ├── smoothPolyRenderer/      ← Main dynamic smooth-poly renderer (shadow + fog + wind)
│   └── smoothPolyUvRenderer/    ← UV-mapped variant of smooth poly renderer
├── resourceManagement/
│   ├── certificates/            ← Encrypted unlock/achievement certificate files
│   ├── languageSystem/          ← CSV-based localisation (GameText, LangRepository)
│   ├── requestProcessing/       ← BackgroundLoader, GL-thread request queue
│   └── saveSystem/              ← SaveSystem, SaveGame, SavingProcess, metadata
├── shadows/
│   ├── rendering/               ← Shadow map master renderer + dynamic shadow renderer
│   └── shadowBox/               ← Frustum-fitting shadow box, terrain clamping
└── utils/                       ← EngineUtils, TextureExporter, container types
```

---

## 1 · `engineMain` — The Engine Core

### 1.1 `master` — Engine Lifecycle

#### `Engine`
The central singleton that owns every subsystem. Constructed exclusively by `EngineCreator`.

| Member | Type | Purpose |
|--------|------|---------|
| `window` | `Window` | GLFW window handle |
| `keyboard` | `Keyboard` | Frame-buffered key state |
| `mouse` | `Mouse` | Normalised mouse position + buttons |
| `audioMaster` | `AudioMaster` | OpenAL audio manager |
| `stateManager` | `StateManager` | Priority-queued game state machine |
| `debug` | `EngineDebug` | Per-frame debug data (fps, tri count, …) |
| `timer` | `FrameTimer` | Delta time + absolute game time |
| `mods` | `EngineMod[]` | Active mod list |

**Key methods:**

| Method | Description |
|--------|-------------|
| `Engine.init()` | One-call bootstrap with default configs |
| `Engine.init(mods, configs)` | Parameterised bootstrap |
| `update()` | Per-frame tick — updates UI, audio, input, window, state, debug, clears frame buffer |
| `getDelta()` | Returns `timer.getDelta()` (with SPACE = 0.1× and ALT+SPACE = 10× cheat multipliers) |
| `completeSetUpAfterLoading(LoadingProcess)` | Loops `update()` while loading completes then closes splash |
| `completeSetUp()` | Closes splash immediately with no loading wait |
| `requestClose()` / `isCloseRequested()` | Soft close flag |
| `closeEngine()` | Cleans up particles, BackgroundLoader, UI, audio, window |
| `Engine.instance()` | Static access to the running singleton |

---

#### `EngineCreator`
Internal factory that orchestrates the two-phase startup:

1. **`initEssentialSystems`** — Creates `ErrorManager`, `BackgroundLoader`, `Window`, OpenGL context, `FrameTimer`, `Keyboard`, `Mouse`, `Ui`.
2. **Shows splash screen** via `SplashScreenEngine.init()`.
3. **`initEngineSystems`** — Loads `GameText`, UI resources, `StateManager`, `AudioMaster`, `ParticleMaster`.
4. Waits for `BackgroundLoader.isDoneProcessing()` (all background tasks done).
5. Returns the fully-initialised `Engine`.

---

#### `EngineConfigs`
POJO configuration object. All fields are public and mutable before `init()`.

| Field | Default | Meaning |
|-------|---------|---------|
| `windowWidth/Height` | 1280 × 720 | Initial window size |
| `backgroundColour` | `#c8dfdc` | Clear colour |
| `fullscreen` | false | |
| `vsync` | true | |
| `msaa` | true | Multisampled anti-aliasing |
| `fps` | 100 | Target frame rate |
| `hotloading` | false | Live-reload of particles, UI value sheets |
| `locale` | `en` | Language locale |
| `splashScreenCreator` | `DefaultSplashScreenUi::new` | Factory for the splash screen |
| `initialState` / `defaultState` | `EmptyState` | First and fallback game states |
| `debug` | `new EngineDebug()` | Debug data container |
| `volumeModifierTypes` | `EngineVolumeControls.values()` | Volume mod types |
| `uiConfigs` | `new UiConfigs()` | UI scale, style, hot-loading |

---

#### `EngineFiles`
Static file-path registry. All paths are derived from `FileUtils.getRootFolder("res")`.

Notable paths: `RES_FOLDER`, `GUI_FOLDER`, `VALUE_SHEETS_FOLDER`, `SOUND_FOLDER`, `FONT_FOLDER`, `ICON_FOLDER`, `LANG_FILE`, `MODS_FOLDER`, `SPLASH_SCREEN_FOLDER`.

---

#### `EngineMod`
Interface a game implements to define a content mod:
- `getRootFolder()` — disk location of this mod's assets
- `getNamespace()` — unique string prefix for all IDs in this mod

The engine itself registers a default mod using `EngineFiles.ROOT_FOLDER` and `Id.DEFAULT_NAMESPACE`.

---

#### `EngineVolumeControls`
Default enum implementing `VolumeModType`. Single value `GLOBAL` that applies to all `AudioType` values. Games can define their own enum (e.g. `MASTER`, `SFX`, `MUSIC`) by implementing `VolumeModType`.

---

#### `LoadingProcess`
Functional interface with one method: `boolean updateLoading()`. Returns `true` when done. Used to drive the splash screen while assets load.

---

### 1.2 `gameObjects` — Scene Objects

#### `Camera`
Core projection + view matrix calculator with dirty-flag caching.

- Stores `position`, `pitch`, `yaw`, `nearPlane`, `farPlane`, `aspectRatio`, `wideAspectThreshold`.
- **Wide aspect handling**: below `wideAspectThreshold` (default 2:1), the vertical FOV is fixed. Above it, the horizontal FOV is fixed instead (prevents extreme horizontal stretching on ultra-wide screens).
- Matrices are lazily recomputed only when `dirtyView`/`dirtyProjection` are set.
- `getProjectionViewMatrix()` multiplies both matrices every call (noted as a TODO optimisation).

---

#### `GameCamera` (abstract)
Extends `Camera` and adds game-level concerns:

- **`MouseRay mouseRay`** — automatically kept in sync after every `move()` call.
- **`CameraFrustum frustumCuller`** — updated each frame for frustum culling.
- **Orientation vectors** (`forward`, `right`, `up`) — recalculated from pitch/yaw each frame.
- Implements `AudioListener` — provides forward/up vectors to OpenAL listener.
- Implements `Exportable` — state can be serialised/deserialised.
- `convertToWorldPosition(screenX, screenY, dis)` — unprojects screen-space coordinates to world-space at a given camera distance.
- Abstract methods: `move()` (per-frame input) and `cancelSmoothTargets()` (stable resting state for scene transitions).

---

#### `Light`
Directional light with normalised direction, colour, and a settings vector:
- `lightSettings.x` = ambient strength
- `lightSettings.y` = diffuse strength
- `lightSettings.z` = shade (reserved)

---

#### `Environment`
Immutable value object combining a `Light sun` and a `float fogDensity`. Passed to renderers.

---

#### `MouseRay`
Performs unprojection of the mouse cursor into a world-space ray every frame.  
Pipeline: screen → NDC → clip → eye (inverse projection) → world (inverse view).  
Key methods: `getRay()`, `getPointOnRay(float)`, `getIntersectionWithYPlane(float)`.

---

### 1.3 `splashScreen` — Boot Screen

#### `SplashScreen` (abstract)
Extends `UiComponent`. Rendered at render level 100 (on top of everything). The subclass must implement `isReadyForLoading()` — controls when engine loading begins.

#### `SplashScreenEngine`
A minimal render loop (no audio, no particles) that runs until the splash screen signals readiness. Drives `Ui.update()`, `BackgroundLoader.doTopGlRequests()`, and `Window.update()` in a tight loop.

#### `SplashScreenCreator`
Functional interface: `SplashScreen createSplashScreen()`. Default is `DefaultSplashScreenUi::new`.

#### `DefaultSplashScreenUi`
Built-in animated splash that shows the engine logo. Overrides `isReadyForLoading()` to return true after the intro animation completes.

---

## 2 · `inputsOutputs` — Input, Window, State

### 2.1 `windowing`

#### `Window`
GLFW window wrapper. Created via `Window.newWindow(w, h, title).setVsync(...).fullscreen(...).withIcon(...).create()`.

- Tracks both **screen-coordinate** size and **pixel/framebuffer** size (differ on HiDPI displays).
- `update()` — `glfwSwapBuffers` + `glfwPollEvents` + `frameSync.sync()`.
- `addSizeChangeListener(WindowSizeListener)` — fires on framebuffer resize.
- `goFullScreen(boolean)` — runtime toggle using `glfwSetWindowMonitor`.
- `destroy()` — full GLFW teardown.

#### `WindowBuilder`
Builder returned by `Window.newWindow(...)`. Chainable setters: `setVsync`, `fullscreen`, `withIcon`, `setMSAA`, `setFps`.

#### `Sync`
Busy-waits to enforce a target FPS when VSync is off.

#### `IconLoader`
Loads a set of PNG icon files into a `GLFWImage.Buffer` for the window icon.

---

### 2.2 `userInputs`

#### `Keyboard`
GLFW key callback → four `HashSet<Integer>` collections (down, pressed-this-frame, released-this-frame, repeated-this-frame) + char list.

| Method | Description |
|--------|-------------|
| `isKeyDown(key)` | True while held |
| `keyPressEvent(key)` | True only on the first frame |
| `keyPressEvent(key, checkRepeats)` | Also fires on OS key-repeat |
| `keyReleaseEvent(key)` | True on release frame |
| `getChars()` | Unicode chars typed this frame (text input) |
| `isAnyKeyPressed()` | Quick check |
| `update()` | Clears per-frame sets each tick |

#### `Mouse`
GLFW callbacks → normalised `x`,`y` (0–1 in screen coords), `dx`,`dy`, `scroll`, button sets.

| Method | Description |
|--------|-------------|
| `isButtonDown(button)` | True while held |
| `isClickEvent(button)` | True on press frame |
| `isReleaseEvent(button)` | True on release frame |
| `isShortClick(button)` | True if released quickly (not a drag/hold) |
| `isButtonHeld(button)` | True if held longer than short-click threshold |
| `isDoubleClick()` | Detected by `DoubleClickChecker` |
| `getX() / getY()` | 0–1 normalised position |
| `getDx() / getDy()` | Per-frame delta |
| `getScroll()` | Scroll wheel delta this frame (reset to 0 each tick) |

#### `MouseButton`
Enum wrapping GLFW button constants. Used to index `ShortClickChecker[]`.

#### `ShortClickChecker`
Tracks press time per button. Classifies as short-click or long-hold.

#### `DoubleClickChecker`
Detects two quick clicks within a time window.

---

### 2.3 `stateControl`

#### `State` (interface)
```java
int getPriority();
void init();
```
States are identity-compared (`==`), not by value. `init()` is called on every transition into the state.

#### `StateManager`
Priority-queued state machine:
- `suggestState(state, waitForEndRequest)` — inserts into sorted queue by priority.
- `endState(state)` — removes a specific queued state.
- `updateState()` — processes queue head each frame; auto-removes non-persistent states.
- `registerUser(InputUser, State...)` — registers a keyboard/mouse input consumer for specific states; automatically enabled/disabled on transitions.
- `registerKeyboardUser` / `registerMouseUser` — finer-grained registration.

#### `InputUser`
Interface for objects that need keyboard/mouse access in specific states. `StateManager` calls `initState()` / `endState()` on the `RegisteredUsers` tracker on each transition.

#### `KeyboardAccess` / `MouseAccess`
Thin wrappers that give an `InputUser` access to the relevant input objects only when the correct state is active.

#### `EmptyState`
Default no-op `State` implementation.

---

### 2.4 `timing`

#### `FrameTimer`
- `update()` — measures elapsed time since last call, caps delta at a maximum to prevent physics explosions.
- `getDelta()` — elapsed seconds since last frame.
- `getTime()` — total elapsed time in seconds.
- Configured at construction with the target frame cap.

---

## 3 · `openglWrapper` — OpenGL Abstraction

### 3.1 `openglObjects`

#### `Vao`
Thin wrapper around an OpenGL Vertex Array Object. Created with `Vao.create()`.

| Method | Description |
|--------|-------------|
| `createDataFeed(maxVertexCount, usage, Attribute...)` | Allocates a VBO with interleaved attributes, links pointers |
| `createInstanceDataFeed(maxInstances, Attribute...)` | Same but sets `glVertexAttribDivisor(1)` for instancing |
| `initDataFeed(FloatBuffer, usage, Attribute...)` | Uploads initial data immediately |
| `linkInstancingVbo(Vbo, Attribute...)` | Links an external VBO for instanced data |
| `createIndexBuffer(IntBuffer)` | Creates element array buffer |
| `createIndexBufferFeed(maxIndexCount)` | Allocates but doesn't upload |
| `enableAttributes()` | Enables all tracked attributes |
| `delete(deleteVbos)` | Deletes VAO (and optionally all child VBOs) |

Attribute layout is **interleaved** — stride is the sum of all attribute sizes.

#### `Vbo`
Wrapper around `GL_ARRAY_BUFFER` or `GL_ELEMENT_ARRAY_BUFFER`. `storeData(offset, buffer)` uses `glBufferSubData` for partial updates.

#### `Attribute` (abstract)
Describes one vertex attribute: `attributeNumber`, `bytesPerVertex`. Subclasses call `GL20.glVertexAttribPointer` with appropriate type and count.

**Standard attribute subclasses:**

| Class | Data | GL type | Bytes |
|-------|------|---------|-------|
| `Vec3Attribute` | xyz | float | 12 |
| `Vec2Attribute` | uv | float | 8 |
| `NormalAttribute` | normal xyz | float | 12 |
| `ColourAttribute` | rgba | float | 16 |
| `UvAttribute` | u,v | float | 8 |
| `IntAttribute` | single int | int | 4 |

---

### 3.2 `shaders`

#### `ShaderProgram` (abstract)
Full GLSL compile, link, and validate pipeline.

- Constructor compiles vertex + fragment shaders, links, binds attribute locations, deletes shader objects.
- `completeSetup()` — validates program; calls `initVariables()` if `indicateVariablesInitNeeded()` was called.
- `linkTextureSamplers(UniformSampler...)` — binds samplers to texture units 0, 1, 2, … in order.
- `start()` / `stop()` — `glUseProgram`.
- `cleanUp()` — `glDeleteProgram`.

**Uniform types:**

| Class | GL call |
|-------|---------|
| `UniformFloat` | `glUniform1f` |
| `UniformVec2/3/4` | `glUniform2/3/4fv` |
| `UniformMatrix` / `UniformMatrix2` | `glUniformMatrix4fv` |
| `UniformBoolean` | `glUniform1i` (0 or 1) |
| `UniformSampler` | `glUniform1i` (texture unit index) |

#### `Uniforms`
Helper that manages a map of uniform name → `Uniform` object, auto-queries locations via `glGetUniformLocation`.

---

### 3.3 `fbos`

#### `Fbo`
Full FBO manager with multi-attachment and multisampling support. Built via `Fbo.newFbo(window, w, h)` or `Fbo.newMultisampledFbo(...)` builder pattern.

| Method | Description |
|--------|-------------|
| `bindForRender(colourIndex)` | Binds as draw target, sets draw buffer, sets viewport |
| `bindForRender()` | Binds without changing draw buffer |
| `unbindAfterRender()` | Restores default FBO and window viewport |
| `blitToScreen(colourIndex, w, h)` | GPU blit to default framebuffer |
| `blitToFbo(srcIdx, targetFbo, targetIdx)` | Resolve multisampled FBO |
| `reInitColourAttachment(index)` | Re-creates a colour attachment (used on window resize) |
| `getFboTexture(attachmentId)` | Returns `Texture` for a `TextureAttachment` |
| `getDepthBuffer()` | ID of depth attachment |
| `isComplete()` | Checks `GL_FRAMEBUFFER_COMPLETE` |
| `delete()` | Deletes all attachments |

**Attachment types:** `TextureAttachment` (readable depth/colour) and `RenderBufferAttachment` (non-readable, faster for MSAA).

---

### 3.4 `textures`

#### `Texture`
Lazy-initialized OpenGL texture. Supports `GL_TEXTURE_2D` and array textures.

| Method | Description |
|--------|-------------|
| `Texture.init2d()` | Creates and binds a 2D texture immediately (GL thread) |
| `Texture.loadFromFile(File)` | Returns a `TextureBuilder` (decode now, GL upload via BackgroundLoader) |
| `storeDataRgba(TexData)` | Uploads RGBA pixel data |
| `initRgbaStorage(w, h, format)` | Allocates empty RGBA storage |
| `initDepthStorage(w, h, precision)` | Allocates depth storage |
| `bindToBank(n)` | `glActiveTexture(GL_TEXTURE0+n)` + `glBindTexture` |
| `setNearestFiltering()` / `setLinearFiltering()` | Min/mag filter shortcuts |
| `setMipmapParams(generateMipmap, anisotropic, bias)` | Full mipmap config |
| `setClampedEdges(clamp)` | Repeat or clamp-to-edge wrap |
| `setClampToBorder(colour)` | Border colour wrap mode |

#### `TextureBuilder`
Decodes PNG on calling thread; posts an OpenGL upload request via `BackgroundLoader.addOpenGlRequest()`.

#### `ArrayTexture` / `ArrayTextureLoaderGl`
2D texture array for sprite sheets or particle texture atlases.

---

### 3.5 `openglUtils`

#### `OpenglUtils`
Static utilities: `clearFrameBuffer`, `prepareFrameBuffer`, `enableAlphaBlending`, `enableDepthTesting`, `bindTextureToBank`.

#### `GlRenderConfigs`
Holds boolean flags (`depthTesting`, `antialiasing`, `backfaceCulling`, `alphaBlending`). Call `apply()` before a draw call to synchronise GL state.

#### `FullScreenQuad`
Singleton VAO for a screen-aligned quad — used by post-processing filters.

#### `VaoUtils`
Low-level interleaved data packing helpers.

---

## 4 · `rendering` — Renderers

### 4.1 `smoothPolyRenderer` — Main World Renderer

#### `SmoothPolyDynamicRenderer`
The primary scene renderer for all smooth-polygon 3D geometry.

**Per-frame pipeline:**
1. Apply `GlRenderConfigs` (depth, AA, backface cull).
2. Bind shadow map texture.
3. Load camera (proj-view matrix), sun (colour, direction), fog, wind time, camera position, lighting settings.
4. Iterate `SmoothPolyDynamicBatch.getIterator(camera)` — frustum-culled iterator.
5. For each visible entity: load model matrix, alpha, tint colour, custom material colours.
6. Draw with `glDrawElements(GL_TRIANGLES, indexCount, GL_UNSIGNED_INT, startOffset)`.

**Shader uniforms loaded:**
- `projectionViewMatrix`, `modelMatrix`, `lightColour`, `lightDirection`
- `fogDensity`, `time` (wind animation), `cameraPosition`, `shadowMapSpace`
- Full lighting: `sunDiffuseStrength`, `ambientStrength`, `ambientDirectionalBias`, `skyReflectionStrength`, `rimLightStrength`, `sunSpecularStrength`, `specularShinyness`
- Tone-mapping: `brightness`, `contrast`, `saturation`, `filmicValue`, `rrtValue`, `basicValue`
- Material: `materialFactor`, `materialColours[N]`, `tintColour`, `alpha`, `useAlphaIndicator`

#### `SmoothPolyDynamicBatch<T>` (interface)
```java
Vao getVao();
boolean isEmpty();
Iterator<T> getIterator(Camera camera);  // Camera passed for frustum cull
```

#### `SmoothPolyRenderData` (interface)
Contract for renderable entities: `getTransform()`, `getCurrentMesh()`, `isVisible()`, `getAlpha()`, `hasTint()`, `getTintColour()`, `getMaterialFactor()`, `getMaterialColours()`, `hasMultipleCustomCols()`.

---

### 4.2 Other Renderers

| Renderer | Shader | Purpose |
|----------|--------|---------|
| `SmoothPolyUvRenderer` | `smoothPolyUvVertex/Fragment.glsl` | UV-textured variant of smooth-poly |
| `EntityRenderer` | `entityVertex/FragmentShader.glsl` | Per-entity transform rendering |
| `SimpleMeshRenderer` | `simpleVertex/FragmentShader.glsl` | Unlit flat mesh |
| `BoxRenderer` | `boxVertex/Fragment.glsl` | Debug AABB/OBB wire boxes |

---

### 4.3 `RenderConfigs`
Global render constants, e.g. `WIND_SPEED` used by the shader's wind animation `time` uniform.

### 4.4 `LightingSettings`
Value object with all lighting parameters. `TEMP_GLOBAL_LIGHT` is a static instance used until a proper per-scene system is implemented.

---

## 5 · `renderData` — GPU Data Management

### 5.1 `vboMemoryMapping`

#### `VboMemoryManager`
Manages a `ResizingArrayVbo` that grows on demand, allocating/freeing byte ranges for dynamic geometry.

#### `ResizingArrayVbo`
A `GL_ARRAY_BUFFER` that doubles its capacity when full (similar to an `ArrayList`). Tracks used regions.

#### `DataBundle`
Holds the raw byte slice for one object's GPU data. Written by a `ByteFormat` and committed to the VBO.

#### `MemoryMapper` / `MemoryManagerCreator`
Factory + utility for initialising memory managers with the correct format.

---

### 5.2 `byteExtracting`

#### `ByteFormat` (interface)
Defines how a `SmoothPolyMesh` (or similar) is serialised into bytes for upload.

**Standard formats:**

| Class | Content |
|-------|---------|
| `SmoothPolyBaseFormat` | Positions + normals + material indices |
| `SmoothPolyMatFormat` | Positions + normals + per-vertex material colours |
| `SmoothPolyUvFormat` | Positions + normals + UVs |

#### `MultiModelByteExtractor`
Extracts bytes from multiple mesh models and packs them into a single contiguous buffer.

---

### 5.3 `instancing`

#### `InstancedDataVao`
VAO that holds per-instance transform data in a separate VBO. Updated with `glBufferSubData` each frame.

#### `RenderInstance`
Lightweight value object containing a model matrix and any per-instance shader data.

---

### 5.4 `meshAtlas`

#### `SmoothPolyMeshAtlas`
A single shared VAO containing all mesh data for a batch. Objects index into it using byte offsets.

#### `MeshDataAtlasUpdater`
Updates the atlas when meshes are added or removed. Re-packs the VBO.

---

### 5.5 `MeshData`
```java
int getStartIndex();   // byte offset into the index buffer
int getIndexCount();   // triangle count × 3
```
Used in `renderEntity()` calls: `glDrawElements(GL_TRIANGLES, indexCount, GL_UNSIGNED_INT, startIndex * BYTES_IN_INT)`.

---

## 6 · `shadows` — Shadow Mapping

### `ShadowMaster`
High-level controller. Created with `ShadowMaster.init(ShadowConfigs)`.

| Member | Description |
|--------|-------------|
| `shadowMap` (Fbo) | Depth-only FBO for the shadow map |
| `getShadowMapSpace()` | Combined light proj-view matrix used in main shader |
| `setShadowDistance(float)` | Adjusts shadow frustum extent at runtime |
| `updateShadowMap(batches, camera, sun)` | Binds FBO → renders shadow pass → unbinds |

### `ShadowConfigs`
Configuration: `shadowMapSize`, `shadowDistance`, `depthBufferFormat`, `shadowBoxClampHeight`, `shadowBoxZOffset`.

### `ShadowBox`
Calculates the light-space AABB that tightly fits the camera's view frustum:
- `update(camera, sun)` — recomputes fit each frame.
- `getShadowMapSpace()` — orthographic light proj × light view matrix.
- `getShadowBoxSpace()` — light-space matrix used for the shadow pass.

### `FrustumFittingBox`
Math helper that projects all 8 frustum corners into light space and computes the tight AABB.

### `FrustumTerrainClamper`
Extends the shadow box downward to always include the terrain, preventing shadows from being cut off.

### `SnappingBox`
Snaps the shadow box to texel boundaries to eliminate shadow shimmer on movement.

### `ShadowMapMasterRenderer` / `ShadowDynamicRenderer`
Renders all dynamic geometry into the depth FBO using a simplified shader (`shadowDynamicVertex/Fragment.glsl`) — only transforms, no lighting or colour.

---

## 7 · `particles` — Particle System

### 7.1 Core Types

#### `Particle`
Base class for all particles. Public fields: `position (Vector3f)`, `velocity (Vector3f)`, `baseScale`, `elapsedTime`, plus abstract `getSize()`, `isAlive()`.

#### `MeshParticle` / `QuadParticle`
Concrete particle types. `MeshParticle` stores a mesh reference; `QuadParticle` stores texture atlas row/column.

### 7.2 `particleEffects`

#### `ParticleEffect` (interface)
```java
void pulse(Transform);                    // emit a fixed burst
void update(Transform);                   // emit PPS × delta particles
void pulse(Transform, ParticleEffectParams);
void update(Transform, ParticleEffectParams);
ParticleEffect createVariant(ParticleEffectParams);
ParticleEffect createVariant(ParticleEffectParam...);
void copySettings(ParticleEffect);
```

#### `ParticleEmitter` (abstract)
Implements `ParticleEffect`. Calculates particles-to-create this frame = `pps × delta` + probabilistic rounding. Delegates to `ParticleEffectComponent[]` for initialisation and update.  
Applies `Transform` to particle position and velocity using model matrix multiplication.

#### `ParticleEffectComponent` (interface)
```java
void initParticle(Particle, ParticleEffectParams);   // called on spawn
void updateParticle(Particle);                       // called each frame
```

**Built-in components (20+):**

| Component | Effect |
|-----------|--------|
| `BounceParticleComp` | Reverses y-velocity (with damping) when particle hits `bounceHeight`, also damps horizontal velocity |
| `GravityParticleComp` | Applies downward acceleration |
| `MovementParticleComp` | Integrates velocity into position |
| `DragParticleComp` | Velocity × drag factor |
| `SpeedParticleComp` | Randomised initial speed |
| `FadeParticleComp` | Alpha fade over lifetime |
| `ScaleUpParticleComp` | Size grows over lifetime |
| `SizeParticleComp` | Randomised initial size |
| `LifeLengthParticleComp` | Sets random lifetime within range |
| `ColourParticleComp` | Sets initial colour (random from range) |
| `FanOutParticleComp` | Spreads velocity in a cone |
| `Rotate3dParticleComp` | Rotates particle in 3D |
| `OffsetParticleComp` | Random position offset from emitter |
| `HeightFadeParticleComp` | Fades based on world-space Y height |
| `TextureAnimateParticleComp` | Advances sprite sheet frame |
| `SquareSpawnParticleComp` | Spawns in a square area |
| `CircleSpawnParticleComp` | Spawns on a circle |
| `LineSpawnParticleComp` | Spawns along a line |
| `SphereParticleSpawn` | Spawns on a sphere surface |
| `ChimneyParticleSpawn` | Spawns in an upward cone (chimney shape) |
| `CuboidChimneySpawn` | Spawns in a box with upward bias |

#### `ParticleEffectVariant`
Wraps a base `ParticleEmitter` + overrides specific parameters via `ParticleEffectParams`. Delegates all calls to the base emitter, injecting the variant params.

#### `CompoundParticleEffect`
Combines multiple `ParticleEffect` instances into one call — useful for complex multi-layered effects.

---

### 7.3 `params`

#### `ParticleEffectParams`
Map from `ParticleEffectParam` type → value. Supports `FloatParam`, `Vec3Param`, `ColourParam`. Components read from this map to override defaults.

#### `FloatVar` / `Vec3Var` / `ColourVar`
Randomisable value types used inside components — hold a base value + optional random range.

#### `CustomVariable`
Extension point: arbitrary custom data keyed per-component.

---

### 7.4 `batches`

#### `MeshParticleBundle`
Holds all live `MeshParticle` instances + the shared `InstancedParticleMeshVao`. Each frame: insertion-sort by camera distance for correct transparency ordering, then upload instance data.

#### `QuadParticleBundle` / `QuadVaoCreator`
Same concept for textured quad particles. Maintains the instanced quad VAO.

#### `InsertionSort`
Custom insertion sort for the particle list — efficient because particles are nearly sorted frame-to-frame.

---

### 7.5 `loading`

#### `ParticleEffectLoader`
Deserialises `.cba` particle effect files using the toolbox tag-format reader.

#### `ParticleFxHotLoader`
Wraps `ParticleEffectLoader` for hot-loading: watches the particle effect folder and reloads changed files at runtime.

#### `EffectLoaderCreator`
Factory: creates the loader + optionally the hot-loader depending on `hotloading` flag.

---

### 7.6 `ParticleMaster`
Singleton coordinator.

| Method | Description |
|--------|-------------|
| `renderParticles(camera, light)` | Update + render in one call |
| `updateParticles(camera)` | Advance simulation + upload instance data |
| `clearAllParticles()` | Remove all live particles |
| `getGlobalEffect(id)` | Look up a pre-loaded effect by filename |

---

### 7.7 `rendering`

Both renderers use instanced rendering (one draw call per particle type):
- **`MeshParticleRenderer`** — renders mesh-based particles. Shader: `meshParticleVertex/Fragment.glsl`.
- **`QuadParticleRenderer`** — renders textured billboarded quads. Shader: `quadParticleVertex/Fragment.glsl`.

---

## 8 · `audio` — Audio System

### 8.1 `core`

#### `AudioMaster`
Singleton audio coordinator.

| Method | Description |
|--------|-------------|
| `AudioMaster.init(volumeModTypes, soundFolders)` | Initialises OpenAL, loads sounds, creates source pools |
| `playSound(Sound, PlayParams)` | Acquires a source, applies params, starts playback (or streams) |
| `update(delta)` | Updates listener, ticks all active playthroughs |
| `cleanUp()` | Stops all sounds, destroys streaming thread, destroys AL context |
| `instance()` | Static singleton access |
| `setCurrentScene(Object)` | Scene tag for scene-local sound stopping |

If `AlContext.init()` fails, `EmptyAudioMaster` is substituted — all methods become no-ops.

#### `Sound`
Data object: `AlBuffer` ID (or -1 if not fully loaded), `fullyLoaded` flag, sample rate, channel count.

#### `SoundRepository`
Registry of all loaded sounds, keyed by `HashId`.

#### `AudioConfigs`
Per-sound config: `AudioType`, base volume, loop flag, etc.

---

### 8.2 `openAlObjects`

| Class | Wraps |
|-------|-------|
| `AlContext` | OpenAL device + context creation/destruction |
| `AlBuffer` | `alGenBuffers` — holds PCM data |
| `AlSource` | `alGenSources` — plays from a buffer or stream |
| `AlListenerManager` | Sets 3D listener position/orientation/velocity each frame |
| `AudioListener` (interface) | Implemented by `GameCamera` — provides forward/up vectors |
| `AlError` | `alGetError` wrapper with descriptive messages |

---

### 8.3 `soundPlaying`

#### `SoundPlaythrough`
Represents one active play of a sound. Manages:
- Volume (global × type × local), pitch, loop flag
- 3D position if applicable
- `update(delta)` — checks for `AL_STOPPED`, handles looping, streaming, scene checks
- `end()` / `hasEnded()` / `fadeOut(seconds)`

#### `PlayParams`
Builder for sound parameters:

| Method | Description |
|--------|-------------|
| `setVolume(float)` | 0–1 |
| `setPitch(float)` | 1 = normal |
| `setLoop(boolean)` | |
| `set3dPosition(Vector3f)` | World-space position |
| `setScene(Object)` | Scene tag — sound auto-stops on scene change |

#### `AudioType`
Enum: `MUSIC`, `SFX`, `AMBIENT` (used to route to different source pools and volume channels).

#### `VolumeControl`
Tracks a source's runtime volume factors.

---

### 8.4 `globalVolume`

#### `VolumeLevels`
Maintains one `float` level per `VolumeModType`. `getGlobalVolume(AudioType)` multiplies all modifier levels that affect this type.

#### `GlobalVolume`
Singleton holding a reference to `VolumeLevels`.

#### `VolumeModType` (interface)
```java
AudioType[] getAffectedTypes();
```
Implemented as an enum by the game. Example: `GLOBAL` affects all types; `MUSIC` affects only `AudioType.MUSIC`.

#### `VolumeMod`
Value object pairing a `VolumeModType` with a current level (0–1 float).

---

### 8.5 `loading`

#### `SoundLoader`
Decodes `.ogg` and PCM sound files using the `OggStream` decoder. Uploads to `AlBuffer` on the main thread.

#### `AudioStream` / `OggStream`
Streaming decoder for large files — reads in small page-sized chunks without loading the whole file.

#### `AudioStreamFactory` / `SoundRepositoryLoader`
Scans the sound folder tree and loads all sound files into the `SoundRepository`.

---

### 8.6 `sourcePools`

#### `SourcePool`
Manages a fixed-size pool of `AlSource` objects for a given `AudioType`. If all sources are in use, the quietest/oldest source is evicted.

#### `SourcePoolCreator`
Creates a `Map<AudioType, SourcePool>` with configurable pool sizes per type.

---

### 8.7 `streaming`

#### `StreamingService`
Runs a background thread that buffers audio data from `AudioStream` into `AlSource` buffer queues. Uses a producer-consumer pattern — sources are added to the queue and the thread continuously refills their buffers.

#### `ActiveStream`
Represents one actively streaming sound: tracks the `AlSource`, the decoder, and the refill state.

---

### 8.8 `gameConcepts`

#### `Sound2d` / `Sound2dBuilder`
Non-positional sound. Builder sets volume, pitch, type, loop. `play()` returns a `SoundPlaythrough`.

#### `Sound3d` / `Sound3dBuilder`
Positional sound. Additional: `setMaxDistance`, `setRolloff`. `play(Vector3f)` calls `PlayParams.set3dPosition`.

#### `Sound3dEmitter`
Attaches a `Sound3d` to a moving game entity — updates the position of the playthrough each frame.

#### `AmbientSound` / `AmbientSoundPlayer`
Crossfades between ambient sound layers based on game state (e.g. weather, indoors/outdoors).

#### `MusicPlayer`
Sequential playlist: plays tracks in order, advancing `nextTrackIndex` when the current `SoundPlaythrough.hasEnded()`. `start()` must be called to begin.

#### `MusicTrack`
Pairs a `Sound` with a volume level.

#### `CompoundSound` / `CompoundSoundPlaying`
A group of `Track` objects with `TrackPlaying` instances. Suitable for complex multi-layer sounds.

**Track prefabs:**

| Class | Behaviour |
|-------|-----------|
| `LoopTrack` | Loops indefinitely until stopped |
| `EndingTrack` | Plays once, then the compound sound ends |
| `RandomTrack` | Picks randomly from a list each play |
| `TriggerTrack` | Waits for an external trigger to play |

#### `AudioFader`
Smoothly fades the volume of a `SoundPlaythrough` from one level to another over a given duration.

#### `SoundBuilder` / `SoundProvider` / `SoundUtil`
Builder pattern for constructing sounds with pitch/volume randomisation:
- `SingleSoundProvider` — always returns the same sound
- `RandSoundProvider` — randomly picks from a list
- `SimplePitchProvider` — fixed pitch
- `VaryingPitchProvider` — random pitch within a range
- `PitchProvider` (interface) — can be lambda

---

## 9 · `guis` — User Interface

### 9.1 `uiComponent` — Core Component

#### `UiComponent` (abstract)
The base of every UI element. Owns:
- **`UiPositioner positioning`** — screen-space bounds, constraint system.
- **`AlphaControl alpha`** — inherited + local alpha management.
- **`UiDisplayer displayer`** — display/undisplay transitions.
- **`Animator animator`** — lazy-initialised animation engine.

**Lifecycle:**
1. `add(component, constraints)` → sets parent, stores constraints, calls `doSetUp()`.
2. `doSetUp()` → resolves level, inherits clipping bounds, positions itself, calls `init()`, inits children.
3. `update(delta, parentsDisplayed)` → calls `updateSelf()`, `updateAnimation()`, `displayer.update()`, recurses.
4. `remove()` → schedules for removal; `delete()` → recursively frees resources.

**Key methods:**

| Method | Description |
|--------|-------------|
| `add(component, constraints)` | Adds a child |
| `addInStyle(component, constraints)` | Adds with display transition |
| `addText(text, x, y, width)` | Convenience for text children |
| `show(boolean)` | Toggle visibility (propagates to children) |
| `display(boolean)` | Show/hide with transition |
| `setDisplayed(boolean)` | Instant show/hide without transition |
| `close()` | Graceful animated removal |
| `remove()` | Instant removal |
| `replaceInStyle(newComponent, removeOld)` | Cross-fade swap |
| `clipChildrenToBounds()` | Scissor-clip children to this component |
| `clipToGuideBounds(guide)` | Scissor-clip to another component |
| `setLevel(int)` | Render layer (100 = on top) |
| `notifyDimensionChange(scaleChange)` | Propagates resize event through tree |
| `isMouseOver()` | Checks mouse position + clipping bounds |
| `isClickedOn(MouseButton)` | `isMouseOver() && isClickEvent(button)` |
| `reload()` | Clear + re-`init()` |
| `setReloadOnSizeChange()` | Auto-reload on window resize |
| `testMouseoverOnChildren()` | Use children's bounds for mouseover |

---

#### `UiPositioner`
Resolves `UiConstraints` (4 constraints: x, y, width, height) relative to the parent's `Dimensions` to compute absolute screen-space `Dimensions`.

#### `AlphaControl`
Calculates total alpha as `selfAlpha × parentTotalAlpha`. Animators can modify this multiplicatively.

#### `UiDisplayer`
Manages display states with optional transition animations. Supports `display()`, `undisplay()`, `undisplayThenDisplay()` (for swapping components).

#### `Dimensions`
Holds `x, y, width, height` in UI units. `contains(mouseX, mouseY)` for hit testing.

---

### 9.2 `uiMain`

#### `Ui`
Static facade for the entire UI system.

| Method | Description |
|--------|-------------|
| `Ui.init(window, mouse, keyboard, configs)` | Initialise renderers, cursor manager, scaling |
| `Ui.loadResources()` | Load style and texture repositories |
| `Ui.update(delta)` | Update resource manager, layout tree, render all UI + text |
| `Ui.cleanUp()` | Destroy renderers and cursors |
| `Ui.getContainer()` | Root `UiContainer` |
| `Ui.getMouse()` / `getKeyboard()` | Shared input access |
| `Ui.getDisplayWidth/Height()` | Width/height in UI units (pixels ÷ uiSizeFactor) |
| `Ui.getActualDisplayWidthPixels()` | Raw pixel width |
| `Ui.setManualUiSize(float)` | Runtime UI scale override |
| `Ui.isMouseInUi()` | True if mouse is over any UI component |
| `Ui.enableMouseInteraction(boolean)` | Toggle mouse interaction globally |

#### `UiContainer`
Root component; always full-screen. Not added to a parent — uses `forceInitialization()`.

#### `UiConfigs`
UI configuration: `style`, `uiScalingAlgorithm`, `manualUiSize`, `enableHotloading`.

#### `UiScalingAlgorithm` (interface)
`float getScaleFactor(displayWidth, displayHeight)`. Two implementations:
- **`HomegrownScaling`** — scales proportionally to a reference resolution.
- **`DefaultUiScaling`** — fixed scale of 1.

---

### 9.3 `constraints` — Layout System

Constraints implement `UiConstraint` — a single method `float getSize(UiPositioner)` or `float getPosition(UiPositioner)`. The `UiPositioner` provides access to parent and self dimensions.

**38 constraint types grouped by purpose:**

| Category | Constraints |
|----------|-------------|
| **Absolute** | `PixelConstraint`, `PixelOtherConstraint`, `CappedPixelConstraint` |
| **Relative** | `RelativeConstraint`, `RelativeSelfConstraint`, `RelativeOtherConstraint`, `RelativeOtherAxisConstraint`, `FillRelativeConstraint` |
| **Centering** | `CenterConstraint`, `CenterOffsetConstraint`, `CenterOffsetSelfRel`, `CenterListConstraint`, `CenteredArrayConstraint` |
| **Matching** | `MatchSizeConstraint`, `FollowConstraint`, `RelativeFollowConstraint`, `FollowTextXConstraint` |
| **Fill** | `FillConstraint`, `FillToTextX` |
| **Ratio** | `RatioConstraint`, `RatioOtherConstraint` |
| **Text-driven** | `TextHeightConstraint`, `PreTextConstraint`, `FollowTextXConstraint` |
| **Array/list** | `ScalingArrayConstraint`, `RelScalingArrayConstraint`, `CenterListConstraint` |
| **Special** | `BestFitConstraint` (aspect-fit), `AspectFitConstraint`, `MouseFollowConstraint`, `WrapConstraint`, `CustomConstraint`, `DefaultScale` |
| **Other** | `BetweenConstraint`, `PrecedeConstraint`, `CenterOnPxConstraint`, `CenterOnRelConstraint`, `CenterOnOtherPxConstraint`, `RelOtherMaxConstraint` |
| **Abstract base** | `AbstractRelativeConstraint` |

#### `ConstraintUtils`
Factory methods: `fill()`, `fill(padding)`, `getRelative(x,y,w,h)`, `getPixel(...)`, `centered(w,h)`, `scaleToFit(aspect)`, `scaleToFitWithLimitedAspect(maxW2H, maxH2W)`, `getCenteredPos()`, `centeredRelSquare(relWidth)`.

---

### 9.4 `transitions` — Animation System

#### `Animator`
Per-component animator that manages multiple concurrent `Animation` instances (one per `AnimationBlueprint`). Accumulates offset values (x, y, width, height, alpha) from all active animations, then calls `notifyDimensionChange()` or `notifyTotalAlphaChange()` if any changed.

#### `AnimationBlueprint` (abstract)
Factory for `Animation` instances. `createInstance(oldAnim, reverse, delay)`.

#### `Animation` (abstract)
One running animation instance. `update(delta, Animator)` — calls `applyX/Y/Width/Height/Alpha` on the `Animator`. `shouldBeRemoved()` when finished.

#### `Transition` / `TransitionBlueprint`
An animation that runs once (display or undisplay). Created by `UiDisplayer`.

#### `Effect` / `EffectBlueprint`
A looping or triggered animation effect (e.g. pulse, wave). `stop()` cancels the effect.

**Blueprint prefabs:**

| Class | Behaviour |
|-------|-----------|
| `EaseDriverBlueprint` / `EaseDriver` | Smooth ease-in/out based on `EasingFunction` |
| `SlideDriverBlueprint` | Slides a component in/out from an edge |
| `BounceDriverBlueprint` | Spring-bounce animation |
| `SinDriverBlueprint` | Continuous sine-wave oscillation |
| `WaveDriverBlueprint` | Wave-based oscillation |
| `ValueDriverBlueprint` | Drives from toolbox `ValueDriver` |

#### `EasingFunction`
Enum of easing types: `LINEAR`, `EASE_IN`, `EASE_OUT`, `EASE_IN_OUT`, `BACK_OUT`, etc.

---

### 9.5 `text` — Font Rendering

#### `Font`
Loaded font metadata + texture atlas reference.

#### `Text` / `TextBuilder`
A `UiComponent` wrapping rendered text. `TextBuilder` sets content, font, size, colour, alignment, line wrapping.

#### `Align`
Enum: `LEFT`, `CENTER`, `RIGHT`.

#### Font loading pipeline:

| Class | Role |
|-------|------|
| `FontLoader` | Reads `.png` atlas + `.fnt` meta file |
| `MetaDataLoader` | Parses AngelCode bitmap font `.fnt` format |
| `Character` | Per-glyph bounds: x, y, w, h in atlas coords + advance |
| `Word` | A sequence of `Character`s |
| `Line` | A sequence of `Word`s with max-width wrapping |
| `TextStructureGenerator` | Breaks raw string into `Line`s respecting wrap width |
| `TextMeshGenerator` | Converts `Line`s into vertex positions + UVs |
| `TextGenerator` | Orchestrates generation and uploads to a `TextMesh` |

#### `TextMesh`
A VAO containing position and UV data for one rendered string. Updated when text changes.

#### `FontRenderer` / `FontShader`
Renders all `TextMesh` objects in one pass. Shader: `fontVertex/Fragment.glsl`. Uses SDF or bitmap rendering depending on font format.

---

### 9.6 `uiRendering`

#### `UiRenderer` / `UiShader`
Renders all `UiBlock` objects (coloured rectangles with corner radius and outline). Batches by render level. Shader: `uiVertex/Fragment.glsl`.

---

### 9.7 `uiResources`

#### `UiStyle`
A complete visual style definition with 30+ `Colour` fields and several dimension fields (`fontSize`, `cornerRadius`, `bigCornerRadius`, etc.). All values stored in a `DataObject` for hot-loading.

#### `UiStyleConfigs`
Mutable POJO — set values before `Ui.loadResources()`.

#### `UiResources`
Holds the loaded `UiStyle`, font repository, and texture repository.

#### `UiResourceManager`
Loads repositories from disk; optionally starts a `ValueSheetHotLoader`.

#### `ValueSheet` / `ValueSheetRepositoryLoader` / `ValueSheetHotLoader`
Hot-loadable JSON/tag-format sheets of named float/colour values. Components can subscribe to `ValueSheet` values so they update at runtime without restarting.

#### `FontRepositoryLoader` / `UiTextureRepositoryLoader`
Scan the `fonts/` and `GUIs/` folders and populate `HashRegistry<Font>` and `HashRegistry<Texture>`.

---

### 9.8 `gardenUiPrefabs` — Pre-built Widgets

**Buttons:**

| Class | Description |
|-------|-------------|
| `BasicButtonUi` | Base button with hover/press states |
| `BasicTextButtonUi` | Button with centred text label |
| `RectangleButtonUi` | Rectangular background |
| `CircleButtonUi` | Circular background |
| `IconRectangleButtonUi` | Icon + rectangle |
| `RoundIconButtonUi` | Circular icon button |
| `TextColourButtonUi` | Button that colours text on hover |
| `ColourButtonUi` | Solid colour-fill button |
| `LayerTextureButtonUi` | Multi-layer texture button (idle/hover/press) |
| `TextRectangleButtonUi` | Text + outline rectangle |

**Sliders:**

| Class | Description |
|-------|-------------|
| `SliderUi` | Float slider with draggable marker |
| `IntSliderUi` | Integer-valued slider |
| `SliderMarkerUi` | The draggable thumb |

**Stat Bars:** `StatBarUi`, `PercentStatBarUi`, `CountStatBarUi`, `TextStatBarUi`, `IconStatBarUi` — all display a fill ratio with optional icon, text, or count. `StatBarUpdater` / `CountStatBarUpdater` drive them from game data.

**Text Input:** `TextFieldUi` (single-line text), `NumberFieldUi`, `TextEditor` (multi-line). `CharFilter` / `NumberFilter` / `TextFilter` validate input.

**Scroll Panel:** `ScrollPanelUi` with `ScrollBarUi` + `BarUi` for the thumb. Clips children to the panel bounds.

**Spinner:** `SpinnerUi` (left/right cycle through values) + `NamedSpinnerUi`.

**Named Panel:** `NamedPanelUi` with `NameBannerUi` for a titled container.

**Pop-up:** `PopUp3dUi` — a world-space anchored pop-up with a 3D anchor point. `NamedPopUpUi` adds a title banner.

**Tooltips:** `ToolTipUi` + `ToolTipUpdater` base. Prefabs: `PlainToolTipUi`, `SingleLineToolTipUi`, `TextToolTipUi`.

**Utils:** `BorderPanelUi` (panel with an inset content area), `LayerTextureUi` (stacked texture layers), `EngineUiSounds` (hover/click sounds).

---

### 9.9 `components` — Interaction Components

| Class | Description |
|-------|-------------|
| `ClickableUi` | Adds click/hover callbacks to any component |
| `MouseListener` | More granular: `onEnter`, `onExit`, `onClick`, `onRelease`, `onHold` |
| `CheckBoxUi` | Boolean toggle with checked/unchecked textures |
| `CheckOptionUi` | Radio-button style option |
| `TogglableUi` | Two-state toggle |
| `ToggleGroup` | Ensures only one `TogglableUi` active at a time |
| `EmptyUi` | Invisible spacer component |
| `DebugUi` / `DebugDataUi` / `DebugSizeUi` | Debug overlays |
| `ToolTipUi` / `ToolTipUpdater` | Tooltip display with hover delay |
| `DragClickChecker` / `DragClickDetector` | Distinguishes drag from click |
| `ElementGridUi` | Grid of equal-sized elements |
| `EventData` | Value object for mouse event data |

---

### 9.10 `grids` — Grid Layouts

| Class | Description |
|-------|-------------|
| `GridLayout` | Fixed columns, auto-calculated rows |
| `SimpleGridLayout` | Minimal implementation |
| `CenteredGridLayout` | Centres the grid horizontally |
| `CentralGridLayout` | Centres in both axes |
| `LeftGridLayout` | Left-aligned |
| `ScalingGridLayout` | Items scale to fill available space |
| `IGridLayout` | Interface |

---

### 9.11 `customCursor`

#### `CursorManager`
Created at `Ui.init()`. Allows registering custom cursors and switching between them. Uses GLFW standard and custom cursor shapes.

#### `Cursor` / `CursorLoader`
Loads a cursor from a PNG file at a specified hot-spot.

---

### 9.12 `layout`

#### `BaseLayout`
Manages dynamic positioning of children within a parent. Registered with `UiComponent.registerLayout()`. Responds to child add/remove via `initializeLayout()`. Subclasses implement their own positioning logic.

#### `ValueSheet`
A shareable sheet of named values (`float`, `Colour`) loaded from disk and optionally hot-reloaded. Components query values by `HashId`.

---

## 10 · `features` — Gameplay Systems

### 10.1 `behaviours` — Action / Behaviour Tree

#### `Action` (abstract)
Base node with `Status` state machine (`UNSTARTED → RUNNING → PASSED / FAILED`). Implements `Exportable` for save/load.

```java
abstract void update(float delta);
void init();       // transitions to RUNNING
void resume();     // transitions to PASSED (for interrupted actions)
void markPaused(boolean);
```

#### `Status`
Enum: `UNSTARTED`, `RUNNING`, `PASSED`, `FAILED`. `isComplete()` = `PASSED || FAILED`.

#### `ActionManager`
An `ArrayDeque<Action>` stack for one entity. Supports:
- `setAction(action)` — replaces everything
- `interrupt(action, startRotation)` — pushes a `TransitionAction` to smooth the turn, then the interrupting action, then pauses the current action
- `update(delta)` — pops completed actions, inits new top, calls `update()`

**Standard node types:**

| Class | Description |
|-------|-------------|
| `SequenceAction` | Runs children in order; fails if any child fails |
| `SelectorAction` | Tries children until one passes |
| `RandomSequenceAction` | Runs children in random order |
| `LoopAction` | Repeats a sequence N times |
| `EndlessLoopAction` | Repeats forever |
| `TimedAction` | Marks passed after N seconds |
| `MultiTimedAction` | Multiple phases with different durations |
| `WaitAction` | Pause for a fixed duration |
| `WaitRandom` | Pause for a random duration within a range |
| `TransitionAction` | Smoothly rotates entity to a target bearing (used by `ActionManager.interrupt()`) |
| `FailCondition` | Wraps an action; inverts failure/pass |
| `CompositeAction` | Base composite; manages a child list |

**New composites (newer API):**

| Class | Description |
|-------|-------------|
| `NewCompositeAction` | Cleaner base for composites |
| `NewSequenceAction` | Sequence with proper `RUNNING` propagation |
| `NewSelectorAction` | Selector with proper `RUNNING` propagation |
| `ConditionNode` | Wraps a `BooleanSupplier`; passes if true |
| `RandomChoiceNode` | Randomly selects and runs one child |

---

### 10.2 `debugSystem`

#### `EngineDebug`
Container for engine debug data fields (populated in `Engine.update()`):
- `fps` (`FloatData`) — rolling average FPS
- `dynamicEntities` (`CountData`) — visible vs total
- `entityTris` (`CountTotalData`) — total tris rendered

#### Data types:
- `FloatData` — smoothed float value
- `CountData` — visible count + total count per frame
- `CountDisplayData` — text formatter for count data
- `CountTotalData` — accumulated total

---

### 10.3 `debugger`

#### `Debugger`
Global static debug facility (enabled by passing a `DebugFormat` to `Debugger.init()`):
- Frame counters + per-second counters via `RollingAverageCounter`
- `report(key)` — increments a named counter
- `toggleState(scene, stateId)` / `checkState(scene, stateId)` — per-scene boolean flags
- `addListener(scene, stateId, DebugListener)` — triggered on toggle

#### `DebugFormat` (interface)
`void initializeDebugger()` — registers all counters. `Map<String,String> getInfo()` — formatted debug output for display.

---

### 10.4 `frustumCulling`

#### `CameraFrustum`
Updated each frame by `GameCamera.update()`. Wraps a `Frustum` (6 `Plane`s) and exposes:
- `containsSphere(center, radius)` — quick reject (all-or-nothing)
- `testSphere(center, radius)` → `FrustumResult` (IN / PARTIAL / OUT)
- `testAabb(mins, maxs)` → `FrustumResult` — uses closest/furthest-point algorithm per plane

#### `FrustumCreator`
Extracts the 6 planes from the camera's projection-view matrix.

#### `Plane`
`normal (Vector3f)` + `d (float)`. `getSignedDistance(point)` = dot(normal, point) + d.

---

### 10.5 `movement`

#### `Steerer3d`
Controls a 3D entity's rotation towards a target bearing using configurable angular speed and momentum.

#### `Steering`
Stateless helper calculating the required angular delta towards a target.

#### `PathFollower3d`
Follows a list of waypoints using `Steerer3d`. Advances to the next waypoint when within arrival radius.

#### `MoveAnimation` (interface)
```java
void update(float delta, float speed, Vector3f position, float rotation);
boolean isActive();
```
Applied by the movement system for visual movement enhancement.

#### `BouncyWalkAnimation`
Implements `MoveAnimation` — adds a vertical bounce proportional to speed.

---

## 11 · `resourceManagement` — Resources, Save, Lang

### 11.1 `requestProcessing`

#### `BackgroundLoader`
Thread-safe two-queue system for non-GL and GL work:

| Method | Thread | Description |
|--------|--------|-------------|
| `addGeneralRequest(Request)` | Any | Queued to background thread (or immediate if on main thread) |
| `addOpenGlRequest(Request)` | Any | Queued to main thread (or immediate if already on GL thread) |
| `doTopGlRequests()` | Main | Process a few GL requests per frame |
| `completeAllRequests()` | Main | Block until all requests done |
| `isDoneProcessing()` | Any | True when both queues empty |
| `cleanUp()` | Main | Drain + kill background thread |

#### `Request` (interface)
`void execute()` — the unit of deferred work.

#### `GeneralRequestProcessor` / `GlRequestProcessor`
Internal queue processors. `GeneralRequestProcessor` runs on a daemon thread; `GlRequestProcessor` is drained by the main loop.

---

### 11.2 `saveSystem`

#### `SaveSystem`
Manages a folder of `.dat` save files.

| Method | Description |
|--------|-------------|
| `init(savesFolder, version, gameVersion)` | Scans folder, loads existing saves |
| `createNewSave(name)` | Creates a new `SaveGame` with a random ID |
| `getListOfSaves()` | Returns saves sorted by last-played date |
| `getMostRecentSave()` | Convenience for quick-load |
| `deleteSave(save)` | Deletes file + removes from list |
| `hasSavesAvailable()` | `!saves.isEmpty()` |

Save file naming convention: `{id}_SAVE_{date}_{time}_{name}.dat`  
Temp files: `{id}_TEMP_...dat` — written during saving to avoid corruption.

#### `SaveGame`
Wraps one save file. `load(file, saveSystem)` reads metadata. `createSavingProcess()` starts a `SavingProcess` which writes data atomically via a temp file.

#### `SavingProcess`
Writes game state to a temp `.dat` file using the toolbox `Writer`. On completion, renames the temp file to the real save file name (atomic swap).

#### `MetaData`
Read from the file header: save name, date, game version. Used to show the save list without reading the full file.

#### `SaveFileFinder`
Scans the saves folder, ignoring temp files and corrupt entries.

---

### 11.3 `languageSystem`

#### `GameText`
Static localisation facade. `init(locale, mods)` loads CSV files from `res/lang/{locale}.csv` for each mod. Falls back to `en.csv`.

```java
GameText.get("item.carrot.name")    // → "Carrot"
GameText.getComplex("ui.tooltip")   // → ComplexString (supports formatting)
```

#### `LangRepository`
`HashRegistry<String>` for simple strings + `HashRegistry<ComplexString>` for formatted ones.

#### `LangRepositoryLoader`
Reads CSV (key, value) rows. Supports multiple mods and locale fallback.

#### `ComplexString`
A string with placeholder slots (e.g. `"You have {0} carrots"`) that can be filled at runtime.

---

### 11.4 `certificates`

#### `Certificate`
An encrypted file recording a set of unlocked `Id`s (achievements, found items, etc.).

| Method | Description |
|--------|-------------|
| `unlockId(id)` | Returns `true` if newly unlocked (not already in set) |
| `getIds()` | Full set of unlocked IDs |
| `save()` | Writes the encrypted file |

#### `CertificateCreator`
Loads or creates a certificate file. Uses `Encoder` for XOR-based encryption.

#### `Encoder`
Simple XOR encoding using a key derived from the certificate type.

---

## 12 · `postProcessing` — Post-processing

#### `PostProcessingFilter` (abstract)
Base class for screen-space effects. Renders using `FullScreenQuad` + a custom fragment shader.

Subclasses implement their own `ShaderProgram` and call `renderQuad()` with a source texture.

**Provided GLSL vertices:**
- `basicVertex.glsl` — standard full-screen quad pass-through
- `basicVertexFlip.glsl` — flipped Y version (for FBO blit differences)

Games extend `PostProcessingFilter` for blur, bloom, colour correction, etc.

---

## 13 · `utils` — Engine Utilities

#### `EngineUtils`
General static utility methods used across the engine.

#### `TextureExporter`
Reads an FBO texture back from the GPU (`glReadPixels`) and saves it to a PNG file. Used for screenshot capture or shadow map debugging.

#### Container types:

| Class | Description |
|-------|-------------|
| `Container<T>` | Mutable single-value holder |
| `FloatContainer` | Primitive float holder (avoids boxing) |
| `IntContainer` | Primitive int holder |

These are used across the engine when a lambda or callback needs to mutate a captured value.

---

## Cross-Cutting Design Patterns

| Pattern | Where used |
|---------|-----------|
| **Singleton** | `Engine`, `AudioMaster`, `ParticleMaster`, `Ui`, `Debugger` |
| **Builder** | `Window`, `Fbo`, `Texture`, `Sound2d/3d`, `SliderUi`, `Text` |
| **Strategy** | `UiScalingAlgorithm`, `ByteFormat`, `PitchProvider`, `SoundProvider`, `EasingFunction` |
| **Component (ECS-style)** | Particle effect system (`ParticleEffectComponent[]` per emitter) |
| **Template Method** | `ShaderProgram.initVariables()`, `GameCamera.move()`, `SplashScreen.isReadyForLoading()`, `UiComponent.init()` / `updateSelf()` |
| **Observer** | `WindowSizeListener`, `DebugListener`, `BaseLayout` change listeners |
| **Command / Request** | `Request` interface in `BackgroundLoader` |
| **Object Pool** | `SourcePool` (AL sources), toolbox `Vec3Pool`, `Vec2Pool`, `Vec4Pool` |
| **Dirty Flag** | `Camera` matrices (recomputed only on change) |
| **Lazy Init** | `UiComponent.animator`, shader `Uniforms` |
| **Composite** | `UiComponent` (tree of children), `CompoundSound`, `CompoundParticleEffect`, `SequenceAction` |
| **Null Object** | `EmptyAudioMaster`, `EmptyState`, `EmptyPlaythrough` |
| **Factory Method** | `EngineCreator.init()`, `ParticleMaster.init()`, `ShadowMaster.init()` |
| **Two-phase init** | `EngineCreator`: essential systems → splash → full systems |
| **Atomic file write** | `SavingProcess`: write temp → rename |

