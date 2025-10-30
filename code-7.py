alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def encrypt(plaintext, key):
    """Encrypt plaintext using substitution cipher key"""
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
    """Decrypt ciphertext using substitution cipher key"""
    ciphertext = ciphertext.upper()
    plaintext = ""
    for ch in ciphertext:
        if ch.isalpha():
            index = key.index(ch)
            plaintext += alphabet[index]
        else:
            plaintext += ch
    return plaintext
print("=== SIMPLE SUBSTITUTION CIPHER ===")
plaintext = input("Enter the plaintext: ").upper()
key = input("Enter a 26-letter key (substitution alphabet): ").upper()
if len(key) != 26 or len(set(key)) != 26:
    print("Error: Key must be 26 unique letters (A–Z).")
else:
    cipher = encrypt(plaintext, key)
    print("\n--- ENCRYPTION ---")
    print("Ciphertext:", cipher)

    decrypted = decrypt(cipher, key)
    print("\n--- DECRYPTION ---")
    print("Decrypted Text:", decrypted)
