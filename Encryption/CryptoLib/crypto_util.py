
# Required Librarys 
from cryptography.fernet import Fernet
import os

# Encryption 

# Generates Key to be used when locking and unlocking encrypted files    
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

# Reads the stored encryption key from the file
def load_key():
    return open("key.key", "rb").read()


# Uses Provided Path to find the file and ecrypt the data usign the key 
def encrypt_file(file_path, key):
    f = Fernet(key)
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(file_path, "wb") as file:
            file.write(encrypted_data)
        return True
    except Exception as e:
        print(f"Error encrypting file {file_path}: {e}")
        return False

# Used to dencrpt fils 
def decrypt_file(file_path, key):
    f = Fernet(key)
    try:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(file_path, "wb") as file:
            file.write(decrypted_data)
        return True
    except Exception as e:
        print(f"Error decrypting file {file_path}: {e}")
        return False

# Extensions to the file Encrypt and Decrypt to recursivley encryting a folders contents 
def encrypt_folder(folder_path, key):
    success = True
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if not encrypt_file(file_path, key):
                success = False
    return success

# Used to dencrpt folder
def decrypt_folder(folder_path, key):
    success = True
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if not decrypt_file(file_path, key):
                success = False
    return success
