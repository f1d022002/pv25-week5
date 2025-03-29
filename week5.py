import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel, QComboBox, QMessageBox, QTextEdit, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
import re

class FormValidationApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Form Validation')
        self.setGeometry(100, 100, 600, 400)

        # Set layout
        self.layout = QVBoxLayout()
        self.form_layout = QFormLayout()

        
        self.nim_label = QLabel('P: Andi Sibwayiq Abi Mahmud  NIM: F1D022002')
        self.nim_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.layout.addWidget(self.nim_label)

        # Name 
        self.name_input = QLineEdit()
        self.form_layout.addRow('Name:', self.name_input)

        # Email 
        self.email_input = QLineEdit()
        self.form_layout.addRow('Email:', self.email_input)

        # Age 
        self.age_input = QLineEdit()
        self.age_input.setValidator(QIntValidator())
        self.form_layout.addRow('Age:', self.age_input)

        # Phone Number 
        self.phone_input = QLineEdit()
        self.phone_input.setInputMask('+62 999 9999 9999')
        self.form_layout.addRow('Phone Number:', self.phone_input)

        self.address_input = QTextEdit()
        self.form_layout.addRow('Address:', self.address_input)

        # Gender 
        self.gender_dropdown = QComboBox()
        self.gender_dropdown.addItem("Select Gender")
        self.gender_dropdown.addItem("Mas2")
        self.gender_dropdown.addItem("Mbak2") 
        self.gender_dropdown.addItem("Anomali") 
        self.form_layout.addRow('Gender:', self.gender_dropdown)

        # Education 
        self.education_dropdown = QComboBox()
        self.education_dropdown.addItem("Select Education Level")
        self.education_dropdown.addItem("Esemah")
        self.education_dropdown.addItem("Unram")
        self.education_dropdown.addItem("S2")
        self.education_dropdown.addItem("Esdehh")
        self.form_layout.addRow('Education:', self.education_dropdown)

        
        self.layout.addLayout(self.form_layout)

        # Submit Button
        self.submit_button = QPushButton('Save')
        self.submit_button.setStyleSheet("QPushButton { background-color: #6A4C92; color: white; font-size: 14px; padding: 10px; border-radius: 3px; }")
        self.submit_button.clicked.connect(self.validate_and_submit)

        # Clear Button
        self.clear_button = QPushButton('Clear')
        self.clear_button.setStyleSheet("QPushButton { background-color: #6A4C92; color: white; font-size: 14px; padding: 10px; border-radius: 3px; }")
        self.clear_button.clicked.connect(self.clear_fields)

        
        button_layout = QHBoxLayout()

        
        button_layout.addWidget(self.submit_button)
        button_layout.addWidget(self.clear_button)


        self.layout.addLayout(button_layout)

        self.setLayout(self.layout)

    def validate_and_submit(self):
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        age = self.age_input.text().strip()
        phone = self.phone_input.text().strip().replace(" ", "").replace("+", "") 
        address = self.address_input.toPlainText().strip()  
        gender = self.gender_dropdown.currentText()
        education = self.education_dropdown.currentText()

        # Validate nama
        if not name.isalpha():
            self.show_warning('Huruf Woe bkn Angka.')
            return

        # Validate email
        if not self.is_valid_email(email):
            self.show_warning('Jangn Lupa @,.com.')
            return

        # Validate umur
        if not age.isdigit():
            self.show_warning('Dekk?')
            return

        # kondisi umur
        if int(age) < 18:
            self.show_warning('Minimal 18 yahhhh.')
            return

        # Validate no hp
        if len(phone) != 12:
            self.show_warning('Janagn Di isi 13 Digit Dek.')
            return

        # Validate alamat
        if not address:
            self.show_warning('Gk punya Rumah?')
            return

        # Validate gender
        if gender == "Select Gender":
            self.show_warning('Gk Punya Gender?')
            return

        # Validate education
        if education == "Select Education Level":
            self.show_warning('PIlih, jn gk di pilih')
            return

        self.show_success('Kelassss!!!!!!')
        self.clear_fields()

    def is_valid_email(self, email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def show_warning(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Form Validation")
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setStyleSheet("QPushButton { background-color: #6A4C92; color: white; font-size: 14px; }")
        msg.exec_()

    def show_success(self, message):
        success_msg = QMessageBox()
        success_msg.setIcon(QMessageBox.Information)
        success_msg.setWindowTitle("Success")
        success_msg.setText(message)
        success_msg.setStandardButtons(QMessageBox.Ok)
        success_msg.setStyleSheet("QPushButton { background-color: #6A4C92; color: white; font-size: 14px; }")
        success_msg.exec_()

    def clear_fields(self):
        self.name_input.clear()
        self.email_input.clear()
        self.age_input.clear()
        self.phone_input.clear()
        self.address_input.clear()  
        self.gender_dropdown.setCurrentIndex(0)
        self.education_dropdown.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FormValidationApp()
    window.show()
    sys.exit(app.exec_())
