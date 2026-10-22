import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    """Fixture que provee una instancia limpia de la calculadora en cada prueba."""
    return Calculator()

def test_invalid_plan(calc):
    """R1: Test con plan inválido/desconocido."""
    assert calc.calculate_quote("GOLD", [], 1) == -1