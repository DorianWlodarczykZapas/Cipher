import pytest

from src.decoders.factory import CipherFactory
from src.decoders.rot_13 import Rot13Cipher
from src.decoders.rot_47 import Rot47Cipher


class TestCipherFactory:
    def test_get_rot13_cipher(self):
        cipher = CipherFactory.get_cipher("rot13")
        (
            pytest.fail("cipher is not an instance of Rot13Cipher")
            if not isinstance(cipher, Rot13Cipher)
            else None
        )

    def test_get_rot47_cipher(self):
        cipher = CipherFactory.get_cipher("rot47")
        (
            pytest.fail("cipher is not an instance of Rot47Cipher")
            if not isinstance(cipher, Rot47Cipher)
            else None
        )

    def test_get_cipher_invalid_type(self):
        with pytest.raises(ValueError) as excinfo:
            CipherFactory.get_cipher("unknown")

        expected_msg = "Unknown cipher type: unknown"
        actual_msg = str(excinfo.value)

        if expected_msg not in actual_msg:
            pytest.fail(
                f"Expected message '{expected_msg}' not found in '{actual_msg}'"
            )
