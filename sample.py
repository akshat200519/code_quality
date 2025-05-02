# This is a sample Python code that aims to be compatible with flake8, pylint, and bandit.

import math  # Import used

# Define a constant
MAX_VALUE = 100


def calculate_hypotenuse(a: float, b: float) -> float:
    """Calculates the hypotenuse of a right-angled triangle."""
    return math.sqrt(a**2 + b**2)


def greet(name="World"):
    """Greets the given name or the world."""
    print(f"Hello, {name}!")


def process_data(data: list) -> list:
    """Processes a list of numbers and returns their squares."""
    results = []
    for item in data:
        if item < MAX_VALUE:
            results.append(item**2)
    return results


def read_file_content(filepath: str) -> str | None:
    """Reads the content of a file if it exists."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None


if __name__ == "__main__":
    side1 = 3.0
    side2 = 4.0
    hypotenuse = calculate_hypotenuse(side1, side2)
    print(f"The hypotenuse of a triangle with sides {side1} and {side2} is: {hypotenuse}")

    greet("User")
    greet()

    numbers = [1, 5, 10, 150, 20]
    squared_numbers = process_data(numbers)
    print(f"Squared numbers less than {MAX_VALUE}: {squared_numbers}")

    # Example of reading a file (this file might not exist in your environment)
    file_content = read_file_content("example.txt")
    if file_content:
        print(f"Content of example.txt: {file_content[:50]}...")  # Print only first 50 chars
    print("End of program")  # Added a print statement
