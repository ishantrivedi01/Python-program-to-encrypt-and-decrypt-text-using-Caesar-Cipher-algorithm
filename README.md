# Caesar Cipher Encryption & Decryption

This program implements the Caesar cipher, a simple encryption technique that shifts letters in the alphabet by a specified number of positions. It allows users to encrypt and decrypt messages using a user-defined shift value.

## Features

- Encrypts messages using the Caesar cipher.
- Decrypts messages using the same cipher.
- Prompts the user for a valid shift value.
- User-friendly interface for input and output.

## Functions

### `encrypt(text: str, shift: int) -> str`

Encrypts the given text using the Caesar cipher with the specified shift.

**Args:**
- `text`: The input string to be encrypted.
- `shift`: The number of positions to shift each character.

**Returns:**
- The encrypted string.

### `decrypt(text: str, shift: int) -> str`

Decrypts the given text using the Caesar cipher with the specified shift.

**Args:**
- `text`: The input string to be decrypted.
- `shift`: The number of positions to shift each character back.

**Returns:**
- The decrypted string.

### `get_valid_shift() -> int`

Prompts the user for a valid shift value until one is provided.

**Returns:**
- Valid integer shift value between 0 and 25.

## Usage

1. Run the program.
2. Enter your message when prompted.
3. Provide a shift value (integer between 0 and 25).
4. Choose to encrypt or decrypt your message by typing 'e' or 'd', respectively.
5. To exit the program, type 'q'.

### Example

```bash
$ python caesar_cipher.py
==============================================
               Caesar Cipher Encryption & Decryption               
==============================================
Enter your message: Hello, World!
Enter shift value (integer between 0-25): 3
Type 'e' to encrypt, 'd' to decrypt, or 'q' to quit: e

Encrypted message: Khoor, Zruog!
