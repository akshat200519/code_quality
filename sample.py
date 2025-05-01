import os, sys  # Multiple imports on the same line (not recommended)

def example_function():
    print("This is an example")  # IndentationError

def unused_function():  # Unused function (Pylint will detect this)
    pass

def divide_numbers(a, b):
    result = a / b  # Potential ZeroDivisionError
    return result
    
class myClass:  # Class name should follow PascalCase (PEP8)
    def __init__(self, value):
        self.value = value
    
    def get_value(self):
        return self.value

def security_risk():
    user_input = input("Enter command: ")
    os.system(user_input)  # Security Risk: Arbitrary command execution

x = { 'key' : "value" }  # Incorrect spacing in dictionary

print( "Hello, World!" )  # Unnecessary spaces inside parentheses
