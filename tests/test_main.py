import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import add

def test_add_function():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(5, 5) == 10
    