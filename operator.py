import bpy
from . Window import Window
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
import sys

class DragnDropOperator(bpy.types.Operator):
    '''
    This modal operator is used to start the pyqt5 window.
    the variable self.timer is used to refresh the pyqt5 window
    based on a timer handled by blender's window manager.
    '''

    bl_idname = "wm.drag_n_drop"
    bl_label = "Operator to start a Drag and Drop window"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def modal(self, context, event):
        # This function runs in background in blender has long as 
        # the operator is alive
        # process pyqt5 events
        if event.type == 'TIMER':
            self.event_loop.processEvents()
            self.Qt_application.sendPostedEvents(None, 0)
        return {'PASS_THROUGH'}

    def execute(self, context):
        self.Qt_application = QApplication.instance()
        if self.Qt_application is None:
            self.Qt_application = QApplication(['blender'])
        self.event_loop = QtCore.QEventLoop()
        self.window = Window()
        
        # Register operator as modal
        self.timer = context.window_manager.event_timer_add(0.1, window=context.window)

        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}


        # Old code
        # # app = QApplication(sys.argv)
        # window = Window()   
        # window.show()
        # app.exec()
        # context.window_manager.modal_handler_add(self)
        