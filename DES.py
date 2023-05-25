from Crypto.Cipher import DES
from secrets import token_bytes

key = token_bytes(8)
nonce = ""
tag = ""

def encrypt_DES(message):
    global nonce
    global tag
    cipher = DES.new(key, DES.MODE_EAX)
    nonce =  cipher.nonce
    ciphertext, tag  = cipher.encrypt_and_digest(message.encode('ascii'))
    print("Dentro de encrypt "+ str(nonce))
    return ciphertext

def decrypt_DES(ciphertext):
    global nonce 
    nonce= nonce
    global tag
    tag=tag
    print("Dentro de decrypt "+ str(nonce))
    cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False
    