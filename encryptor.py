from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

backend = default_backend()

def derive_key(password: bytes, salt: bytes) -> bytes:
    # Derive a secure key from password using PBKDF2HMAC
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,       # AES-256 key length = 32 bytes
        salt=salt,
        iterations=100000,
        backend=backend
    )
    return kdf.derive(password)

def encrypt_file(file_path, password):
    salt = os.urandom(16)   # 16 bytes salt
    key = derive_key(password.encode(), salt)
    iv = os.urandom(16)     # 16 bytes IV for AES
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    encryptor = cipher.encryptor()

    with open(file_path, "rb") as f:
        data = f.read()

    encrypted_data = encryptor.update(data) + encryptor.finalize()

    with open(file_path + ".enc", "wb") as f:
        f.write(salt + iv + encrypted_data)

    print(f"File encrypted successfully: {file_path}.enc")

def decrypt_file(file_path, password):
    with open(file_path, "rb") as f:
        salt = f.read(16)
        iv = f.read(16)
        encrypted_data = f.read()

    key = derive_key(password.encode(), salt)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    output_file = file_path.replace(".enc", ".dec")
    with open(output_file, "wb") as f:
        f.write(decrypted_data)

    print(f"File decrypted successfully: {output_file}")

def main():
    while True:
        print("\n=== Advanced Encryption Tool ===")
        print("1. Encrypt File")
        print("2. Decrypt File")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            file_path = input("Enter file path to encrypt: ")
            password = input("Enter password: ")
            encrypt_file(file_path, password)

        elif choice == "2":
            file_path = input("Enter encrypted file path (.enc): ")
            password = input("Enter password: ")
            decrypt_file(file_path, password)

        elif choice == "3":
            print("Exiting... Stay secure, bro!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()