from flask import Flask, request, jsonify, render_template, json
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.playfair.playfair_cipher import PlayFairCipher
# ...
app = Flask(__name__)

# CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

# --------------------------
# VIGENERE CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()
playfair_cipher = PlayFairCipher()


@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data["plain_text"]
    key = int(data["key"])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({"encrypted_message": encrypted_text})


@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data["cipher_text"]
    key = int(data["key"])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({"decrypted_message": decrypted_text})


@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    data = request.json
    plain_text = data["plain_text"]
    key = data["key"]
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({"encrypted_text": encrypted_text})


@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.json
    cipher_text = data["cipher_text"]
    key = data["key"]
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({"decrypted_text": decrypted_text})
# --------------------------


@app.route("/api/playfair/creatematrix", methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'playfair_matrix': playfair_matrix})


@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})


@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# #router routes for home page


@app.route("/")
def home():
    return render_template('index.html')

# #router routes for caesar cipher


@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

# WEB ENCRYPTION FORM HANDLING (GET data from HTML form)


# Trong app.py (Thay thế hai hàm này)

@app.route("/encrypt", methods=['POST'])
def web_caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])

    caesar_cipher_local = CaesarCipher()
    encrypted_text = caesar_cipher_local.encrypt_text(text, key)

    # Trả về template, truyền kết quả mã hóa và key vào biến 'result_encrypt'
    return render_template('caesar.html',
                           result_encrypt=encrypted_text,
                           text_encrypt=text,
                           key_encrypt=key)


@app.route("/decrypt", methods=['POST'])
def web_caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])

    caesar_cipher_local = CaesarCipher()
    decrypted_text = caesar_cipher_local.decrypt_text(text, key)

    # Trả về template, truyền kết quả giải mã và key vào biến 'result_decrypt'
    return render_template('caesar.html',
                           result_decrypt=decrypted_text,
                           text_decrypt=text,
                           key_decrypt=key)


# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
