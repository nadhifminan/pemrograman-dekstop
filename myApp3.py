import sys
from PyQt6.QtWidgets import QApplication, QPushButton
applikasi = QApplication(sys.argv)
window = QPushButton("Tekan Saya")
window.show()
applikasi.exec()