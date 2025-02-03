from control_panel import ControlPanel
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('AutoShorts')
        self.setObjectName('MainWindow')
        #self.setWindowIcon(path)
        self.setMinimumSize(900, 700)
        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        self.layout = QGridLayout()
        central_widget.setLayout(self.layout)
        central_widget.setContentsMargins(0, 0, 0, 0)
        
        self.control_panel = ControlPanel()
        self.layout.addWidget(self.control_panel, 0, 0, 1, 1)

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