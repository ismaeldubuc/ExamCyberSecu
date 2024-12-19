from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(data.ljust(16 * ((len(data) + 15) // 16)))
    with open(file_path + '.enc', 'wb') as f:
        f.write(cipher.iv + ciphertext)
    os.remove(file_path)

def encrypt_folder(folder_path, key):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            encrypt_file(file_path, key)

if __name__ == "__main__":
    key = get_random_bytes(16)  # AES-128
    folder_path = 'dossier_confidentiel'
    encrypt_folder(folder_path, key)
    print("Encryption complete. Key:", key.hex())
