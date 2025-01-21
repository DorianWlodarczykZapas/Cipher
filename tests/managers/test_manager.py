from unittest.mock import patch

import pytest

from src.data.buffer import Buffer
from src.data.text_data import TextData
from src.file_handlers.filehandlerfactory import JsonFileHandler
from src.managers.manager import Manager


class TestManager:
    @pytest.fixture
    def manager(self):
        buffer = Buffer()
        return Manager(file_handler_type=JsonFileHandler.TYPE, buffer=buffer)

    def test_negative_number_and_exit(self, manager):
        with patch("builtins.input", side_effect=["-1", "6"]), patch(
            "builtins.print"
        ) as mock_print:
            manager.run()

            mock_print.assert_called()
            mock_print.assert_any_call("Invalid choice. Try again.")
            mock_print.assert_any_call("Closing program. Thank you for using!")

    def test_multiple_negative_numbers_and_exit(self, manager):
        with patch(
            "builtins.input", side_effect=["-2", "-5", "-100", "-1000000", "-256", "6"]
        ), patch("builtins.print") as mock_print:
            manager.run()

            mock_print.assert_called()
            mock_print.assert_any_call("Invalid choice. Try again.")
            mock_print.assert_any_call("Closing program. Thank you for using!")

    def test_zero_and_exit(self, manager):
        with patch("builtins.input", side_effect=["0", "6"]), patch(
            "builtins.print"
        ) as mock_print:
            manager.run()

            mock_print.assert_called()
            mock_print.assert_any_call("Invalid choice. Try again.")
            mock_print.assert_any_call("Closing program. Thank you for using!")

    def test_out_of_range_option_and_exit(self, manager):
        with patch("builtins.input", side_effect=["7", "6"]), patch(
            "builtins.print"
        ) as mock_print:
            manager.run()

            mock_print.assert_called()
            mock_print.assert_any_call("Invalid choice. Try again.")
            mock_print.assert_any_call("Closing program. Thank you for using!")

    def test_multiple_out_of_range_numbers_and_exit(self, manager):
        with patch(
            "builtins.input", side_effect=["10", "21", "100", "1000000", "1256", "6"]
        ), patch("builtins.print") as mock_print:
            manager.run()

            mock_print.assert_called()
            mock_print.assert_any_call("Invalid choice. Try again.")
            mock_print.assert_any_call("Closing program. Thank you for using!")

    def test_actions_without_cipher_selected(self, manager):
        with patch("builtins.input", side_effect=["2", "3", "6"]), patch(
            "builtins.print"
        ) as mock_print:
            manager.run()

            mock_print.assert_called()
            mock_print.assert_any_call("Select a cipher first.")
            mock_print.assert_any_call("Closing program. Thank you for using!")

    def test_display_empty_buffer(self, manager):
        with patch("builtins.input", side_effect=["4", "6"]), patch(
            "builtins.print"
        ) as mock_print:
            manager.run()

            mock_print.assert_called()
            mock_print.assert_any_call("Buffer is currently empty.")
            mock_print.assert_any_call("Closing program. Thank you for using!")

    def test_display_non_empty_buffer(self, manager):
        text_data = TextData(
            text="Something here", rot_type="rot13", status="encrypted"
        )
        manager.buffer.add_text_data(text_data)

        with patch("builtins.input", side_effect=["4", "6"]), patch(
            "builtins.print"
        ) as mock_print:
            manager.run()

        mock_print.assert_any_call(f"0: {text_data}")
        mock_print.assert_any_call("Closing program. Thank you for using!")
