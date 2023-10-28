import os
import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication,QLabel,QMainWindow

basedir = os.path.dirname(__file__)
print("Current Working Folder:",os.getcwd())
print("Paths are relative to:",basedir)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        widget=QLabel("Hello Nadhif")
        widget.setPixmap(QPixmap(os.path.join(basedir,"gambar.jpg")))
        widget.setScaledContents(True)
        self.setCentralWidget(widget)
    
app = QApplication(sys.argv)
Window = MainWindow()
Window.show()
app.exec()