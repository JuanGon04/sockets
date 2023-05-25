from Cryptodome.Cipher import DES
from Cryptodome.Random import get_random_bytes

def pad(text):
    # Completa el texto con espacios para que tenga una longitud múltiplo de 8
    while len(text) % 8 != 0:
        text += b' '
    return text

def encrypt_DES(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = pad(plaintext.encode('utf-8'))
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt_DES(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext)
    return padded_plaintext.strip()

# Generar una clave aleatoria de 8 bytes


# Texto de prueba


    