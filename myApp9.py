import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QSlider, QPushButton, QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        
        # Buat widget utama
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Buat tata letak vertikal
        layout = QVBoxLayout(self.central_widget)
        
        # Buat label
        self.label = QLabel("Hello")
        font = self.label.font()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Buat slider untuk mengubah ukuran teks
        self.size_slider = QSlider(Qt.Orientation.Horizontal)
        self.size_slider.setMinimum(10)
        self.size_slider.setMaximum(100)
        self.size_slider.setValue(30)
        self.size_slider.valueChanged.connect(self.update_font_size)
        
        # Buat combobox untuk mengubah font
        self.font_combo = QComboBox()
        self.font_combo.addItems(["Arial", "Times New Roman", "Verdana"])
        self.font_combo.currentTextChanged.connect(self.update_font)
        
        # Tambahkan label, slider, dan combobox ke tata letak
        layout.addWidget(self.label)
        layout.addWidget(self.size_slider)
        layout.addWidget(self.font_combo)
        
    def update_font_size(self):
        size = self.size_slider.value()
        font = self.label.font()
        font.setPointSize(size)
        self.label.setFont(font)
        
    def update_font(self):
        font_name = self.font_combo.currentText()
        font = self.label.font()
        font.setFamily(font_name)
        self.label.setFont(font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
