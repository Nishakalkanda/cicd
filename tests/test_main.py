import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from cicd.src.main import subtract
from main import add

def test_add_function():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(5, 5) == 10
    

def test_subtract_function():
    assert subtract(12, 3) == 9
    assert subtract(0, 0) == 0
    assert subtract(15, 5) == 10   