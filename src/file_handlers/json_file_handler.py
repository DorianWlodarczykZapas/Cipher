import json
from dataclasses import asdict
from typing import List

from TextData import TextData

from .file_handler import FileHandler


class JsonFileHandler(FileHandler):
    def read_file(self) -> List[TextData]:
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data_list = json.load(file)
                return [TextData(**item) for item in data_list]
        except FileNotFoundError:
            print(f"File {self.filename} not found")
            return []
        except json.JSONDecodeError:
            print(f"File {self.filename} is empty")
            return []
        except Exception as e:
            print(f"Error: {e}")
            return []

    def write_file(self, data: List[TextData]) -> None:
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json_data = [asdict(item) for item in data]
                json.dump(json_data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error: {e}")
