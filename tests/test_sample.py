import pytest
import sys
import os

# Add the parent directory to the path to import main.py
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import add, multiply, divide, greet


def test_add():
    """Test addition function"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_multiply():
    """Test multiplication function"""
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0


def test_divide():
    """Test division function"""
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5

    # Test division by zero
    with pytest.raises(ValueError):
        divide(5, 0)


def test_greet():
    """Test greeting function"""
    assert greet("Alice") == "Hello, Alice!"
    assert greet("pytest") == "Hello, pytest!"


# Fixture example
@pytest.fixture
def sample_data():
    """Sample test data"""
    return {"name": "Alice", "age": 30}


def test_sample_data(sample_data):
    """Test using fixture"""
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30


# Parameterized test example
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (10, -5, 5)
])
def test_add_param(a, b, expected):
    """Test addition with multiple parameters"""
    assert add(a, b) == expected