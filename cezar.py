def caesar_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = ord(char) + key
            if char.isupper():
                if shift > ord('Z'):
                    shift -= 26
                final_char = chr(shift)
            else:
                if shift > ord('z'):
                    shift -= 26
                final_char = chr(shift)
            ciphertext += final_char
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift = ord(char) - key
            if char.isupper():
                if shift < ord('A'):
                    shift += 26
                final_char = chr(shift)
            else:
                if shift < ord('a'):
                    shift += 26
                final_char = chr(shift)
            plaintext += final_char
        else:
            plaintext += char
    return plaintext

plaintext = "Hello, World!"
key = 5
ciphertext = caesar_encrypt(plaintext, key)
print("Ciphertext: ", ciphertext)
plaintext = caesar_decrypt(ciphertext, key)
print("Plaintext: ", plaintext)