import bpy
import math
import json
import os
import sys

try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    script_dir = os.path.dirname(bpy.data.filepath) if bpy.data.filepath else "."

path_to_config = os.path.join(script_dir, "config.json")

def load_ai_params(path):
    if not os.path.exists(path):
        print(f"ERROR: Config file not found at: {path}")
        return {
            "design_params": {
                "nodes": 20, 
                "main_radius": 5, 
                "element_size": 1, 
                "twist_count": 3
            },
            "project_name": "AurumBit_Fallback"
        }
        
    with open(path, 'r') as f:
        return json.load(f)

def create_aurumbit_from_ai():
    data = load_ai_params(path_to_config)
    params = data['design_params']
    
    if bpy.context.scene:
        bpy.ops.object.select_all(action='SELECT')
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

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    bpy.context.object.name = data['project_name']

if __name__ == "__main__":
    create_aurumbit_from_ai()