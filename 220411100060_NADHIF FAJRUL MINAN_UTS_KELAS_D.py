import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QComboBox, QDateEdit, QRadioButton, QSpinBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Mahasiswa")
        
        layout = QVBoxLayout()

        self.nama_label = QLabel("Nama:")
        self.nama_input = QLineEdit()
        layout.addWidget(self.nama_label)
        layout.addWidget(self.nama_input)

        
        self.nim_label = QLabel("NIM:")
        self.nim_input = QLineEdit()
        layout.addWidget(self.nim_label)
        layout.addWidget(self.nim_input)

       
        self.alamat_label = QLabel("Alamat:")
        self.alamat_input = QLineEdit()
        layout.addWidget(self.alamat_label)
        layout.addWidget(self.alamat_input)

        
        self.jenis_kelamin_label = QLabel("Jenis Kelamin:")
        self.jenis_kelamin_radio1 = QRadioButton("Laki-laki")
        self.jenis_kelamin_radio2 = QRadioButton("Perempuan")
        layout.addWidget(self.jenis_kelamin_label)
        layout.addWidget(self.jenis_kelamin_radio1)
        layout.addWidget(self.jenis_kelamin_radio2)

        
        self.tanggal_lahir_label = QLabel("Tanggal Lahir:")
        self.tanggal_lahir_input = QDateEdit()
        layout.addWidget(self.tanggal_lahir_label)
        layout.addWidget(self.tanggal_lahir_input)

        
        self.hobi_label = QLabel("Hobi:")
        self.hobi_combo = QComboBox()
        self.hobi_combo.addItem("Membaca")
        self.hobi_combo.addItem("Olahraga")
        self.hobi_combo.addItem("Traveling")
        layout.addWidget(self.hobi_label)
        layout.addWidget(self.hobi_combo)

       
        self.tinggi_badan_label = QLabel("Tinggi Badan (cm):")
        self.tinggi_badan_input = QSpinBox()
        layout.addWidget(self.tinggi_badan_label)
        layout.addWidget(self.tinggi_badan_input)

       
        self.tambah_data_button = QPushButton("Tambahkan Data")
        self.tambah_data_button.clicked.connect(self.tambahkan_data)
        layout.addWidget(self.tambah_data_button)

        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def tambahkan_data(self):
        
        nama = self.nama_input.text()
        nim = self.nim_input.text()
        alamat = self.alamat_input.text()
        jenis_kelamin = "Laki-laki" if self.jenis_kelamin_radio1.isChecked() else "Perempuan"
        tanggal_lahir = self.tanggal_lahir_input.date().toString(Qt.DateFormat.ISODate)
        hobi = self.hobi_combo.currentText()
        tinggi_badan = self.tinggi_badan_input.value()

        
        print("Nama:", nama)
        print("NIM:", nim)
        print("Alamat:", alamat)
        print("Jenis Kelamin:", jenis_kelamin)
        print("Tanggal Lahir:", tanggal_lahir)
        print("Hobi:", hobi)
        print("Tinggi Badan:", tinggi_badan)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
