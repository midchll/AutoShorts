from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class DragDrop(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setAcceptDrops(True)
        
        self.layout = QLayout(self)
        
        self.label = QLabel("+", self)
        self.label.setObjectName("dragDropLabel")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFixedSize(20, 20)
        self.label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.layout.addWidget(self.label)
        
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
        super().__init__()
        self.VALID_EXTENSION = ('.mp4', '.mov') if expected=="video" else ('.mp3', 'wav')
        self.PROMPT = f"Select {expected} file"
        self.TIP = f"{expected.capitalize()} files ({" *".join(self.VALID_EXTENSION)})"
        self.associated_file = None
        self.setFixedSize(20, 20)
        self.setIcon(QIcon(icon))
        self.setIconSize(QSize(10, 10))
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.clicked.connect(self.open_dialog())
    
    def open_dialog(self):
        self.associated_file, _ = QFileDialog.getOpenFileName(self, self.PROMPT, r'C:\\', ())
        
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.seFilter(QDir.Files)
        
        if dialog.exec_():
            file_name = dialog.selectedFiles()

            if file_name[0].endswith(self.VALID_EXTENSION):
                self.associated_file = file_name
            else:
                pass
        