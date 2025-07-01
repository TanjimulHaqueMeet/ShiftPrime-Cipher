def get_prime_shift(digit_char):
    prime_map = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    if not digit_char.isdigit():
        raise ValueError("Key must contain only digits.")
    return prime_map[int(digit_char)]

def encrypt(plaintext, key):
    cipher = []
    for i, ch in enumerate(plaintext):
        k = get_prime_shift(key[i % len(key)])
        cipher.append(ord(ch) + k)
    return cipher

def decrypt(cipher, key):
    plain = ''
    for i, val in enumerate(cipher):
        k = get_prime_shift(key[i % len(key)])
        plain += chr(val - k)
    return plain

def main():
    print("=== Prime-Based Cipher ===")
    choice = input("Do you want to (E) Encrypt or (D) Decrypt? ").strip().upper()
    if choice == 'E':
        text = input("Enter the plaintext: ")
        key = input("Enter the numeric key (e.g. 4391): ")
        if not key.isdigit():
            print("Error: Key must contain only digits.")
            return
        cipher = encrypt(text, key)
        print("Ciphertext (as numbers):", ' '.join(map(str, cipher)))
    elif choice == 'D':
        cipher_input = input("Enter the cipher numbers separated by spaces: ")
        try:
            cipher = list(map(int, cipher_input.strip().split()))
        except ValueError:
            print("Error: Cipher must be numbers separated by spaces.")
            return
        key = input("Enter the numeric key (e.g. 4391): ")
        if not key.isdigit():
            print("Error: Key must contain only digits.")
            return
        plain = decrypt(cipher, key)
        print("Decrypted Text:", plain)
    else:
        print("Invalid choice. Please select E or D.")

if __name__ == "__main__":
    main()
