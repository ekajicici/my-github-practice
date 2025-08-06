# Simple Calculator

# Function to add two numbers
def add(a, b):
    return a + b

# Function to divide two numbers
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero."

# Example usage
num1 = 10
num2 = 2

print("Addition:", add(num1, num2))
print("Division:", divide(num1, num2))
