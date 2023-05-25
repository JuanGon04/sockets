# -*- coding: utf-8 -*-
import socket
from substitution_cipher import encrypt_substitution, decrypt_substitution
from transposition_cipher import encrypt_transposition, decrypt_transposition

def encrypt(message, method):
    message_encrypt = ""
    if method == 'sustitucion':
       message_encrypt = encrypt_substitution(message)+'1'
    
    if method == 'transposicion':
        message_encrypt = encrypt_transposition(message)

    return message_encrypt

def start_client():
    host = 'localhost'
    port = 8888

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        method = input("Ingrese un metodo de cifrado: ")
        message = input("Ingrese un mensaje ('exit' para salir): ")
        message_encrypt = encrypt(message, method)
        print(message_encrypt)
        client_socket.send(message_encrypt.encode('utf-8'))
        if message == 'exit':
            break
        response = client_socket.recv(1024).decode('utf-8')
        print('El servidor responde:', response)

    client_socket.close()

if __name__ == '__main__':
    start_client()

