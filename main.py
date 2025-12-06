from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Hello, world!", self)
        self.initialization()


    def initialization(self):
        self.setWindowTitle("Hello")
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.setStyleSheet("""
            QLabel#label {
                font-size: 40px;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    win.resize(400, 600)
    sys.exit(app.exec_())
