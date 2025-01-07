from .rot import Rot


class Rot47Cipher(Rot):
    def __init__(self):
        self.shift = 47
        self.start_char = 33
        self.end_char = 126

    def encrypt(self, text: str) -> str:
        return self._rotate(text)

    def decrypt(self, text: str) -> str:
        return self._rotate(text)

    def _rotate(self, text: str) -> str:
        transformed = []
        for char in text:
            if self.start_char <= ord(char) <= self.end_char:
                shifted = ord(char) + self.shift
                if shifted > self.end_char:
                    shifted -= self.end_char - self.start_char + 1
                transformed.append(chr(shifted))
            else:
                transformed.append(char)
        return "".join(transformed)
