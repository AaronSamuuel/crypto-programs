def mod_inverse(a, m):
    """Find modular inverse of a under modulo m"""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_decrypt(cipher, a, b):
    """Decrypt text using given a and b"""
    result = ""
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "Invalid key: 'a' has no modular inverse."

    for char in cipher:
        if char.isalpha():
            c = ord(char.upper()) - 65
            p = (a_inv * (c - b)) % 26
            result += chr(p + 65)
        else:
            result += char
    return result
def solve_affine_key(cipher_most, cipher_second, plain_most='E', plain_second='T'):
    """Solve for a and b based on letter correspondences"""
    C1 = ord(cipher_most.upper()) - 65
    C2 = ord(cipher_second.upper()) - 65
    P1 = ord(plain_most.upper()) - 65
    P2 = ord(plain_second.upper()) - 65
    diffP = (P1 - P2) % 26
    diffC = (C1 - C2) % 26
    inv_diffP = mod_inverse(diffP, 26)
    if inv_diffP is None:
        print("No valid inverse for difference in plaintext values.")
        return None, None
    a = (diffC * inv_diffP) % 26
    b = (C1 - a * P1) % 26
    return a, b
ciphertext = input("Enter the ciphertext: ").upper()
cipher_most = 'B'
cipher_second = 'U'
plain_most = 'E'
plain_second = 'T'

a, b = solve_affine_key(cipher_most, cipher_second, plain_most, plain_second)

if a is not None:
    print(f"\nPossible keys found:\n  a = {a}, b = {b}")
    print("\nDecrypted text:")
    print(affine_decrypt(ciphertext, a, b))
else:
    print("Could not determine valid keys.")
