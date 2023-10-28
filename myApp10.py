# membuat tool bar
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My APP")
        label = QLabel("Hello")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)
        
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        button = toolbar.addAction("Click Me")
        button.triggered.connect(self.onMyToolbarButtonClick)

    def onMyToolbarButtonClick(self):
        print("Button Clicked")

app = QApplication(sys.argv)
Window = MainWindow()
Window.show()
app.exec()
 
