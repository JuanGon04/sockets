# -*- coding: utf-8 -*-
import socket
from substitution_cipher import encrypt_substitution, decrypt_substitution
from transposition_cipher import encrypt_transposition, decrypt_transposition
from DES import encrypt_DES, decrypt_DES
from rsa import encrypt1,decrypt1
from Cryptodome.Random import get_random_bytes
import rsa

key = b'01234567'
public_key  =  rsa.public_key
private_key = rsa.private_key

def encrypt(message, method):
    message_encrypt = ""
    if method == 'sustitucion':
       message_encrypt = encrypt_substitution(message)
    
    if method == 'transposicion':
        message_encrypt = encrypt_transposition(message)

    if method == 'des':
       message_encrypt = encrypt_DES(key, message)
       
    if method == 'rsa':
        message_encrypt = encrypt1(public_key,message)
        
    return message_encrypt

def decrypt(message, method):
    message_decrypt = ""
    if method == 'sustitucion':
       message_decrypt = decrypt_substitution(message)
    
    if method == 'transposicion':
        message_decrypt = decrypt_transposition(message)
        
    if method == "des":
        message_decrypt = decrypt_DES(key, message)
        
    if method == 'rsa':
        message_decrypt = decrypt1(private_key,message)
        
    return message_decrypt

def start_client():
    host = '127.0.0.1'
    port = 8888
    message_encrypt = ()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        while True:
            method_encrypt = input("Ingrese un metodo de cifrado: ").lower()
            print(method_encrypt)
            if method_encrypt == 'sustitucion' or  'transposicion' or 'DES' or 'rsa':
                client_socket.send(method_encrypt.encode('utf-8'))
                break
                    
            else:
                print("metodo incorrecto")
            
        message = input("Ingrese un mensaje ('exit' para salir): ")
        message_encrypt = encrypt(message, method_encrypt)
        print(message_encrypt)
        
        if method_encrypt=='des':
            client_socket.send(message_encrypt)
        else:
            client_socket.send(message_encrypt.encode('utf-8'))

        if message == 'exit':
            break
        
        
        method_decrypt = client_socket.recv(1024).decode('utf-8')
        
        if method_decrypt=='des':
            response = client_socket.recv(1024)
        else:
            response = client_socket.recv(1024).decode('utf-8')
            
        message_decrypt = decrypt(response, method_decrypt)
        print('El servidor responde:', message_decrypt)

    client_socket.close()

if __name__ == '__main__':
    start_client()

