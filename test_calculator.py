import pytest
from calculator import Calculator, apply_group_discount, apply_special_offer, apply_premium_surcharge

@pytest.fixture
def calc():
    """Fixture que provee una instancia limpia de la calculadora en cada prueba."""
    return Calculator()


def test_add(calc):
    """Prueba la suma de dos números."""
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

    
class TestGroupDiscount:

    def test_one_member_no_discount(self):
        assert apply_group_discount(90, 1) == 90

    def test_two_members_apply_discount(self):
        assert apply_group_discount(90, 2) == pytest.approx(81.0)

    def test_three_members_apply_discount(self):
        assert apply_group_discount(135, 3) == pytest.approx(121.5)

    def test_boundary_exactly_two_members(self):
        assert apply_group_discount(100, 2) == pytest.approx(90.0)

