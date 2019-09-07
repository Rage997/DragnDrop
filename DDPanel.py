import bpy
from . Window import MainWidget

class DragDropPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_DragDropPanel"
    bl_label = "DragnDrop Panel"
    bl_category = "DragnDrop"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text='Test')
        row.operator("file.drag_n_drop", text='dio')

    
