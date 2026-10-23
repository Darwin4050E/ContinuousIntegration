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
