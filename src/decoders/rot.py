from abc import ABC, abstractmethod


class Rot(ABC):
    @abstractmethod
    def encrypt(self, text: str) -> str:
        pass

    @abstractmethod
    def decrypt(self, text: str) -> str:
        pass
