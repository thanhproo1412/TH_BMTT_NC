# File: cipher/playfair/playfair_cipher.py
class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        """Tạo ma trận Playfair 5x5 từ khóa."""
        key = key.replace("J", "I") 
        key = key.upper()
        key_set = set(key)

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" 
        remaining_letters = [
            letter for letter in alphabet if letter not in key_set
        ]

        matrix = list(key)

        for letter in remaining_letters:
            matrix.append(letter)
            if len(matrix) == 25:
                break

        playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        """Tìm tọa độ (hàng, cột) của ký tự trong ma trận."""
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        return -1, -1
    
    def playfair_encrypt(self, plain_text, key):
        """Mã hóa văn bản bằng Playfair Cipher."""
        playfair_matrix = self.create_playfair_matrix(key)

        # Xử lý văn bản đầu vào (thay J bằng I, chuyển hoa)
        plain_text = plain_text.replace("J", "I") 
        plain_text = plain_text.upper()
        encrypted_text = ""

        # Thêm 'X' nếu có hai ký tự giống nhau hoặc văn bản có độ dài lẻ
        processed_text = ""
        i = 0
        while i < len(plain_text):
            char1 = plain_text[i]
            if i + 1 < len(plain_text):
                char2 = plain_text[i+1]
                if char1 == char2:
                    processed_text += char1 + "X"
                    i += 1
                else:
                    processed_text += char1 + char2
                    i += 2
            else:
                processed_text += char1 + "X"
                i += 1

        plain_text = processed_text # Văn bản đã được xử lý thành các cặp ký tự

        for i in range(0, len(plain_text), 2):
            pair = plain_text[i:i+2]
            row1, col1 = self.find_letter_coords(playfair_matrix, pair[0])
            row2, col2 = self.find_letter_coords(playfair_matrix, pair[1])

            if row1 == row2: # Cùng hàng: dịch phải 1 vị trí
                encrypted_text += playfair_matrix[row1][(col1 + 1) % 5]
                encrypted_text += playfair_matrix[row2][(col2 + 1) % 5]
            elif col1 == col2: # Cùng cột: dịch xuống 1 vị trí
                encrypted_text += playfair_matrix[(row1 + 1) % 5][col1]
                encrypted_text += playfair_matrix[(row2 + 1) % 5][col2]
            else: # Hình chữ nhật: thay thế bằng góc đối diện (cùng hàng)
                encrypted_text += playfair_matrix[row1][col2]
                encrypted_text += playfair_matrix[row2][col1]

        return encrypted_text
    
    def playfair_decrypt(self, cipher_text, key):
        """Giải mã văn bản bằng Playfair Cipher."""
        playfair_matrix = self.create_playfair_matrix(key)
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(playfair_matrix, pair[0])
            row2, col2 = self.find_letter_coords(playfair_matrix, pair[1])

            if row1 == row2: # Cùng hàng: dịch trái 1 vị trí
                decrypted_text += playfair_matrix[row1][(col1 - 1) % 5]
                decrypted_text += playfair_matrix[row2][(col2 - 1) % 5]
            elif col1 == col2: # Cùng cột: dịch lên 1 vị trí
                decrypted_text += playfair_matrix[(row1 - 1) % 5][col1]
                decrypted_text += playfair_matrix[(row2 - 1) % 5][col2]
            else: # Hình chữ nhật: thay thế bằng góc đối diện (cùng hàng)
                decrypted_text += playfair_matrix[row1][col2]
                decrypted_text += playfair_matrix[row2][col1]

        # Xử lý hậu kỳ: loại bỏ 'X' được thêm vào
        banro = ""
        for i in range(0, len(decrypted_text), 2):
            char1 = decrypted_text[i]
            char2 = decrypted_text[i+1]

            if i + 2 < len(decrypted_text) and char2 == 'X' and decrypted_text[i+2] == char1:
                banro += char1
            else:
                banro += char1 + char2

        if banro[-1] == 'X': # Loại bỏ X cuối cùng nếu nó là ký tự đệm
            banro = banro[:-1]

        return banro