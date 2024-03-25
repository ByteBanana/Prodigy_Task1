def encrypt(msg, key):
    encrypted_msg = ""
    for char in msg:
        # Encrypt uppercase letters
        if char.isupper():
            encrypted_msg += chr((ord(char) + key - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            encrypted_msg += chr((ord(char) + key - 97) % 26 + 97)
        else:
            encrypted_msg += char
    return encrypted_msg

def decrypt(msg, key):
    decrypted_msg = ""
    for char in msg:
        # Decrypt uppercase letters
        if char.isupper():
            decrypted_msg += chr((ord(char) - key - 65) % 26 + 65)
        # Decrypt lowercase letters
        elif char.islower():
            decrypted_msg += chr((ord(char) - key - 97) % 26 + 97)
        else:
            decrypted_msg += char
    return decrypted_msg

def main():
    while True:
        print("\nOptions:")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            msg = input("Enter the message to encrypt: ")
            key = int(input("Enter key: "))
            encrypted_msg = encrypt(msg, key)
            print("Encrypted message:", encrypted_msg)
        elif choice == '2':
            msg = input("Enter the message to decrypt: ")
            key = int(input("Enter key: "))
            decrypted_msg = decrypt(msg, key)
            print("Decrypted message:", decrypted_msg)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()

