from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtMultimedia import QMediaPlayer
from control_widgets import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class ProgressBar(QWidget):
    pass

class MediaPlayer(QWidget):
    def __init__(self, media_panel, parent=None):
        super().__init__(parent)
        self.setObjectName("MediaPlayer")
        self.media_panel = media_panel
        self.super_layout = QVBoxLayout()
        self.control_layout = QHBoxLayout()
        self.control_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.video_file = None
        self.audio_file = None
        
        self.qmedia_player = QMediaPlayer(self)
        self.video_widget = QVideoWidget(self)
        self.qmedia_player.setVideoOutput(self.video_widget)
        
        # Play-Pause button
        self.pback_button = QPushButton()
        self.pback_button.setObjectName("PlayPause")
        self.pback_button.setFixedSize(32, 32)
        self.pback_icons = [QIcon("Images/play-button.png"), QIcon("Images/pause-button.png")]
        self.paused = True
        self.pback_button.setIcon(self.pback_icons[0])
        self.pback_button.setIconSize(QSize(14, 14))
        self.pback_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.pback_button.clicked.connect(lambda: self.pback_action())
        
        self.control_layout.addWidget(self.pback_button)
        self.super_layout.addWidget(self.video_widget)
        self.super_layout.addLayout(self.control_layout)
        self.setLayout(self.super_layout)
        
    def pback_action(self):
        self.paused = not self.paused
        if not self.paused:
            self.qmedia_player.play()
            self.pback_button.setIcon(self.pback_icons[1]) # Playing
        else:
            self.qmedia_player.pause()
            self.pback_button.setIcon(self.pback_icons[0]) # Paused
            
    def update_media(self, video_file, audio_file):
        if video_file:
            self.video_file = video_file
            self.qmedia_player.setSource(QUrl.fromLocalFile(video_file))
        if audio_file:
            self.audio_file = audio_file
        
        
class Timeline():
    pass
        