import os


def greet_user(name: str) -> str:
    """Return a greeting message for the user."""
    if not name:
        raise ValueError("Name cannot be empty.")
    return f"Hello, {name}!"


def calculate_sum(a: int, b: int) -> int:
    """Calculate and return the sum of two integers."""
    return a + b


class FileManager:
    """A simple file manager class."""

    def __init__(self, filename: str):
        self.filename = filename

    def write_to_file(self, content: str) -> None:
        """Write content to the file safely."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write(content)

    def read_from_file(self) -> str:
        """Read content from the file safely."""
        with open(self.filename, 'r', encoding='utf-8') as file:
            return file.read()


def main():
    """Main function to demonstrate the script."""
    user_name = "DevOps"
    message = greet_user(user_name)
    print(message)

    result = calculate_sum(10, 20)
    print(f"Sum: {result}")

    file_manager = FileManager("sample.txt")
    file_manager.write_to_file("This is a test file.")
    content = file_manager.read_from_file()
    print(f"File content: {content}")


if __name__ == "__main__":
    main()
