def caesar_cipher(text, key, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift = key if mode == 'encrypt' else -key
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result
text = input("Enter text: ")
key = int(input("Enter key (1-25): "))

encrypted = caesar_cipher(text, key, 'encrypt')
decrypted = caesar_cipher(encrypted, key, 'decrypt')

print("\n--- Results ---")
print(f"Encrypted text: {encrypted}")
print(f"Decrypted text: {decrypted}")
