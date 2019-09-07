import bpy

class DragDropPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_DragDropPanel"
    bl_label = "A panel"
    bl_category = "Test panel"
    bl_space_type = "FILE_BROWSER"
    bl_region_type = "UI"

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("view3d.cursor_center")

