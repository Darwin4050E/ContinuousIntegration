import pytest
from calculator import Calculator

"""Tests unitarios para cada requerimiento."""

@pytest.fixture
def calc():
    """Fixture que provee una instancia limpia de la calculadora en cada prueba."""
    return Calculator()

def test_invalid_plan(calc):
    """R1: Test con plan inválido/desconocido."""
    assert calc.calculate_quote("GOLD") == -1