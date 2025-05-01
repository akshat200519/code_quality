import os
import sys  # Imports are now on separate lines

def example_function():
    print("This is an example function")  # Correct indentation

def divide_numbers(a, b):
    """Divides two numbers and handles ZeroDivisionError"""
    try:
        result = a / b
    except ZeroDivisionError:
        result = None  # Return None for division by zero
        print("Error: Cannot divide by zero.")
    return result

class MyClass:  # Class name now follows PEP8 (PascalCase)
    def __init__(self, value):
        self.value = value
  
    def get_value(self):
        return self.value

def secure_execute(command):
    """Executes a command safely (avoiding security risks)"""
    safe_commands = ['ls', 'echo']  # Only allow a predefined list of safe commands
    if command in safe_commands:
        os.system(command)
    else:
        print("Security alert: Command not allowed.")

x = {'key': 'value'}  # Correct dictionary spacing

print("Hello, World!")  # Removed unnecessary spaces
