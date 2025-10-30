def generate_matrix(key):
    """Generate 5x5 Playfair matrix using the given key"""
    key = key.upper().replace("J", "I")
    matrix = []
    for ch in key:
        if ch not in matrix and ch.isalpha():
            matrix.append(ch)
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in matrix:
            matrix.append(ch)
    return [matrix[i:i+5] for i in range(0, 25, 5)]
def find_position(matrix, ch):
    """Find row and column of a character in the matrix"""
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == ch:
                return i, j
    return None
def prepare_text(text):
    """Prepare plaintext for Playfair encryption"""
    text = text.upper().replace("J", "I")
    prepared = ""
    i = 0
    while i < len(text):
        if text[i].isalpha():
            if i + 1 < len(text) and text[i] == text[i + 1]:
                prepared += text[i] + "X"
                i += 1
            else:
                if i + 1 < len(text) and text[i + 1].isalpha():
                    prepared += text[i] + text[i + 1]
                    i += 2
                else:
                    prepared += text[i] + "X"
                    i += 1
        else:
            i += 1
    if len(prepared) % 2 != 0:
        prepared += "X"
    return prepared
def encrypt_pair(matrix, a, b):
    """Encrypt a pair of letters"""
    r1, c1 = find_position(matrix, a)
    r2, c2 = find_position(matrix, b)
    if r1 == r2:
        return matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
    elif c1 == c2:
        return matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]

def decrypt_pair(matrix, a, b):
    """Decrypt a pair of letters"""
    r1, c1 = find_position(matrix, a)
    r2, c2 = find_position(matrix, b)
    if r1 == r2:
        return matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
    elif c1 == c2:
        return matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]
def playfair_encrypt(text, key):
    """Encrypt plaintext using Playfair cipher"""
    matrix = generate_matrix(key)
    prepared = prepare_text(text)
    cipher = ""
    for i in range(0, len(prepared), 2):
        cipher += encrypt_pair(matrix, prepared[i], prepared[i+1])
    return cipher
def playfair_decrypt(cipher, key):
    """Decrypt ciphertext using Playfair cipher"""
    matrix = generate_matrix(key)
    plain = ""
    for i in range(0, len(cipher), 2):
        plain += decrypt_pair(matrix, cipher[i], cipher[i+1])
    return plain
print("=== PLAYFAIR CIPHER ===")
key = input("Enter the key: ").upper()
text = input("Enter the message (Plaintext or Ciphertext): ")

print("\n--- ENCRYPTION ---")
cipher = playfair_encrypt(text, key)
print("Cipher Text:", cipher)

print("\n--- DECRYPTION ---")
plain = playfair_decrypt(cipher, key)
print("Decrypted Text:", plain)
