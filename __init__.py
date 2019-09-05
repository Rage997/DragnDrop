# This addons allow the drag and dropping of 3D file format files into blender.


bl_info = {
    "name" : "DeepBlend",
    "author" : "Rage",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from . DDPanel import *

classes = (DD_PT_)

register, unregister = bpy.utils.register_classes_factory(classes)

def register():
    bpy.utils.register_class(DD_PT_)
    # bpy.types.Scene.dragndrop = bpy.props.PointerProperty(type=MyAddonProperties)

def unregister():
    bpy.utils.unregister_class(DD_PT_)
