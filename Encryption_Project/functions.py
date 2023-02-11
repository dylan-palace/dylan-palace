from random import SystemRandom as u
from time import time
from sys import exit
import base64
from strings import base64lib

#Base64 character library found in strings.py -> Reverse lookup
def reverse_base64lib(char):
    return list(base64lib.keys())[list(base64lib.values()).index(char)]

#Exit when error :(
def exit_program():
    print('Closing program :(\n\n')
    exit()

#Generates a list of random numbers from 0-64 (base64 library) that matches the size of the data
def random_key(length):
    start_time = time()
    _key = []
    for counter in range(length):
        _key.append(base64lib[u().randint(0, 64)])
    print(f"---Key generated after {time() - start_time} seconds ---")
    return "".join(_key)

#Reads file data
def read_file(filepath):
    try:
        with open(filepath, encoding="utf-8", 'r') as f:
            data = f.read()
    except:
        print(f'\n\n--- Error reading {filepath}--- \n\n')
        exit_program()
    return data

#Writes data to file
def write_file(data, filepath):
    try:
        with open(filepath, 'w') as f:
            f.write(str(data))
    except:
        print(f'\n\n--- Error writing to {filepath} --- \n\n')
        exit_program()
    return data

#Decryptor, needs key and encrypted data. Shifts data based on the randomly generated corresponding key value
#Returns the decrypted string
def decrypt(_key, data):
    start_time = time()
    decrypted = []
    for index in range(len(data)):
        decrypt = reverse_base64lib(data[index]) - reverse_base64lib(_key[index])
        if decrypt < 0:
            decrypt += 65
        decrypted_char = base64lib[decrypt]
        decrypted.append(decrypted_char)
    print(f"--- Decryption successful after {time() - start_time} seconds ---")
    return str(base64.b64decode(''.join(decrypted)))[2:-1]

#Encryptor, shifts the base64 value based on the randomly generated key value
def encrypt(_key, data):
    start_time = time()
    encrypted = []
    for index in range(len(data)):
        total = reverse_base64lib(data[index]) + reverse_base64lib(_key[index])
        if total > 64:
            total -= 65
        encrypted.append(base64lib[total])
    print(f"--- Encryption successful after {time() - start_time} seconds ---")
    return ''.join(encrypted)
