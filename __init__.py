# This addons allow the drag and dropping of 3D file format files into blender.

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
from . DDPanel import DragDropPanel
from . operator import DragnDropOperator

# classes = ("file.drag_n_drop")

# register, unregister = bpy.utils.register_classes_factory(classes)

def register():
    bpy.utils.register_class(DragDropPanel)
    bpy.utils.register_class(DragnDropOperator)
    # register()

def unregister():
    bpy.utils.unregister_class(DragDropPanel)
    bpy.utils.unregister_class(DragnDropOperator)
    # unregister()