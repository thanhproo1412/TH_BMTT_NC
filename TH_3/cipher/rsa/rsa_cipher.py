import sys
import os

# Lấy đường dẫn thư mục gốc (TH_3) và thêm vào hệ thống
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow # Bây giờ Python sẽ tìm thấy folder ui ở thư mục gốc
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Đảm bảo các tên object này khớp với file rsa.py của bạn
        self.ui.btn_gen_keys.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                QMessageBox.information(self, "Success", response.json()["message"])
        except Exception as e:
            print(f"Error: {e}")

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {
            "message": self.ui.txt_plain_text.toPlainText(),
            "key_type": "public"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.ui.txt_cipher_text.setPlainText(response.json()["encrypted_message"])
                QMessageBox.information(self, "Success", "Encrypted Successfully")
        except Exception as e:
            print(f"Error: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {
            "ciphertext": self.ui.txt_cipher_text.toPlainText(),
            "key_type": "private"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.ui.txt_plain_text.setPlainText(response.json()["decrypted_message"])
                QMessageBox.information(self, "Success", "Decrypted Successfully")
        except Exception as e:
            print(f"Error: {e}")

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {"message": self.ui.txt_info.toPlainText()}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.ui.txt_sign.setPlainText(response.json()["signature"])
                QMessageBox.information(self, "Success", "Signed Successfully")
        except Exception as e:
            print(f"Error: {e}")

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.txt_info.toPlainText(),
            "signature": self.ui.txt_sign.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                result = "Verified Successfully" if response.json()["is_verified"] else "Verified Fail"
                QMessageBox.information(self, "Result", result)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())