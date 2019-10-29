''' 
This addons allow the drag and dropping of 3D file format files into blender.
Right now (Blender 2.80) there's neither a "drag event" in the Blender GUI
or the possibility to extend the Blender GUI using PyQt5. 
This addon, creates an external PyQt5 allowing to load files in Blender
by dragging and dropping them into this window. 
'''

bl_info = {
    "name" : "DragnDrop",
    "author" : "Rage",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from . operator import DragnDropOperator

def register():
    bpy.utils.register_class(DragnDropOperator)

def unregister():
    bpy.utils.unregister_class(DragnDropOperator)
