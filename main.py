from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("What's your name?", self)
        self.line = QLineEdit(self)
        self.button = QPushButton("Click Me", self)
        self.label2 = QLabel(self)
        self.initialization()


    def initialization(self):
        self.setWindowTitle("Hello")

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.line)
        vbox.addWidget(self.button)
        vbox.addWidget(self.label2)

        self.setLayout(vbox)
        self.label.setAlignment(Qt.AlignCenter)
        self.line.setAlignment(Qt.AlignCenter)
        self.label2.setAlignment(Qt.AlignCenter)

        self.label.setObjectName("label")
        self.line.setObjectName("line")
        self.button.setObjectName("button")
        self.label2.setObjectName("label2")

        self.setStyleSheet("""
            QLabel, QLineEdit, QPushButton {
                font-size: 40px;
            }
        """)

        self.button.clicked.connect(self.get_name)

    def get_name(self):
        name = self.line.text().strip()
        if name:
            self.label2.setText(f"Hello, {name}")
        else:
            self.label2.setText("Enter your name")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    # win.resize(400, 600)
    sys.exit(app.exec_())
