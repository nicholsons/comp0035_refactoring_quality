import pytest

from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator(2, 2)


class TestCalculator:

    def test_add(self, calc):
        result = calc.add()
        assert result == 4

    def test_subtract(self, calc):
        result = calc.subtract()
        assert result == 0

    def test_multiply(self, calc):
        result = calc.multiply()
        assert result == 4

    def test_divide(self, calc):
        result = calc.divide()
        assert result == 1

    def test_divide_by_zero_returns_error(self):
        with pytest.raises(ZeroDivisionError):
            c = Calculator(3, 0)
            c.divide()


if __name__ == "__main__":
    pytest.main(["test"])
