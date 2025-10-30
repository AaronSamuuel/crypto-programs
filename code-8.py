import string
alphabet = string.ascii_uppercase
def encrypt(plaintext, key):
    """Encrypt the plaintext using the monoalphabetic cipher key"""
    plaintext = plaintext.upper()
    ciphertext = ""
    for ch in plaintext:
        if ch.isalpha():
            index = alphabet.index(ch)
            ciphertext += key[index]
        else:
            ciphertext += ch
    return ciphertext
def decrypt(ciphertext, key):
    """Decrypt the ciphertext using the monoalphabetic cipher key"""
    ciphertext = ciphertext.upper()
    plaintext = ""
    for ch in ciphertext:
        if ch.isalpha():
            index = key.index(ch)
            plaintext += alphabet[index]
        else:
            plaintext += ch
    return plaintext
print("=== MONOALPHABETIC CIPHER ===")
key = input("Enter a 26-letter cipher key (A–Z permutation): ").upper()
if len(key) != 26 or len(set(key)) != 26:
    print("Error: The key must contain all 26 unique letters (A–Z)!")
else:
    plaintext = input("Enter the plaintext: ")
    cipher_text = encrypt(plaintext, key)
    print("\n--- ENCRYPTION ---")
    print("Cipher Text:", cipher_text)
    decrypted_text = decrypt(cipher_text, key)
    print("\n--- DECRYPTION ---")
    print("Decrypted Text:", decrypted_text)
