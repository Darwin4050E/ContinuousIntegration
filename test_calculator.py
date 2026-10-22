"""Unit tests for calculator module."""
import pytest
from calculator import (
    Calculator,
    apply_group_discount,
    apply_special_offer,
    apply_premium_surcharge
)


@pytest.fixture(name="calc")
def fixture_calc():
    """Fixture que provee una instancia limpia de la calculadora."""
    return Calculator()


def test_add(calc):
    """Prueba la suma de dos números."""
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0


class TestGroupDiscount:
    """Tests for R4 group discount."""

    def test_one_member_no_discount(self):
        """One member gets no discount."""
        assert apply_group_discount(90, 1) == 90

    def test_two_members_apply_discount(self):
        """Two members get 10% discount."""
        assert apply_group_discount(90, 2) == pytest.approx(81.0)

    def test_three_members_apply_discount(self):
        """Three members get 10% discount."""
        assert apply_group_discount(135, 3) == pytest.approx(121.5)

    def test_boundary_exactly_two_members(self):
        """Exactly two members triggers discount."""
        assert apply_group_discount(100, 2) == pytest.approx(90.0)


class TestSpecialOffer:
    """Tests for R5 special offer."""

    def test_below_200_no_discount(self):
        """Amount below 200 gets no discount."""
        assert apply_special_offer(81) == 81

    def test_exactly_200_no_discount(self):
        """Amount exactly 200 gets no discount."""
        assert apply_special_offer(200) == 200

    def test_above_200_subtract_20(self):
        """Amount above 200 gets 20 subtracted."""
        assert apply_special_offer(306) == pytest.approx(286.0)

    def test_exactly_400_subtract_20(self):
        """Amount exactly 400 gets 20 subtracted."""
        assert apply_special_offer(400) == pytest.approx(380.0)

    def test_above_400_subtract_50(self):
        """Amount above 400 gets 50 subtracted."""
        assert apply_special_offer(450) == pytest.approx(400.0)


class TestPremiumSurcharge:
    """Tests for R6 premium surcharge."""

    def test_no_premium_extra_no_surcharge(self):
        """No premium extra means no surcharge."""
        assert apply_premium_surcharge(286, False) == pytest.approx(286.0)

    def test_with_premium_extra_adds_15_percent(self):
        """Premium extra adds 15% surcharge."""
        assert apply_premium_surcharge(200, True) == pytest.approx(230.0)

    def test_premium_surcharge_large_amount(self):
        """Premium surcharge works on large amounts."""
        assert apply_premium_surcharge(400, True) == pytest.approx(460.0)
        