def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()
    for char in key:
        if char.isalpha() and char not in used:
            matrix.append(char)
            used.add(char)
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]
def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None
def prepare_text(text):
    text = text.upper().replace("J", "I")
    prepared = ""
    i = 0
    while i < len(text):
        if text[i].isalpha():
            a = text[i]
            b = text[i+1] if i+1 < len(text) and text[i+1].isalpha() else 'X'
            if a == b:
                prepared += a + 'X'
                i += 1
            else:
                prepared += a + b
                i += 2
        else:
            i += 1
    if len(prepared) % 2 != 0:
        prepared += 'X'
    return prepared
def encrypt_pair(a, b, matrix):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]
def decrypt_pair(a, b, matrix):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)
    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]
def playfair_encrypt(plaintext, key):
    matrix = generate_key_matrix(key)
    prepared = prepare_text(plaintext)
    ciphertext = ""
    for i in range(0, len(prepared), 2):
        ciphertext += encrypt_pair(prepared[i], prepared[i+1], matrix)
    return ciphertext, matrix
def playfair_decrypt(ciphertext, key):
    matrix = generate_key_matrix(key)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        plaintext += decrypt_pair(ciphertext[i], ciphertext[i+1], matrix)
    return plaintext
key = input("Enter keyword: ")
text = input("Enter plaintext: ")
ciphertext, matrix = playfair_encrypt(text, key)
decrypted = playfair_decrypt(ciphertext, key)
print("\n5x5 Key Matrix:")
for row in matrix:
    print(" ".join(row))
print("\n--- Results ---")
print(f"Prepared Text : {prepare_text(text)}")
print(f"Encrypted Text: {ciphertext}")
print(f"Decrypted Text: {decrypted}")
