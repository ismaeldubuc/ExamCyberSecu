from Crypto.Cipher import AES
import os

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext).rstrip()
    original_path = file_path.replace('.enc', '')
    with open(original_path, 'wb') as f:
        f.write(plaintext)
    os.remove(file_path)

def decrypt_folder(folder_path, key):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_name.endswith('.enc'):
            decrypt_file(file_path, key)

if __name__ == "__main__":
    folder_path = 'dossier_confidentiel'
    key = bytes.fromhex("6eac4554e8f47401ffd4bb0a2d306a11")
    decrypt_folder(folder_path, key)
    print("Decryption complete.")
