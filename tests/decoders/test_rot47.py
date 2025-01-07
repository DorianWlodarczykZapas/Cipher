import unittest

from src.decoders.rot_47 import Rot47Cipher


class TestRot47Cipher(unittest.TestCase):
    def setUp(self):
        self.cipher = Rot47Cipher()

    def test_encrypt_character_within_range(self):
        self.assertEqual(self.cipher.encrypt("!"), "P")
        self.assertEqual(self.cipher.encrypt("~"), "O")

    def test_decrypt_character_within_range(self):
        self.assertEqual(self.cipher.decrypt("p"), "A")
        self.assertEqual(self.cipher.decrypt("O"), "~")

    def test_encrypt_decrypt_identity(self):
        text = "Hello, World!123"
        encrypted = self.cipher.encrypt(text)
        decrypted = self.cipher.decrypt(encrypted)
        self.assertEqual(decrypted, text)

    def test_encrypt_sentences(self):
        sentences = [
            (
                "The quick brown fox jumps over the lazy dog.",
                "%96 BF:4< 3C@H? 7@I ;F>AD @G6C E96 =2KJ 5@8]",
            ),
            (
                "ROT47 should only affect ASCII characters between 33 and 126.",
                "#~%cf D9@F=5 @?=J 27764E p$rxx 492C24E6CD 36EH66? bb 2?5 `ae]",
            ),
        ]
        for text, expected in sentences:
            self.assertEqual(self.cipher.encrypt(text), expected)

    def test_decrypt_sentences(self):
        sentences = [
            ('O{I#x+6"!,B6#y"~l"!~#:9#DZ"%H}', "~LxRIZeQP[qeRJQO=QPORihRs+QTwN"),
            (
                "4FC:@? p!p6C46 r@?8E 96C 4@F=5 2?286C 72E96C2Aj |@C:8:?D 33 j @7 126.",
                "curion APAerce Congt her could anager fatherap; Morigins bb ; of `ae]",
            ),
        ]
        for encrypted, expected in sentences:
            self.assertEqual(self.cipher.decrypt(encrypted), expected)
