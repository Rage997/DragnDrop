from PyQt5.QtWidgets import QApplication, QMainWindow
import bpy
import sys
import os

class MainWidget(QMainWindow):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.setWindowTitle("DragnDrop files")
        self.resize(720,480)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [(u.toLocalFile()) for u in event.mimeData().urls()]
        for f in files:
            print(f)
  
          
app = QApplication(sys.argv)            
window = MainWidget()
window.show()
