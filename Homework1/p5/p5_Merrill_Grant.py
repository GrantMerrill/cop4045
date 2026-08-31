def caesar_cipher(text, shift):
    """Shift each alphabetic character in text by the given integer shift."""
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            offset = (ord(char) - start + shift) % 26
            result += chr(start + offset)
        else:
            result += char

    return result


def caesar_decipher(cyphertext, shift):
    """Decrypt a Caesar-encrypted string by shifting letters backward."""
    clear = ""

    for char in cyphertext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            offset = (ord(char) - start - shift) % 26
            clear += chr(start + offset)
        else:
            clear += char

    return clear


def letter_frequency(text):
    """Count how many times each letter appears in the text, ignoring case and non-letters."""
    counts = {chr(code): 0 for code in range(ord('a'), ord('z') + 1)}

    for char in text:
        if char.isalpha():
            letter = char.lower()
            counts[letter] += 1

    return counts


def main():
    """Display a simple menu for Caesar cipher operations."""
    print("Caesar Cipher Menu")
    print("1. Enter a message")
    print("2. Enter a shift value")
    print("3. View encrypted text, letter frequency, and decrypted text")
    print("4. Exit")

    message = ""
    shift = 0

    while True:
        choice = input("\nSelect an option (1-4): ")

        if choice == "1":
            message = input("Enter a message: ")
            print("Message saved.")
        elif choice == "2":
            try:
                shift = int(input("Enter a shift value: "))
                print("Shift saved.")
            except ValueError:
                print("Invalid shift. Please enter an integer.")
        elif choice == "3":
            if message == "":
                print("Please enter a message first.")
                continue

            encrypted = caesar_cipher(message, shift)
            frequencies = letter_frequency(message)
            decrypted = caesar_decipher(encrypted, shift)

            print("\nCiphered text:", encrypted)
            print("Letter frequency:")
            for letter, count in frequencies.items():
                if count > 0:
                    print(f"  {letter}: {count}")
            print("Deciphered text:", decrypted)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
