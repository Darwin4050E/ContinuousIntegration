import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    """Fixture que provee una instancia limpia de la calculadora en cada prueba."""
    return Calculator()


def test_add(calc):
    """Prueba la suma de dos números."""
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0