import pytest

from src.file_handlers.filehandlerfactory import FileHandlerFactory
from src.file_handlers.json_file_handler import JsonFileHandler


class TestFileHandlerFactory:
    def test_get_json_file_handler(self):
        filename = "test.json"
        handler = FileHandlerFactory.get_file_handler(JsonFileHandler.TYPE, filename)
        assert isinstance(handler, JsonFileHandler)
        assert handler.filename == filename

        if not isinstance(handler, JsonFileHandler):
            pytest.fail("Handler is not an instance of JsonFileHandler")
        if handler.filename != filename:
            pytest.fail("Filename does not match the provided filename")

    def test_get_file_handler_invalid_type(self):
        with pytest.raises(ValueError) as excinfo:
            FileHandlerFactory.get_file_handler("xml", "test.xml")
        expected_msg = "Unknown file type: xml"
        actual_msg = str(excinfo.value)
        if expected_msg not in actual_msg:
            pytest.fail(
                f"Expected message '{expected_msg}' not found in '{actual_msg}'"
            )
