import unittest

from p5_Merrill_Grant import caesar_cipher, caesar_decipher, letter_frequency


class TestCaesarFunctions(unittest.TestCase):
    def test_caesar_cipher_basic(self):
        self.assertEqual(caesar_cipher("Hello, World!", 3), "Khoor, Zruog!")

    def test_caesar_cipher_preserves_case_and_spaces(self):
        self.assertEqual(caesar_cipher("AbC xyz", 5), "FgH cde")

    def test_caesar_decipher_basic(self):
        self.assertEqual(caesar_decipher("Khoor, Zruog!", 3), "Hello, World!")

    def test_caesar_round_trip(self):
        original = "Python is fun!"
        encoded = caesar_cipher(original, 7)
        decoded = caesar_decipher(encoded, 7)
        self.assertEqual(decoded, original)

    def test_letter_frequency_counts_letters_case_insensitive(self):
        result = letter_frequency("aA bB cC")
        expected = {
            "a": 2,
            "b": 2,
            "c": 2,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
            "m": 0,
            "n": 0,
            "o": 0,
            "p": 0,
            "q": 0,
            "r": 0,
            "s": 0,
            "t": 0,
            "u": 0,
            "v": 0,
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0,
        }
        self.assertEqual(result, expected)

    def test_letter_frequency_ignores_non_letters(self):
        result = letter_frequency("123 !!! abc-XYZ")
        self.assertEqual(result["a"], 1)
        self.assertEqual(result["b"], 1)
        self.assertEqual(result["c"], 1)
        self.assertEqual(result["x"], 1)
        self.assertEqual(result["y"], 1)
        self.assertEqual(result["z"], 1)
        self.assertEqual(result["d"], 0)


if __name__ == "__main__":
    unittest.main()
