import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

# Membuat fungsi untuk menampilkan pesan dialog
def show_message_dialog():
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Pesan Dialog")
    msg_box.setText("Tombol telah ditekan!")
    msg_box.setStandardButtons(QMessageBox.Okey)
    msg_box.exec()

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Contoh Aplikasi PyQt")
window.setGeometry(100, 100, 400, 200)

button = QPushButton("Tekan Tombol", window)
button.setGeometry(150, 80, 100, 40)
button.clicked.connect(show_message_dialog)

window.show()
# app.exec()
sys.exit(app.exec())
