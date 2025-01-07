from .rot import Rot


class Rot13Cipher(Rot):
    def __init__(self):
        self.shift = 13
        self.alphabet_size = 26

    def encrypt(self, text: str) -> str:
        return self._rotate(text)

    def decrypt(self, text: str) -> str:
        return self._rotate(text)

    def _rotate(self, text: str) -> str:
        transformed = []
        for char in text:
            if char.isalpha():
                start = ord("a") if char.islower() else ord("A")
                offset = (ord(char) - start + self.shift) % self.alphabet_size
                transformed.append(chr(start + offset))
            else:
                transformed.append(char)
        return "".join(transformed)
