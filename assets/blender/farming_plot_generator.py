"""
Blender script: Farming Plot generator for SuperStoreTycoon.

Creates a low-poly modular farming plot kit aligned to the game's tile system.
Tile convention:
    - 1 Blender unit = 1 game grid tile.
    - Supports 1x1, 2x2, 3x3, and 4x4 farming plots (Section 39 asset list).

How to use:
    1) Open Blender.
    2) Scripting tab -> open this file.
    3) Run script.
    4) Export selected collection as FBX/GLB if needed.
"""

import bpy

COLLECTION_NAME = "MLP_FarmingPlot_Kit"


def clear_collection(name: str) -> bpy.types.Collection:
    """Create collection if needed and remove old generated meshes."""
    scene = bpy.context.scene
    collection = bpy.data.collections.get(name)
    if collection is None:
        collection = bpy.data.collections.new(name)
        scene.collection.children.link(collection)

    for obj in list(collection.objects):
        bpy.data.objects.remove(obj, do_unlink=True)

    return collection


def ensure_materials():
    """Create / fetch reusable materials."""
    def mat(name, color):
        material = bpy.data.materials.get(name)
        if material is None:
            material = bpy.data.materials.new(name=name)
            material.use_nodes = True
            bsdf = material.node_tree.nodes.get("Principled BSDF")
            bsdf.inputs["Base Color"].default_value = color
            bsdf.inputs["Roughness"].default_value = 0.95
        return material

    soil = mat("MLP_Soil", (0.18, 0.09, 0.05, 1.0))
    ridge = mat("MLP_Soil_Ridge", (0.25, 0.13, 0.07, 1.0))
    border = mat("MLP_Plot_Border", (0.40, 0.28, 0.18, 1.0))
    return soil, ridge, border


def create_base_plot(size: int, collection: bpy.types.Collection, materials):
    """Create one plot object for a given NxN footprint."""
    soil_mat, ridge_mat, border_mat = materials
    offset_x = (size - 1) * 5.0

    # Outer border slab
    bpy.ops.mesh.primitive_cube_add(size=1, location=(offset_x, 0, 0.05))
    border_obj = bpy.context.active_object
    border_obj.name = f"FarmingPlot_{size}x{size}_Border"
    border_obj.scale = (size * 0.5, size * 0.5, 0.05)
    border_obj.data.materials.append(border_mat)
    collection.objects.link(border_obj)
    bpy.context.scene.collection.objects.unlink(border_obj)

    # Tilled soil surface
    bpy.ops.mesh.primitive_plane_add(size=size * 0.9, location=(offset_x, 0, 0.11))
    soil_obj = bpy.context.active_object
    soil_obj.name = f"FarmingPlot_{size}x{size}_Soil"
    soil_obj.data.materials.append(soil_mat)
    collection.objects.link(soil_obj)
    bpy.context.scene.collection.objects.unlink(soil_obj)

    # Furrow ridges
    ridge_count = max(2, size + 1)
    spacing = (size * 0.85) / (ridge_count - 1)
    start = -((ridge_count - 1) * spacing) / 2
    for i in range(ridge_count):
        ridge_y = start + i * spacing
        bpy.ops.mesh.primitive_cube_add(size=1, location=(offset_x, ridge_y, 0.13))
        ridge_obj = bpy.context.active_object
        ridge_obj.name = f"FarmingPlot_{size}x{size}_Ridge_{i+1:02d}"
        ridge_obj.scale = (size * 0.42, 0.04, 0.03)
        ridge_obj.data.materials.append(ridge_mat)
        collection.objects.link(ridge_obj)
        bpy.context.scene.collection.objects.unlink(ridge_obj)


def build_farming_plot_kit():
    collection = clear_collection(COLLECTION_NAME)
    materials = ensure_materials()

    for size in (1, 2, 3, 4):
        create_base_plot(size=size, collection=collection, materials=materials)

    print("SuperStoreTycoon farming plot kit generated: 1x1, 2x2, 3x3, 4x4")


if __name__ == "__main__":
    build_farming_plot_kit()
