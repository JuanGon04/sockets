import random



def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_inverse(e, phi):
    d = 0
    x1, x2 = 0, 1
    y1, y2 = 1, 0
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = y2 - temp1 * y1

        x2 = x1
        x1 = x
        y2 = y1
        y1 = y

    if temp_phi == 1:
        d = y2

    return d % phi


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Ambos números deben ser primos.")
    elif p == q:
        raise ValueError("p y q no pueden ser iguales.")

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2  # Comenzar con el valor más bajo para e

    # Buscar un valor adecuado para e
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    # Si no se encuentra un valor adecuado para e, generar un error
    if e == phi:
        raise ValueError("No se pudo encontrar un valor adecuado para e.")

    # Calcular el valor de d utilizando inverso multiplicativo
    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))





   
def encrypt1(public_key, plaintext):
    key, n = public_key
    cipher = [str(pow(ord(char), key, n)) for char in plaintext]
    encrypted_message = ' '.join(cipher)
    return encrypted_message


def decrypt1(private_key, ciphertext):
    key, n = private_key
    cipher = [int(char) for char in ciphertext.split()]
    plain = [chr(pow(char, key, n)) for char in cipher]
    decrypted_message = ''.join(plain)
    return decrypted_message

def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 2 == 0:
        return False
    if num < 9:
        return True
    if num % 3 == 0:
        return False
    r = int(num**0.5)
    f = 5
    while f <= r:
        if num % f == 0:
            return False
        if num % (f + 2) == 0:
            return False
        f += 6
    return True


p = 61
q = 53
public_key, private_key = generate_keypair(p, q)