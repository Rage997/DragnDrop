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

register, unregister = bpy.utils.register_classes_factory(DragDropPanel)

def register():
    bpy.utils.register_class(DragDropPanel)


def unregister():
    bpy.utils.unregister_class(DragDropPanel)
