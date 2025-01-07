import json
import tempfile
import unittest

from src.data.text_data import TextData
from src.file_handlers.json_file_handler import JsonFileHandler


class TestJsonFileHandler(unittest.TestCase):
    def test_read_file(self):
        temp_file = tempfile.NamedTemporaryFile(
            delete=False, mode="w+", encoding="utf-8"
        )
        data = [{"text": "Hello, World!", "rot_type": "rot13", "status": "encrypted"}]
        json.dump(data, temp_file)
        temp_file.close()

        handler = JsonFileHandler(filename=temp_file.name)
        result = handler.read_file()
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], TextData)
        self.assertEqual(result[0].text, "Hello, World!")
        self.assertEqual(result[0].rot_type, "rot13")
        self.assertEqual(result[0].status, "encrypted")

        temp_file.close()

    def test_write_file(self):
        temp_file = tempfile.NamedTemporaryFile(
            delete=False, mode="w+", encoding="utf-8"
        )
        temp_file.close()

        handler = JsonFileHandler(filename=temp_file.name)
        text_data = [
            TextData(text="Hello, World!", rot_type="rot13", status="encrypted")
        ]
        handler.write_file(text_data)

        with open(temp_file.name, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["text"], "Hello, World!")
            self.assertEqual(data[0]["rot_type"], "rot13")
            self.assertEqual(data[0]["status"], "encrypted")
        temp_file.close()

    def test_read_multiple_entries(self):
        temp_file = tempfile.NamedTemporaryFile(
            delete=False, mode="w+", encoding="utf-8"
        )
        data = [
            {"text": "Hello, World!", "rot_type": "rot13", "status": "encrypted"},
            {"text": "Second entry", "rot_type": "none", "status": "decrypted"},
            {"text": "Another message", "rot_type": "rot13", "status": "encrypted"},
        ]
        json.dump(data, temp_file)
        temp_file.close()

        handler = JsonFileHandler(filename=temp_file.name)
        results = handler.read_file()
        self.assertEqual(len(results), 3)
        self.assertIsInstance(results[1], TextData)
        self.assertEqual(results[1].text, "Second entry")
        self.assertEqual(results[2].text, "Another message")

        temp_file.close()

    def test_write_multiple_entries(self):
        temp_file = tempfile.NamedTemporaryFile(
            delete=False, mode="w+", encoding="utf-8"
        )
        temp_file.close()

        handler = JsonFileHandler(filename=temp_file.name)
        text_data = [
            TextData(text="Hello, World!", rot_type="rot13", status="encrypted"),
            TextData(text="Second entry", rot_type="none", status="decrypted"),
            TextData(text="Another message", rot_type="rot13", status="encrypted"),
        ]

        handler.write_file(text_data)

        with open(temp_file.name, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.assertEqual(len(data), 3)
            self.assertEqual(data[1]["text"], "Second entry")
            self.assertEqual(data[2]["text"], "Another message")

        temp_file.close()
