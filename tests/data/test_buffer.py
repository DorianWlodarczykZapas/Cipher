import unittest

from src.data.buffer import Buffer
from src.data.text_data import TextData


class TestBuffer(unittest.TestCase):
    def setUp(self):
        self.buffer = Buffer()

    def test_add_text_object_to_buffer(self):
        test_object = TextData(text="Kod cezara", rot_type="rot13", status="encrypted")
        self.buffer.add_text_data(test_object)
        self.assertEqual(len(self.buffer.memory), 1)
        self.assertIn(test_object, self.buffer.memory)

    def test_remove_text_object_from_buffer(self):
        buffer = Buffer()
        test_object = TextData(
            text="Example Text", rot_type="rot13", status="encrypted"
        )
        buffer.add_text_data(test_object)
        buffer.remove_text_data(0)
        self.assertEqual(len(buffer.memory), 0)
        self.assertNotIn(test_object, buffer.memory)

    def test_remove_text_object_from_empty_buffer(self):
        buffer = Buffer()
        buffer.remove_text_data(0)
        self.assertEqual(len(buffer.memory), 0)

    def test_remove_text_object_with_invalid_index(self):
        buffer = Buffer()
        test_object = TextData(
            text="Another Example", rot_type="rot13", status="encrypted"
        )
        buffer.add_text_data(test_object)
        buffer.remove_text_data(10)
        self.assertEqual(len(buffer.memory), 1)
        self.assertIn(test_object, buffer.memory)

    def test_display_buffer_empty(self):
        buffer = Buffer()
        self.assertFalse(buffer.memory)

    def test_display_buffer_with_items(self):
        buffer = Buffer()
        test_object1 = TextData(text="First Text", rot_type="rot13", status="encrypted")
        test_object2 = TextData(
            text="Second Text", rot_type="rot13", status="encrypted"
        )
        buffer.add_text_data(test_object1)
        buffer.add_text_data(test_object2)
        self.assertIn(test_object1, buffer.memory)
        self.assertIn(test_object2, buffer.memory)
        self.assertEqual(len(buffer.memory), 2)
