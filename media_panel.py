from PyQt6.QtWidgets import *
from media_widgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class MediaPanel(QWidget):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.setObjectName("MediaPanel")
        self.main_window = main_window
        self.layout = QGridLayout()
        self.layout.setSpacing(10)
        self.setContentsMargins(0, 0, 0, 0)
        self.populate()
        self.setLayout(self.layout)
        
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
    def populate(self):
        
        process_button = QPushButton()
        process_button.setObjectName("ProcessButton")
        process_button.setIcon(QIcon("Images/process-button.png"))
        process_button.setIconSize(QSize(90, 90))
        process_button.setFixedSize(83, 40)
        process_button.setCursor(Qt.CursorShape.PointingHandCursor)
        
        proc_group = QWidget()
        proc_group.setObjectName("ProcessGroup")
        proc_group_layout = QHBoxLayout()
        proc_group_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        proc_group_layout.addWidget(process_button)
        proc_group.setFixedHeight(60)
        proc_group.setLayout(proc_group_layout)
        proc_group.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        self.media_player = MediaPlayer(self)
                
        self.layout.addWidget(proc_group, 0, 0, 1, 1)
        self.layout.addWidget(self.media_player, 1, 0, 1, 1)
        
    def update_media(self):
        video = self.main_window.video_file
        audio = self.main_window.audio_file
        print(f"Updating media player with Video: {video}, Audio: {audio}")
        
        self.media_player.update_media(video, audio)