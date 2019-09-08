from PyQt5.QtWidgets import QApplication, QMainWindow
import bpy
import sys
import os

class MainWidget(QMainWindow):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.setWindowTitle("DragnDrop files")
        self.resize(480,480)
        self.setAcceptDrops(True)
        # self.start()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [(u.toLocalFile()) for u in event.mimeData().urls()]
        for f in files:
            self.load_file(f)

# Handling all formats in this function
    def load_file(self, f):
        filename, file_extension = os.path.splitext(f)
        file_extension = file_extension.split('.')[1]
        print(filename, file_extension) 
        if file_extension == 'obj':
            bpy.ops.import_scene.obj(filepath=f)
        elif file_extension == 'fbx':
            bpy.ops.import_scene.fbx(filepath=f)
        elif file_extension == 'dae':
            bpy.ops.wm.collada_import(filepath=f)
        elif file_extension == '3ds':
            bpy.ops.import_scene.x3d(filepath=f)
        elif file_extension == 'glb' or 'gltf':
            print('called')
            bpy.ops.import_scene.gltf(filepath=f)
        else:
            print('Unrecognized format!')
        