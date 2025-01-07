import unittest

from src.decoders.rot_13 import Rot13Cipher


class TestRot13Cipher(unittest.TestCase):
    def setUp(self):
        self.cipher = Rot13Cipher()

    def test_encrypt_single_char(self):
        self.assertEqual(self.cipher.encrypt("a"), "n")
        self.assertEqual(self.cipher.encrypt("z"), "m")

    def test_decrypt_single_char(self):
        self.assertEqual(self.cipher.decrypt("n"), "a")
        self.assertEqual(self.cipher.decrypt("m"), "z")

    def test_encrypt_uppercase_char(self):
        self.assertEqual(self.cipher.encrypt("A"), "N")
        self.assertEqual(self.cipher.encrypt("Z"), "M")

    def test_decrypt_uppercase_char(self):
        self.assertEqual(self.cipher.decrypt("N"), "A")
        self.assertEqual(self.cipher.decrypt("M"), "Z")

    def test_encrypt_string(self):
        self.assertEqual(self.cipher.encrypt("Hello, World!"), "Uryyb, Jbeyq!")

    def test_decrypt_string(self):
        self.assertEqual(self.cipher.decrypt("Uryyb, Jbeyq!"), "Hello, World!")

    def test_non_alpha_characters(self):
        self.assertEqual(self.cipher.encrypt("1234567890"), "1234567890")
        self.assertEqual(self.cipher.encrypt("!@#$%^&*()_+"), "!@#$%^&*()_+")

    def test_encrypt_decrypt_identity(self):
        text = "The quick brown fox jumps over the lazy dog."
        encrypted = self.cipher.encrypt(text)
        decrypted = self.cipher.decrypt(encrypted)
        self.assertEqual(decrypted, text)
