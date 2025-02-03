import PyQt6
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class DragDrop(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("dragDrop")
        self.setMinimumSize(60, 60)
        self.setAcceptDrops(True)
        
        self.layout = QGridLayout(self)
        self.label = QLabel("DRAG", self)
        self.label.setObjectName("dragDropLabel")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.layout.addWidget(self.label, 0, 0, 1, 1)
        
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setLayout(self.layout)
        
    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
    
    #TODO: separate video/audio(txt) file submissions using expected type param
    def dropEvent(self, event: QDropEvent):
        urls = event.mimeData().urls()
        for url in urls:
            file_path = url.toLocalFile()
            self.add_file(file_path)
            
class FileDialog(QPushButton):
    def __init__(self, parent=None, icon=None, expected=None):
        super().__init__(parent)
        self.setObjectName("fileDialog")
        self.VALID_EXTENSION = ('.mp4', '.mov') if expected=="video" else ('.mp3', 'wav')
        self.PROMPT = f"Select {expected} file"
        self.TIP = f"{expected.capitalize()} files ({" *".join(self.VALID_EXTENSION)})"
        self.associated_file = None
        self.setMinimumSize(60, 60)
        self.setMaximumHeight(100)
        self.setIcon(QIcon(icon))
        self.setIconSize(QSize(20, 20))
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.clicked.connect(lambda: self.open_dialog())
    
    def open_dialog(self):
        dialog = QFileDialog.getOpenFileName(self, self.PROMPT, r'C:\\', self.TIP)
        if dialog:
            file_name = dialog
            if file_name[0].endswith(self.VALID_EXTENSION):
                self.associated_file = file_name
            else:
                pass
        
class ControlGroup(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("controlGroup")
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        
        self.setMinimumSize(200, 100)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
    def add_children(self, children):
        for child in children:
            self.layout.addWidget(child)

class TextField(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("textField")
        self.layout = QVBoxLayout()
        
        field = QTextEdit()
        field.setObjectName("textFieldInner")
        field.setPlaceholderText("Text here: ")
        field.setCursorWidth(6)
                
        self.layout.addWidget(field)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setLayout(self.layout)