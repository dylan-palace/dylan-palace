import string
import random

alphabet = list(string.ascii_lowercase)

def encode_message(cleartext):
    key, encoded_message= [], []
    for char in cleartext:
        if char in alphabet:
            n = alphabet.index(char)
            key_val = random.randint(-(n), 25-n)
            encoded_message.append(alphabet[ ( n + key_val ) ])
            key.append(key_val)
        else:
            encoded_message.append(char)
            key.append(0)
    print("Encoded Message:", "".join(encoded_message))
    decode_message(key, encoded_message)


def decode_message(key, encoded_message):
    re_decoded = []
    count = 0
    for char in encoded_message:
        if char not in alphabet:
            re_decoded.append(char)
        else:
            new_char_pos = alphabet.index(char) - key[count]
            if new_char_pos < 0:
                new_char_pos = new_char_pos + 25
            re_decoded.append(alphabet[new_char_pos])
        count += 1
    print("Key:", key)
    if print_decoded == ("Y" or "y"):
        print("Decoded message:", "".join(re_decoded))

print("Before we begin... would you like the decoded version of this message to print? Y/n")
print_decoded = input()
print("Enter String to be encrypted:")
encode_message(input())
