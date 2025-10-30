def gcd(a, b):
    """Find the greatest common divisor (used to check if 'a' is valid)"""
    while b != 0:
        a, b = b, a % b
    return a
def mod_inverse(a, m):
    """Find modular inverse of a under modulo m (used for decryption)"""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def encrypt(text, a, b):
    """Encrypt the plaintext using Affine Cipher"""
    result = ""
    for char in text:
        if char.isalpha():
            p = ord(char.upper()) - 65
            c = (a * p + b) % 26
            result += chr(c + 65)
        else:
            result += char
    return result
def decrypt(cipher, a, b):
    """Decrypt the ciphertext using Affine Cipher"""
    result = ""
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "Decryption not possible — 'a' has no modular inverse (not coprime with 26)."
    
    for char in cipher:
        if char.isalpha():
            c = ord(char.upper()) - 65
            p = (a_inv * (c - b)) % 26
            result += chr(p + 65)
        else:
            result += char
    return result
plain_text = input("Enter the plaintext: ").upper()
a = int(input("Enter value for a (must be coprime with 26): "))
b = int(input("Enter value for b: "))

if gcd(a, 26) != 1:
    print("Invalid key! 'a' must be coprime with 26 for a one-to-one mapping.")
else:
    cipher_text = encrypt(plain_text, a, b)
    print("\n--- Encryption ---")
    print("Cipher Text:", cipher_text)

    decrypted_text = decrypt(cipher_text, a, b)
    print("\n--- Decryption ---")
    print("Decrypted Text:", decrypted_text)
