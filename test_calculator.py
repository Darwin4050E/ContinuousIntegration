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


class TestSpecialOffer:

    def test_below_200_no_discount(self):
        assert apply_special_offer(81) == 81

    def test_exactly_200_no_discount(self):
        assert apply_special_offer(200) == 200

    def test_above_200_subtract_20(self):
        assert apply_special_offer(306) == pytest.approx(286.0)

    def test_exactly_400_subtract_20(self):
        assert apply_special_offer(400) == pytest.approx(380.0)

    def test_above_400_subtract_50(self):
        assert apply_special_offer(450) == pytest.approx(400.0)


class TestPremiumSurcharge:

    def test_no_premium_extra_no_surcharge(self):
        assert apply_premium_surcharge(286, False) == pytest.approx(286.0)

    def test_with_premium_extra_adds_15_percent(self):
        assert apply_premium_surcharge(200, True) == pytest.approx(230.0)

    def test_premium_surcharge_large_amount(self):
        assert apply_premium_surcharge(400, True) == pytest.approx(460.0)