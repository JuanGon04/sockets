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


def start_server():
    host = 'localhost'
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
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                print('Mensaje recibido:', message)

                response = input('Ingrese una respuesta al cliente: ')
                client_socket.send(response.encode('utf-8'))

            except UnicodeDecodeError:
                print('Error al decodificar el mensaje.')

        client_socket.close()

    server_socket.close()

if __name__ == '__main__':
    start_server()
