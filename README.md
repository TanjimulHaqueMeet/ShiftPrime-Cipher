<p align="center">
  <img src="hstu_logo_.png" alt="HSTU Logo" width="150">
</p>

<h2 align="center"><strong>Hajee Mohammad Danesh Science and Technology University, Dinajpur-5200</strong></h2>

---

<h2 align="center" style="color:#16a085;"><strong> Course Information</strong></h2>

<p align="center">
  <strong>Course Title:</strong> Mathematical Analysis for Computer Science  
  <br>
</p>
<p align="center">
  <strong>Course Code:</strong> CSE 361
</p>

---

<h2 align="center" style="color:#2980b9;"><strong> Algorithm Name</strong></h2>

<h1 align="center" style="color:#8e44ad;"><strong>🔐 ShiftPrime-Cipher</strong></h1>
<h3 align="center" style="color:#8e44ad;"><strong>A Lightweight Prime-Based Encryption Algorithm</strong></h3>

---

<h2 align="center" style="color:#16a085;"><strong>Submitted By</strong></h2>

<p align="center">
  <strong>Name:</strong> Md. Tanjimul Haque Meet 
  <br>
  <strong>Student ID:</strong> 2002049 
  <br>
  <strong>Level: 3 , Semester: II</strong> 
  <br>
  Department of Computer Science and Engineering  
</p>

---

<h2 align="center" style="color:#16a085;"><strong>Submitted To</strong></h2>

<p align="center">
  <strong>Name:</strong> Pankaj Bhowmik  
  <br>
  Lecturer  
  <br>
  Department of Computer Science and Engineering, HSTU
</p>


---

## 🧠 Overview

**ShiftPrime-Cipher** is a symmetric encryption algorithm that uses a numeric key to map each digit to a corresponding prime number. Each character in the plaintext is shifted using these prime values to generate a ciphertext. It is lightweight, educational, and based on basic number theory.

---

## 🔑 Prime Mapping

| Digit | Prime |
|-------|-------|
| 0     | 2     |
| 1     | 3     |
| 2     | 5     |
| 3     | 7     |
| 4     | 11    |
| 5     | 13    |
| 6     | 17    |
| 7     | 19    |
| 8     | 23    |
| 9     | 29    |

---

## 🔐 Encryption Algorithm

1. For each character in the plaintext:
2. Get the corresponding digit from the key (cycle if needed).
3. Map the digit to its prime number.
4. Shift the character’s ASCII value by that prime.
5. Store the result in a list.

---

## 🔓 Decryption Algorithm

1. For each number in the ciphertext:
2. Get the corresponding digit from the key (cycle if needed).
3. Map the digit to its prime number.
4. Subtract the prime from the number.
5. Convert the result back to a character.

---

## 📊 Flowcharts

### 🔐 Encryption  
Encryption.png

### 🔓 Decryption  
![Decryption Flowchart](path/to/Decryption.png)

> ⚠️ Replace `path/to/...` with the actual file paths in your GitHub repo (e.g., `images/encryption.png`).

---

## 🧪 Test Case

**Plaintext:** `HSTU CSE`  
**Key:** `4391`  

### Encryption

| Index | Char | ASCII | Key Digit | Prime | Encrypted |
|-------|------|-------|-----------|--------|-----------|
| 0     | H    | 72    | 4         | 11     | 83        |
| 1     | S    | 83    | 3         | 7      | 90        |
| 2     | T    | 84    | 9         | 29     | 113       |
| 3     | U    | 85    | 1         | 3      | 88        |
| 4     | (space) | 32 | 4         | 11     | 43        |
| 5     | C    | 67    | 3         | 7      | 74        |
| 6     | S    | 83    | 9         | 29     | 112       |
| 7     | E    | 69    | 1         | 3      | 72        |

**Ciphertext (numbers):** `83 90 113 88 43 74 112 72`

### Decryption → `HSTU CSE`

---

## 🧾 Source Code (Python)

```python
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
