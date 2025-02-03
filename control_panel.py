from control_widgets import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class ControlPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("ControlPanel")
        self.layout = QGridLayout()
        self.layout.setSpacing(10)
        self.setContentsMargins(0, 0, 0, 0)
        self.populate()
        self.setLayout(self.layout)
        self.setMaximumWidth(300)
        
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
    def populate(self):

        # VIDEO CONTROLS
        v_group = ControlGroup()
        v_dialog = FileDialog(icon="Images/folder.png", expected="video")
        v_drag = DragDrop(icon="Images/upload-arrow.png")
        v_group.add_children([v_dialog, v_drag])
        
        # AUDIO CONTROLS
        a_group = ControlGroup()
        a_dialog = FileDialog(icon="Images/folder.png", expected="audio")
        a_drag = DragDrop(icon="Images/upload-arrow.png")
        a_group.add_children([a_dialog, a_drag])
        
        # TEXT INPUT
        textfield = TextField()
        
        self.layout.addWidget(v_group, 1, 1, 1, 1)
        self.layout.addWidget(a_group, 2, 1, 1, 1)
        self.layout.addWidget(textfield, 3, 1, 5, 1)
