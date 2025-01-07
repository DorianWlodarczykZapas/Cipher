from .file_handler import FileHandler
from .json_file_handler import JsonFileHandler


class FileHandlerFactory:
    @staticmethod
    def get_file_handler(file_handler_type: str, filename: str) -> FileHandler:
        if file_handler_type == JsonFileHandler.TYPE:
            return JsonFileHandler(filename)
        else:
            raise ValueError(f"Unknown file type: {file_handler_type}")
