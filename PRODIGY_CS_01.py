def caesar_cipher(text, shift, mode):
    result = ""
    
    for char in text:
        if char.isupper():
            if mode == 'encrypt':
                result += chr((ord(char) + shift - 65) % 26 + 65)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            if mode == 'encrypt':
                result += chr((ord(char) + shift - 97) % 26 + 97)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    
    return result

def main():
    print("Caesar Cipher Program")
    print("---------------------")
    
    message = input("Enter the message: ")
    
    shift = int(input("Enter the shift value: "))
    
    mode = input("Choose mode (encrypt/decrypt): ").lower()
    
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
        return
    
    result = caesar_cipher(message, shift, mode)
    
    print(f"\nResult: {result}")

if __name__ == "__main__":
    main()