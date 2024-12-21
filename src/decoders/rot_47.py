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
            if 33 <= ord(char) <= 126:
                new_char = ord(char) + self.shift
                if new_char > 126:
                    new_char = new_char - 94
                transformed.append(chr(new_char))
            else:
                transformed.append(char)
        return "".join(transformed)
