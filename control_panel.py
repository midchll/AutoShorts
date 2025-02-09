from control_widgets import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class ControlPanel(QWidget):
    file_selected = pyqtSignal()
    
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.setObjectName("ControlPanel")
        self.main_window = main_window
        self.layout = QGridLayout()
        self.layout.setSpacing(10)
        self.setContentsMargins(0, 0, 0, 0)
        self.populate()
        self.setLayout(self.layout)
        self.setMaximumWidth(300)

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

    def populate(self):

        # VIDEO CONTROL GROUP
        v_group = ControlGroup()
        v_label = QLabel()
        v_label.setObjectName("VideoIndicator")
        v_label.setPixmap(QPixmap("Images/video-indicator.png"))
        v_label.setFixedSize(40, 83)
        v_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        v_dialog = FileDialog(v_group, icon="Images/folder.png", expected="video")
        v_drag = DragDrop(icon="Images/upload-arrow.png")
        
        v_dialog.file_selected.connect(self.update_video)
        v_drag.file_selected.connect(self.update_video)
        
        v_group.add_children([v_label, v_dialog, v_drag])

        # AUDIO CONTROL GROUP
        a_group = ControlGroup()
        a_label = QLabel()
        a_label.setObjectName("AudioIndicator")
        a_label.setPixmap(QPixmap("Images/audio-indicator.png"))
        a_label.setFixedSize(40, 83)
        a_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        a_dialog = FileDialog(a_group, icon="Images/folder.png", expected="audio")
        a_drag = DragDrop(icon="Images/upload-arrow.png")
        
        a_dialog.file_selected.connect(self.update_audio)
        a_drag.file_selected.connect(self.update_audio)
        
        a_group.add_children([a_label, a_dialog, a_drag])

        # TEXT INPUT
        textfield = TextField()

        self.layout.addWidget(v_group, 1, 1, 1, 1)
        self.layout.addWidget(a_group, 2, 1, 1, 1)
        self.layout.addWidget(textfield, 3, 1, 5, 1)
        
    def update_video(self, file_path):
        self.main_window.video_file = file_path
        print(f"Updating the video file with: {file_path}")
        self.file_selected.emit()
    
    def update_audio(self, file_path):
        self.main_window.audio_file = file_path
        print(f"Updating the audio file with: {file_path}")
        self.file_selected.emit() # Notify file selected through shared parent main window
