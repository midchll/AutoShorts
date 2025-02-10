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

        # Playback container
        self.pback_group = QWidget()
        self.pback_group.setObjectName("PlaybackGroup")
        self.pback_group.setFixedHeight(54)
        self.pback_group_layout = QHBoxLayout()
        self.pback_group_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

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

        # Video timeline
        self.timeline = QSlider(Qt.Orientation.Horizontal)
        self.timeline.setRange(0, 0)
        self.timeline.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.timeline.sliderMoved.connect(lambda: self.setVidPos(self.timeline.value()))

        self.qmedia_player.positionChanged.connect(lambda: self.setTimelinePos(self.qmedia_player.position()))

        self.pback_group_layout.addWidget(self.pback_button)
        self.pback_group_layout.addWidget(self.timeline)
        self.pback_group.setLayout(self.pback_group_layout)

        self.control_layout.addWidget(self.pback_group)
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
            self.qmedia_player.pause()
            self.qmedia_player.setPosition(0)
            self.qmedia_player.durationChanged.connect(lambda: self.setTimelineDur(self.qmedia_player.duration()))
        if audio_file:
            self.audio_file = audio_file

    def setTimelineDur(self, duration):
        self.timeline.setRange(0, duration)

    def setVidPos(self, value):
        self.qmedia_player.setPosition(value)

    def setTimelinePos(self, pos):
        self.timeline.setValue(pos)
        # Pause playback at video end
        if self.timeline.value() == self.qmedia_player.duration():
            self.pback_action()