from PyQt6.QtWidgets import *
from media_widgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class MediaPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Outerface")
        self.layout = QGridLayout()
        self.layout.setSpacing(10)
        self.setContentsMargins(0, 0, 0, 0)
        self.populate()
        self.setLayout(self.layout)
        
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
    def populate(self):
        
        media_player = MediaPlayer()
        
        self.layout.addWidget(media_player, 0, 0, 1, 1)