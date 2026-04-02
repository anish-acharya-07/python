import random
import string


characters = string.ascii_letters + string.digits + string.punctuation + " "

characters = list(characters)

key = characters.copy()

random.shuffle(key)

# print(f"characters : {characters}")
# print(f"keys : {key}")

#encryption

plain_text = input("\nenter a message to encrypt : ")

cipher_text = ""

for letter in plain_text:

    index = characters.index(letter)
    cipher_text += key[index]

print(f"\noriginal message : {plain_text}")
print(f"encrypted message : {cipher_text}")


#decryption

cipher_text = input("\nenter the encrypted message to decrypt : ")

plain_text = ""

for letter in cipher_text:

    index = key.index(letter)

    plain_text += characters[index]

print(f"\nencrypted message : {cipher_text}")
print(f"decrypted text : {plain_text}\n")
