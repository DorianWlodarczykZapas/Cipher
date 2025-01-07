from .text_data import TextData


class Buffer:
    def __init__(self):
        self.memory = []

    def add_text_data(self, text_data: TextData) -> None:
        self.memory.append(text_data)
        print(f"Added: {text_data}")

    def remove_text_data(self, index: int) -> None:
        if 0 <= index < len(self.memory):
            removed = self.memory.pop(index)
            print(f"Removed: {removed}")
        else:
            print(f"Error: Index {index} out of range. No item removed.")

    def display_buffer(self) -> None:
        if self.memory:
            for i, text_data in enumerate(self.memory):
                print(f"{i}: {text_data}")
        else:
            print("Buffer is currently empty.")
