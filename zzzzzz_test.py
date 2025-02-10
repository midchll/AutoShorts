import sys
from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt

class SliderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slider App")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.slider = QSlider(Qt.Orientation.Horizontal)
        layout.addWidget(self.slider)

        self.label = QLabel("Slider Value: 0", self)
        layout.addWidget(self.label)

        self.slider.valueChanged.connect(self.update_label)

        self.setLayout(layout)

    def update_label(self):
        value = self.slider.value()
        self.label.setText(f"Slider Value: {value}")

def main():
    app = QApplication(sys.argv)
    window = SliderApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()