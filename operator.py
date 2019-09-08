import bpy
from . Window import MainWidget
from PyQt5.QtWidgets import QApplication
import sys

class DragnDropOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "file.drag_n_drop"
    bl_label = "Operator to start a Drag and Drop window"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        app = QApplication(sys.argv)
        window = MainWidget()   
        window.show()
        app.exec()
        return {'RUNNING_MODAL'}