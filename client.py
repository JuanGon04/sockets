# -*- coding: utf-8 -*-
import socket
from substitution_cipher import encrypt_substitution, decrypt_substitution
from transposition_cipher import encrypt_transposition, decrypt_transposition

def encrypt(message, method):
    message_encrypt = ""
    if method == 'sustitucion':
       message_encrypt = encrypt_substitution(message)
    
    if method == 'transposicion':
        message_encrypt = encrypt_transposition(message)

    return message_encrypt

def decrypt(message, method):
    message_decrypt = ""
    if method == 'sustitucion':
       message_decrypt = decrypt_substitution(message)
    
    if method == 'transposicion':
        message_decrypt = decrypt_transposition(message)

    return message_decrypt

def start_client():
    host = '127.0.0.1'
    port = 8888

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        while True:
            method_encrypt = input("Ingrese un metodo de cifrado: ").lower()
            
            if method_encrypt == 'sustitucion' or method_encrypt == 'transposicion':
                client_socket.send(method_encrypt.encode('utf-8'))
                break
            
            else:
                print("metodo incorrecto")
            
        message = input("Ingrese un mensaje ('exit' para salir): ")
        message_encrypt = encrypt(message, method_encrypt)
        print(message_encrypt)
        client_socket.send(message_encrypt.encode('utf-8'))

        if message == 'exit':
            break
        
        
        method_decrypt = client_socket.recv(1024).decode('utf-8')
        response = client_socket.recv(1024).decode('utf-8')
        message_decrypt = decrypt(response, method_decrypt)
        print('El servidor responde:', message_decrypt)

    client_socket.close()

if __name__ == '__main__':
    start_client()

