from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class DragDrop(QWidget):
    def __init__(self, parent=None, icon=None):
        super().__init__(parent)
        self.setObjectName("DragDrop")
        self.setAcceptDrops(True)
        self.setFixedHeight(84)

        self.layout = QGridLayout(self)
        pixmap = QPixmap(icon)
        self.label = QLabel()
        self.label.setPixmap(pixmap)
        self.label.setFixedSize(25, 25)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(self.label)
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
        self.setObjectName("FileDialog")
        self.VALID_EXTENSION = ('.mp4', '.mov') if expected=="video" else ('.mp3', 'wav')
        self.PROMPT = f"Select {expected} file"
        self.TIP = f"{expected.capitalize()} files ({" *".join(self.VALID_EXTENSION)})"
        self.setFixedHeight(84)
        self.setIcon(QIcon(icon))
        self.setIconSize(QSize(20, 20))
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.clicked.connect(lambda: self.open_dialog())

    def open_dialog(self):
        dialog = QFileDialog.getOpenFileName(self, self.PROMPT, r'', self.TIP)
        if dialog:
            file_name = dialog
            if file_name[0].endswith(self.VALID_EXTENSION):
                self.parent.asc_file = file_name
            else:
                pass

class ControlGroup(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("ControlGroup")
        self.asc_file = None
        self.layout = QHBoxLayout()
        self.setFixedHeight(104)
        self.setLayout(self.layout)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

    def add_children(self, children):
        for child in children:
            self.layout.addWidget(child)

class TextField(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("TextField")
        self.layout = QVBoxLayout()

        field = QTextEdit()
        field.setObjectName("TextFieldInner")
        field.setPlaceholderText("Text here: ")
        field.setCursorWidth(6)

        self.layout.addWidget(field)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setLayout(self.layout)