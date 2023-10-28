import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout

from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
)

class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Widgets App")
        
        layout = QVBoxLayout()
        widgets=[
            QCheckBox,
            QComboBox,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]
        
        for w in widgets:
            layout.addWidget(w())
            widget = QWidget()
            widget.setLayout(layout)
            
            # widget Will expand
            
            self.setCentralWidget(widget)
            
app = QApplication(sys.argv)
Window = MainWindow()
Window.show()
app.exec()
        
        