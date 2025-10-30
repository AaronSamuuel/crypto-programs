def generate_key(text, key):
    """Repeat or trim the key to match the length of the text"""
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)
def encrypt(text, key):
    """Encrypt the plaintext using the Vigenère cipher"""
    cipher_text = []
    for i in range(len(text)):
        if text[i].isalpha():
            x = (ord(text[i].upper()) + ord(key[i].upper())) % 26
            x += ord('A')
            cipher_text.append(chr(x))
        else:
            cipher_text.append(text[i])
    return "".join(cipher_text)
def decrypt(cipher_text, key):
    """Decrypt the ciphertext using the Vigenère cipher"""
    orig_text = []
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            x = (ord(cipher_text[i].upper()) - ord(key[i].upper()) + 26) % 26
            x += ord('A')
            orig_text.append(chr(x))
        else:
            orig_text.append(cipher_text[i])
    return "".join(orig_text)
plain_text = input("Enter the plaintext: ").upper()
key = input("Enter the key: ").upper()

key_full = generate_key(plain_text, key)
cipher_text = encrypt(plain_text, key_full)

print("\n--- Encryption ---")
print("Generated Key: ", key_full)
print("Cipher Text: ", cipher_text) 
decrypted_text = decrypt(cipher_text, key_full)
print("\n--- Decryption ---")
print("Decrypted Text: ", decrypted_text)
