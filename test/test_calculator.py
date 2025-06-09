import unittest

import pytest
from src.Testing.calculator import add, subtract, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        assert add(2, 3) == 5

    def test_subtract(self):
        assert subtract(10, 3) == 7

    def test_divide_normal(self):
        assert divide(10, 2) == 5.0

    def test_divide_zero(self):
        with pytest.raises(ValueError):
            divide(10, 0)
