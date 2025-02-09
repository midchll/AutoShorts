from PyQt6.QtWidgets import *
from control_panel import *
from PyQt6.QtCore import *
from media_panel import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('EasyMedia')
        self.setObjectName('MainWindow')
        self.setWindowIcon(QIcon("Images/placeholder.png"))
        self.setMinimumSize(900, 700)
        self.video_file = None
        self.audio_file = None

        self.central_widget = QWidget()
        self.central_widget.setContentsMargins(0, 0, 0, 0)
        self.layout = QGridLayout()

        self.control_panel = ControlPanel(main_window=self)
        self.media_panel = MediaPanel(main_window=self)
        
        self.layout.addWidget(self.control_panel, 0, 0, 1, 1)
        self.layout.addWidget(self.media_panel, 0, 1, 1, 3)
        
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
        
        self.control_panel.file_selected.connect(self.media_panel.update_media)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    stylesheet = QFile('styles.qss')
    stylesheet.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text)
    stream = QTextStream(stylesheet)
    styles = stream.readAll()
    app.setStyleSheet(styles)
    stylesheet.close()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())