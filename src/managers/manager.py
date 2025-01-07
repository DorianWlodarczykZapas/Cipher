from typing import Callable, Union

from src.decoders.factory import CipherFactory
from src.file_handlers.filehandlerfactory import FileHandlerFactory


class Manager:
    def __init__(self, file_handler_type: str, buffer) -> None:
        self.buffer = buffer
        self.file_handler_type = file_handler_type
        self.file_handler = None
        self.current_cipher = None
        self.running: bool = True

    def setup_file_handler(self):
        filename = input("Please enter the filename: ")
        self.file_handler = FileHandlerFactory.get_file_handler(
            self.file_handler_type, filename
        )

    def run(self) -> None:
        options = {
            "1": self.select_cipher,
            "2": lambda: self.setup_and_process_file("encrypt"),
            "3": lambda: self.setup_and_process_file("decrypt"),
            "4": self.display_buffer,
            "5": self.remove_from_buffer,
            "6": self.exit_program,
        }
        while self.running:
            print("\nAvailable options:")
            print("1. Select cipher (ROT13/ROT47)")
            print("2. Encrypt file")
            print("3. Decrypt file")
            print("4. Display Buffer")
            print("5. Remove text from Buffer")
            print("6. Exit program")
            choice: str = input("Choose an option (1, 2, 3, 4, 5, 6): ")
            action: Union[Callable, None] = options.get(choice, self.invalid_choice)
            action()

    def select_cipher(self) -> None:
        cipher_type: str = input("Enter cipher type (rot13/rot47): ").lower()
        self.current_cipher = CipherFactory.get_cipher(cipher_type)
        if self.current_cipher:
            print(f"Cipher selected: {cipher_type.upper()}")
        else:
            print("Invalid cipher type. Try again.")

    def setup_and_process_file(self, mode: str):
        if not self.current_cipher:
            print("Select a cipher first.")
            return
        self.setup_file_handler()
        if self.file_handler:
            self.process_file(mode)

    def process_file(self, mode: str) -> None:
        data = self.file_handler.read_file()
        for item in data:
            if (mode == "encrypt" and item.status == "decrypted") or (
                mode == "decrypt" and item.status == "encrypted"
            ):
                item.text = (
                    self.current_cipher.encrypt(item.text)
                    if mode == "encrypt"
                    else self.current_cipher.decrypt(item.text)
                )
                item.status = "encrypted" if mode == "encrypt" else "decrypted"
                self.buffer.add_text_data(item)
        self.file_handler.write_file(data)
        print(f"{mode.capitalize()}ion completed successfully.")

    def display_buffer(self) -> None:
        self.buffer.display_buffer()

    def remove_from_buffer(self):
        index = int(input("Enter the index of the text to remove from the buffer: "))
        self.buffer.remove_text_data(index)

    def exit_program(self) -> None:
        print("Closing program. Thank you for using!")
        self.running = False

    def invalid_choice(self) -> None:
        print("Invalid choice. Try again.")
