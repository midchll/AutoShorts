from PyQt6.QtMultimediaWidgets import *
from control_widgets import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class ProgressBar(QWidget):
    pass

class MediaPlayer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("MediaPlayer")
        self.super_layout = QVBoxLayout()
        self.control_layout = QHBoxLayout()
        
        self.video_widget = QVideoWidget()
        
        self.play_button = PlayPause()
        
        self.control_layout.addWidget(self.play_button)
        
        self.super_layout.addWidget(self.video_widget)
        self.super_layout.addLayout(self.control_layout)
        self.setLayout(self.super_layout)
        
class PlayPause(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("PlayPause")
        self.setEnabled(False)
        self.setFixedSize(30, 30)
        self.icons = [QIcon("Images/play-button.png"), QIcon("Images/pause-button.png")]
        self.icon_index = 0
        self.setIcon(self.icons[self.icon_index])
        self.setIconSize(QSize(20, 20))
        self.clicked.connect(lambda: self.trigger())
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
    def trigger(self):
        self.icon_index -= 1
        self.setIcon(self.icons[self.icon_index])