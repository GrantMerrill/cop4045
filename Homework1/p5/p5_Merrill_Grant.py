def caesar_cipher(text, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            lowercase_char = char.lower()
            index = alphabet.index(lowercase_char)
            new_index = (index + shift) % 26
            shifted_char = alphabet[new_index]

            if is_upper:
                encrypted += shifted_char.upper()
            else:
                encrypted += shifted_char
        else:
            encrypted += char

    return encrypted


def caesar_decipher(cyphertext, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    clear = ""

    for char in cyphertext:
        if char.isalpha():
            is_upper = char.isupper()
            lowercase_char = char.lower()
            index = alphabet.index(lowercase_char)
            new_index = (index - shift) % 26
            shifted_char = alphabet[new_index]

            if is_upper:
                clear += shifted_char.upper()
            else:
                clear += shifted_char
        else:
            clear += char

    return clear


def letter_frequency(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    counts = {}

    for letter in alphabet:
        counts[letter] = 0

    for char in text:
        if char.isalpha():
            lowercase_char = char.lower()
            counts[lowercase_char] += 1

    return counts


def main():
    text = ""
    shift = 0

    print("Caesar Cipher Menu")
    print("1. Enter a message")
    print("2. Enter a shift value")
    print("3. Display encrypted text, letter frequency, and deciphered text")
    print("4. Exit")

    while True:
        choice = input("\nChoose an option: ")

        if choice == "1":
            text = input("Enter a message: ")
            print("Message saved.")

        elif choice == "2":
            while True:
                shift_input = input("Enter a shift value (integer): ")
                try:
                    shift = int(shift_input)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

        elif choice == "3":
            if text == "":
                print("Please enter a message first.")
            else:
                cyphertext = caesar_cipher(text, shift)
                frequencies = letter_frequency(text)
                clear = caesar_decipher(cyphertext, shift)

                print("\nEncrypted text:", cyphertext)
                print("Letter frequency:")
                for letter in frequencies:
                    print(f"{letter}: {frequencies[letter]}")
                print("Deciphered text:", clear)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
