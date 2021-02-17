> A Blender addon to allow drag'n drop of 3D files

Many 3D software support the 'drag and drop' to speed up the loading of 
3D files. Blender does not have such feature. This addon aims to add this
feature to Blender

## Status 

Currently there's no way in Blender 2.81 to detect a drag 'n drop event. This project created a pyqt5 application on top of Blender to overcome this problem. This solution is not a really good one, first for performance reasons and secondly for the integrability of a pyqt5 application inside Blender. 
