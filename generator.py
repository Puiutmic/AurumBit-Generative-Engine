import bpy
import math
import json
import os
from pathlib import Path

def get_config_path():
    if bpy.data.is_saved:
        base_path = Path(bpy.data.filepath).parent
    else:
        try:
            base_path = Path(__file__).parent
        except NameError:
            base_path = Path.cwd()
    return str(base_path / "config.json")

def load_params(path):
    if not os.path.exists(path):
        return {
            "design_params": {"nodes": 60, "main_radius": 3.0, "element_size": 0.4, "twist_count": 4},
            "project_name": "AurumBit_Fallback"
        }
    with open(path, 'r') as f:
        return json.load(f)

def create_geometry():
    data = load_params(get_config_path())
    p = data['design_params']
    
    if bpy.context.scene:
        bpy.ops.object.select_all(action='DESELECT')
        for obj in [o for o in bpy.context.scene.objects if o.type == 'MESH']:
            obj.select_set(True)
        bpy.ops.object.delete()

    for i in range(p['nodes']):
        angle = (i / p['nodes']) * math.pi * 2
        x = p['main_radius'] * math.cos(angle)
        y = p['main_radius'] * math.sin(angle)
        z = math.sin(angle * p['twist_count']) * 0.4
        bpy.ops.mesh.primitive_torus_add(
            location=(x, y, z),
            major_radius=p['element_size'],
            minor_radius=0.03,
            rotation=(0, angle, angle * p['twist_count'])
        )

    bpy.ops.object.select_all(action='DESELECT')
    meshes = [o for o in bpy.context.scene.objects if o.type == 'MESH']
    for o in meshes: o.select_set(True)
    if meshes:
        bpy.context.view_layer.objects.active = meshes[0]
        bpy.ops.object.join()
        bpy.context.object.name = data['project_name']

if __name__ == "__main__":
    create_geometry()