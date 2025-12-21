from flask import Flask, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.playfair.playfair_cipher import PlayFairCipher
import rsa
import os

app = Flask(__name__)

caesar_cipher = CaesarCipher()
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

KEY_PATH = "cipher/rsa/keys/"
if not os.path.exists(KEY_PATH):
    os.makedirs(KEY_PATH)

@app.route("/api/rsa/generate_keys", methods=["GET"])
def rsa_generate_keys():
    (public_key, private_key) = rsa.newkeys(1024)
    with open(os.path.join(KEY_PATH, "publicKey.pem"), "wb") as f:
        f.write(public_key.save_pkcs1())
    with open(os.path.join(KEY_PATH, "privateKey.pem"), "wb") as f:
        f.write(private_key.save_pkcs1())
    return jsonify({"message": "Keys generated and saved successfully"})

@app.route("/api/rsa/encrypt", methods=["POST"])
def rsa_encrypt():
    data = request.json
    message = data["message"].encode('utf-8')
    with open(os.path.join(KEY_PATH, "publicKey.pem"), "rb") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())
    crypto = rsa.encrypt(message, public_key)
    return jsonify({"encrypted_message": crypto.hex()})

@app.route("/api/rsa/decrypt", methods=["POST"])
def rsa_decrypt():
    data = request.json
    ciphertext = bytes.fromhex(data["ciphertext"])
    with open(os.path.join(KEY_PATH, "privateKey.pem"), "rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
    message = rsa.decrypt(ciphertext, private_key).decode('utf-8')
    return jsonify({"decrypted_message": message})

@app.route("/api/rsa/sign", methods=["POST"])
def rsa_sign():
    data = request.json
    message = data["message"].encode('utf-8')
    with open(os.path.join(KEY_PATH, "privateKey.pem"), "rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
    signature = rsa.sign(message, private_key, 'SHA-256')
    return jsonify({"signature": signature.hex()})

@app.route("/api/rsa/verify", methods=["POST"])
def rsa_verify():
    data = request.json
    message = data["message"].encode('utf-8')
    signature = bytes.fromhex(data["signature"])
    with open(os.path.join(KEY_PATH, "publicKey.pem"), "rb") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())
    try:
        rsa.verify(message, signature, public_key)
        return jsonify({"is_verified": True})
    except rsa.VerificationError:
        return jsonify({"is_verified": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)