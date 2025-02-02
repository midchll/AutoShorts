from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        layout = QGridLayout()
        
        self.setWindowTitle('AutoShorts')
        self.setObjectName('MainWindow')
        #self.setWindowIcon(path)
        self.setMinimumSize(900, 700)
        
        # Add widgets to layout (.addWidget())
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    def load_stylesheet(filename):
        pass

    app = QApplication(sys.argv)
    #app.setStyleSheet(load_stylesheet('styles.qss'))
    window = MainWindow()
    window.show()

    sys.exit(app.exec())