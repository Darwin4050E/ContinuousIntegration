"""Unit tests for calculator module."""
from calculator import Calculator


class TestPlans:
    """Tests for R1 plan catalog."""

    calc: Calculator

    def setup_method(self):
        """Provide a clean Calculator instance for each test."""
        self.calc = Calculator()

    def test_basic(self):
        """BASIC plan costs 30."""
        assert self.calc.get_plan_price("BASIC") == 30

    def test_standard(self):
        """STANDARD plan costs 45."""
        assert self.calc.get_plan_price("STANDARD") == 45

    def test_premium(self):
        """PREMIUM plan costs 70."""
        assert self.calc.get_plan_price("PREMIUM") == 70

    def test_invalid(self):
        """Unknown plan returns None."""
        assert self.calc.get_plan_price("GOLD") is None

class TestExtras:
    """Tests for R2."""

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
        """A premium extra on a PREMIUM plan costs 30 and flags premium."""
        assert calc.get_extras_price(["SPA"], "PREMIUM") == (30, True)

    def test_premium_with_basic_is_invalid(self, calc):
        """A premium extra on a BASIC plan is invalid."""
        assert calc.get_extras_price(["SPA"], "BASIC") is None

    def test_unknown_extra_is_invalid(self, calc):
        """An unknown extra is invalid."""
        assert calc.get_extras_price(["YOGA"], "BASIC") is None
