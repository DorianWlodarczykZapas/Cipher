from .rot import Rot
from .rot_13 import Rot13Cipher
from .rot_47 import Rot47Cipher


class CipherFactory:
    @staticmethod
    def get_cipher(cipher_type: str) -> Rot:
        if cipher_type == "rot13":
            return Rot13Cipher()
        elif cipher_type == "rot47":
            return Rot47Cipher()
        else:
            raise ValueError(f"Unknown cipher type: {cipher_type}")
