# Encryption Program

import random
import string
chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# it is best for us to not shows chars and key in real encryption program.
# print(f"chars: {chars}")
# print(f"key: {key}")

# Encrypt the message

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print("\n")
print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")


# Decrypt the message

cipher_text_text = input("\nEnter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
print("\n")
print(f"Encrypted message: {cipher_text}")
print(f"Original message: {plain_text}")














