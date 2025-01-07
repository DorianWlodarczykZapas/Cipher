from data.buffer import Buffer
from managers.manager import Manager


def main():
    manager = Manager(file_handler_type="json", buffer=Buffer())
    manager.run()


if __name__ == "__main__":
    main()
