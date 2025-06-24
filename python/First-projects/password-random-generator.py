import sys
import random
import string
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QFileDialog, QMessageBox
)

class PasswordGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.setGeometry(100, 100, 400, 250)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Password Length Input
        self.length_label = QLabel("Enter password length:")
        self.length_input = QLineEdit()
        self.length_input.setPlaceholderText("e.g., 12")

        # Generate Button
        self.generate_button = QPushButton("Generate Password")
        self.generate_button.clicked.connect(self.generate_password)

        # Resulting Password Display
        self.password_display = QLineEdit()
        self.password_display.setReadOnly(True)

        # Optional Description
        self.desc_label = QLabel("Optional description:")
        self.desc_input = QLineEdit()
        self.desc_input.setPlaceholderText("e.g., Gmail account")

        # Save Button
        self.save_button = QPushButton("Save Password")
        self.save_button.clicked.connect(self.save_password)

        # Add widgets to layout
        layout.addWidget(self.length_label)
        layout.addWidget(self.length_input)
        layout.addWidget(self.generate_button)
        layout.addWidget(QLabel("Generated Password:"))
        layout.addWidget(self.password_display)
        layout.addWidget(self.desc_label)
        layout.addWidget(self.desc_input)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def generate_password(self):
        try:
            length = int(self.length_input.text())
            if length <= 0:
                raise ValueError

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_display.setText(password)
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid positive integer for password length.")

    def save_password(self):
        password = self.password_display.text()
        description = self.desc_input.text()

        if not password:
            QMessageBox.warning(self, "No Password", "Please generate a password first.")
            return

        file_path, _ = QFileDialog.getSaveFileName(self, "Save Password", "", "Text Files (*.txt)")
        if file_path:
            with open(file_path, 'a') as f:
                f.write(f"{description}: {password}\n" if description else f"{password}\n")
            QMessageBox.information(self, "Saved", "Password saved successfully.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec_())
