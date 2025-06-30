def add(x, y):
    """Add two numbers"""
    return x + y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def greet(name):
    """Greet a person"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("Calculator functions ready for testing")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"2 * 3 = {multiply(2, 3)}")
    print(greet("pytest"))
