import os, sys  # Multiple imports on a single line

def example_function():
  print("This is an example function")  # Indentation error: This line should be indented

def unused_function():  # Unused function will be flagged
  pass

def divide_numbers(a, b):
  result = a / b  # Potential ZeroDivisionError when b is zero
  return result

class myClass:  # Class name doesn't follow PEP8 (should be MyClass)
  def __init__(self, value):
    self.value = value
  
  def get_value(self):
    return self.value

def security_risk():
  user_input = input("Enter a command: ")
  os.system(user_input)  # Security risk: This could execute harmful commands

x = { 'key' : "value" }  # Incorrect dictionary spacing, should be {'key': 'value'}

print( "Hello, World!" )  # Unnecessary spaces around the parentheses
