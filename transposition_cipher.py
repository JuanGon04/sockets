permutation = [1, 0, 3, 2]
def encrypt_transposition(message):
    encrypted_message = ""
    num_columns = len(permutation)
    num_rows = len(message) // num_columns

    if len(message) % num_columns != 0:
        num_rows += 1

    for col in permutation:
        pointer = col

        while pointer < len(message):
            encrypted_message += message[pointer]
            pointer += num_columns

    return encrypted_message

def decrypt_transposition(encrypted_message):
    decrypted_message = [''] * len(encrypted_message)
    num_columns = len(permutation)
    num_rows = len(encrypted_message) // num_columns

    if len(encrypted_message) % num_columns != 0:
        num_rows += 1

    # Calcula el número de cajas vacías en la matriz
    num_empty_boxes = (num_rows * num_columns) - len(encrypted_message)

    # Llena las cajas vacías con el carácter de espacio
    for i in range(num_empty_boxes):
        encrypted_message += ' '

    # Calcula el tamaño de las columnas con cajas vacías
    column_sizes = [num_rows] * num_columns
    for i in range(num_empty_boxes):
        column_sizes[i % num_columns] -= 1

    # Despliega los caracteres en la matriz
    pointer = 0
    for col in permutation:
        row = 0
        for _ in range(column_sizes[col]):
            decrypted_message[row * num_columns + col] = encrypted_message[pointer]
            pointer += 1
            row += 1

    return ''.join(decrypted_message)

