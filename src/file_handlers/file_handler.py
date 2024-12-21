from abc import ABC, abstractmethod
from typing import List


class FileHandler(ABC):
    def __init__(self, filename: str) -> None:
        self.filename = filename

    @abstractmethod
    def read_file(self) -> List[dict]:
        pass

    @abstractmethod
    def write_file(self, data: List[dict]) -> None:
        pass
