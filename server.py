# -*- coding: utf-8 -*-

import socket
from substitution_cipher import encrypt_substitution, decrypt_substitution
from transposition_cipher import encrypt_transposition, decrypt_transposition
from DES import encrypt_DES, decrypt_DES

def encrypt(message, method):
    message_encrypt = ""
    if method == 'sustitucion':
       message_encrypt = encrypt_substitution(message)
    
    if method == 'transposicion':
        message_encrypt = encrypt_transposition(message)
        
    if method == 'des':
        message_encrypt = encrypt_DES(message)

    return message_encrypt

def decrypt(message, method):
    message_decrypt = ""
    if method == 'sustitucion':
       message_decrypt = decrypt_substitution(message)
    
    if method == 'transposicion':
        message_decrypt = decrypt_transposition(message)
        
    if method == "des":
        message_decrypt = decrypt_DES(message)

    return message_decrypt

def start_server():
    host = '127.0.0.1'
    port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print('El servidor está escuchando en el puerto', port)

    while True:
        client_socket, address = server_socket.accept()
        print('Conexión establecida desde:', address)

        while True:
            try:
                method_decrypt = client_socket.recv(1024).decode('utf-8')
                
                if method_decrypt=='des':
                    message = client_socket.recv(1024)
                else:
                    message = client_socket.recv(1024).decode('utf-8')
                                
                message_decrypt = decrypt(message, method_decrypt)
                if not message:
                    break
                print('Mensaje recibido:', message_decrypt)
                
            
                while True:
                    method_encrypt = input("Ingrese un metodo de cifrado: ").lower()
                    print(method_encrypt)
                    if method_encrypt == 'sustitucion' or  'transposicion' or  'DES':
                        client_socket.send(method_encrypt.encode('utf-8'))
                        break
                                        
                    else:
                        print("metodo incorrecto")
                
                
                response = input('Ingrese una respuesta al cliente: ')
                message_encrypt = encrypt(response, method_encrypt)
                print(message_encrypt)
                client_socket.send(message_encrypt.encode('utf-8'))

            except UnicodeDecodeError:
                print('Error al decodificar el mensaje.')

        client_socket.close()

    server_socket.close()

if __name__ == '__main__':
    start_server()
