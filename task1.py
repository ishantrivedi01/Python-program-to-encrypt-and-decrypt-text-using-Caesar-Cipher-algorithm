def encrypt(text: str, shift: int) -> str:
    """
    Encrypts the given text using Caesar cipher with the specified shift.
    
    Args:
        text: The input string to be encrypted
        shift: The number of positions to shift each character
        
    Returns:
        The encrypted string
    """
    encrypted_text = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text.append(shifted_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def decrypt(text: str, shift: int) -> str:
    """
    Decrypts the given text using Caesar cipher with the specified shift.
    
    Args:
        text: The input string to be decrypted
        shift: The number of positions to shift each character back
        
    Returns:
        The decrypted string
    """
    return encrypt(text, -shift)

def get_valid_shift() -> int:
    """
    Prompts the user for a valid shift value until one is provided.
    
    Returns:
        Valid integer shift value
    """
    while True:
        try:
            shift = int(input("Enter shift value (integer between 0-25): "))
            if 0 <= shift <= 25:
                return shift
            print("Shift must be between 0 and 25. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    """Main program execution function."""
    print("\n" + "="*50)
    print(" Caesar Cipher Encryption & Decryption ".center(50))
    print("="*50)
    
    message = input("\nEnter your message: ")
    shift = get_valid_shift()
    
    while True:
        choice = input("\nType 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()
        if choice == 'e':
            encrypted = encrypt(message, shift)
            print("\nEncrypted message:", encrypted)
        elif choice == 'd':
            decrypted = decrypt(message, shift)
            print("\nDecrypted message:", decrypted)
        elif choice == 'q':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please type 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()