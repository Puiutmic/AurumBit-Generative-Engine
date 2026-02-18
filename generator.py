import bpy
import math
import json
import os
import sys

def get_config_path():
    try:
        base_path = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        try:
            if bpy.data.filepath:
                base_path = os.path.dirname(bpy.data.filepath)
            else:
                print("WARNING: Fisierul .blend nu este salvat! Folosesc calea default.")
                base_path = "."
        except:
            base_path = "."
            
    return os.path.join(base_path, "config.json")

path_to_config = get_config_path()
print(f"DEBUG: Config path detected at: {path_to_config}")

def load_ai_params(path):
    if not os.path.exists(path):
        print(f"ERROR: Config file not found at: {path}")
        return {
            "design_params": {
                "nodes": 30, 
                "main_radius": 4, 
                "element_size": 0.5, 
                "twist_count": 3
            },
            "project_name": "Fallback_Design"
        }
        
    with open(path, 'r') as f:
        return json.load(f)

def create_aurumbit_from_ai():
    data = load_ai_params(path_to_config)
    params = data['design_params']
    
    if bpy.context.scene:
        bpy.ops.object.select_all(action='DESELECT')
        
        objs_to_delete = [o for o in bpy.context.scene.objects if o.type == 'MESH']
        for o in objs_to_delete:
            o.select_set(True)
        bpy.ops.object.delete()

    for i in range(params['nodes']):
        angle = (i / params['nodes']) * math.pi * 2
        x = params['main_radius'] * math.cos(angle)
        y = params['main_radius'] * math.sin(angle)
        z = math.sin(angle * params['twist_count']) * 0.4
        
        bpy.ops.mesh.primitive_torus_add(
            location=(x, y, z),
            major_radius=params['element_size'],
            minor_radius=0.03,
            rotation=(0, angle, angle * params['twist_count'])
        )

    bpy.ops.object.select_all(action='DESELECT')
    mesh_objs = [o for o in bpy.context.scene.objects if o.type == 'MESH']
    for o in mesh_objs:
        o.select_set(True)
        
    if mesh_objs:
        bpy.context.view_layer.objects.active = mesh_objs[0]
        bpy.ops.object.join()
        bpy.context.object.name = data['project_name']

if __name__ == "__main__":
    create_aurumbit_from_ai()