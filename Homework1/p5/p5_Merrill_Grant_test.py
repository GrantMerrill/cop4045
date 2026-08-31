import unittest

from p5_Merrill_Grant import caesar_cipher, caesar_decipher, letter_frequency


class TestCaesarCipher(unittest.TestCase):
    def test_caesar_cipher_preserves_case_and_spaces(self):
        text = "Hello World!"
        result = caesar_cipher(text, 3)
        self.assertEqual(result, "Khoor Zruog!")

    def test_caesar_decipher_recovers_original_text(self):
        encrypted = "Khoor Zruog!"
        result = caesar_decipher(encrypted, 3)
        self.assertEqual(result, "Hello World!")

    def test_letter_frequency_ignores_non_letters_and_case(self):
        text = "Hello, World! 123"
        result = letter_frequency(text)
        expected = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 1,
            'e': 1,
            'f': 0,
            'g': 0,
            'h': 1,
            'i': 0,
            'j': 0,
            'k': 0,
            'l': 3,
            'm': 0,
            'n': 0,
            'o': 2,
            'p': 0,
            'q': 0,
            'r': 1,
            's': 0,
            't': 0,
            'u': 0,
            'v': 0,
            'w': 1,
            'x': 0,
            'y': 0,
            'z': 0,
        }
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
