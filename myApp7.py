import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        Widget = QLabel("Hello")
        font = Widget.font()
        font.setPointSize(30)
        Widget.setFont(font)
        
        Widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(Widget)
        
app = QApplication(sys.argv)
Window = MainWindow()
Window.show()
app.exec()