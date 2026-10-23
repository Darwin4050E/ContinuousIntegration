"""Unit tests for calculator module."""
import pytest

from calculator import Calculator

@pytest.fixture(name="calc")
def fixture_calc():
    """Provide a clean Calculator instance for every test."""
    return Calculator()

class TestPlans:
    """Tests for R1 plan catalog."""

    def test_basic(self, calc):
        """BASIC plan costs 30."""
        assert calc.get_plan_price("BASIC") == 30

    def test_standard(self, calc):
        """STANDARD plan costs 45."""
        assert calc.get_plan_price("STANDARD") == 45

    def test_premium(self, calc):
        """PREMIUM plan costs 70."""
        assert calc.get_plan_price("PREMIUM") == 70

    def test_invalid(self, calc):
        """Unknown plan returns None."""
        assert calc.get_plan_price("GOLD") is None


class TestExtras:
    """Tests for R2 extras."""

    def test_no_extras(self, calc):
        """No extras yields zero cost and no premium flag."""
        assert calc.get_extras_price([], "BASIC") == (0, False)

    def test_one_non_premium(self, calc):
        """A single non-premium extra costs 15 with no premium flag."""
        assert calc.get_extras_price(["GROUP_CLASSES"], "BASIC") == (15, False)

    def test_two_non_premium(self, calc):
        """Two non-premium extras cost 40 with no premium flag."""
        assert calc.get_extras_price(
            ["GROUP_CLASSES", "PERSONAL_TRAINING"], "BASIC"
        ) == (40, False)

    def test_premium_with_premium_plan(self, calc):
        """A premium extra on PREMIUM costs 30 and flags premium."""
        assert calc.get_extras_price(["SPA"], "PREMIUM") == (30, True)

    def test_premium_with_basic_is_invalid(self, calc):
        """A premium extra on BASIC is invalid."""
        assert calc.get_extras_price(["SPA"], "BASIC") is None

    def test_unknown_extra_is_invalid(self, calc):
        """An unknown extra is invalid."""
        assert calc.get_extras_price(["YOGA"], "BASIC") is None


class TestSubtotal:
    """Tests for R3 subtotal."""

    def test_single_member(self, calc):
        """One member with BASIC plan and no extras costs 30."""
        assert calc.calculate_subtotal(30, 0, 1) == 30

    def test_multiple_members(self, calc):
        """Three members with BASIC plan and one extra costs 135."""
        assert calc.calculate_subtotal(30, 15, 3) == 135

    def test_zero_members_invalid(self, calc):
        """Zero members is invalid."""
        assert calc.calculate_subtotal(30, 0, 0) is None

class TestRounding:
    """Tests for R7."""

    def test_integer(self, calc):
        """An integer is unchanged."""
        assert calc.round_half_up(30) == 30

    def test_half_up(self, calc):
        """Half up rounds to the nearest integer."""
        assert calc.round_half_up(121.5) == 122

    def test_below_half(self, calc):
        """Values below half round down."""
        assert calc.round_half_up(121.4) == 121

    def test_above_half(self, calc):
        """Values above half round up."""
        assert calc.round_half_up(121.6) == 122
