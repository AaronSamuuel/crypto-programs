import string
def encrypt(plaintext, key_map):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            ciphertext += key_map[char].upper() if is_upper else key_map[char]
        else:
            ciphertext += char
    return ciphertext
def decrypt(ciphertext, key_map):
    reverse_map = {v: k for k, v in key_map.items()}
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            plaintext += reverse_map[char].upper() if is_upper else reverse_map[char]
        else:
            plaintext += char
    return plaintext
alphabet = string.ascii_lowercase
substitution = "QWERTYUIOPASDFGHJKLZXCVBNM".lower()
key_map = {alphabet[i]: substitution[i] for i in range(26)}
print("Plain alphabet:  ", alphabet)
print("Cipher alphabet: ", substitution)
text = input("\nEnter text: ")
encrypted = encrypt(text, key_map)
decrypted = decrypt(encrypted, key_map)
print("\n--- Results ---")
print(f"Encrypted text: {encrypted}")
print(f"Decrypted text: {decrypted}")
