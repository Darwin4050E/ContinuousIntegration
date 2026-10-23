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

class TestGroupDiscountMethod:
    """R4 as a Calculator method."""

    def test_one_member_no_discount(self, calc):
        """One member does not get a discount."""
        assert calc.apply_group_discount(90, 1) == 90

    def test_two_members_apply_discount(self, calc):
        """Two members get a 10% discount."""
        assert calc.apply_group_discount(90, 2) == pytest.approx(81.0)

    def test_three_members_apply_discount(self, calc):
        """Three members get a 10% discount."""
        assert calc.apply_group_discount(135, 3) == pytest.approx(121.5)

    def test_boundary_exactly_two_members(self, calc):
        """Two members at the boundary get a 10% discount."""
        assert calc.apply_group_discount(100, 2) == pytest.approx(90.0)


class TestSpecialOfferMethod:
    """R5 as a Calculator method."""

    def test_below_200_no_discount(self, calc):
        """Amounts below 200 do not get a discount."""
        assert calc.apply_special_offer(81) == 81

    def test_exactly_200_no_discount(self, calc):
        """200 is NOT > 200, so no discount."""
        assert calc.apply_special_offer(200) == 200

    def test_above_200_subtract_20(self, calc):
        """Amounts above 200 get 20 subtracted."""
        assert calc.apply_special_offer(306) == pytest.approx(286.0)

    def test_exactly_400_subtract_20(self, calc):
        """400 is NOT > 400, so subtract 20."""
        assert calc.apply_special_offer(400) == pytest.approx(380.0)

    def test_above_400_subtract_50(self, calc):
        """Amounts above 400 get 50 subtracted."""
        assert calc.apply_special_offer(450) == pytest.approx(400.0)


class TestPremiumSurchargeMethod:
    """R6 as a Calculator method."""

    def test_no_premium_no_surcharge(self, calc):
        """No premium extra does not add a surcharge."""
        assert calc.apply_premium_surcharge(286, False) == pytest.approx(286.0)

    def test_with_premium_adds_15_percent(self, calc):
        """A premium extra adds a 15% surcharge."""
        assert calc.apply_premium_surcharge(200, True) == pytest.approx(230.0)

    def test_large_amount(self, calc):
        """A large amount with premium extra adds 15%."""
        assert calc.apply_premium_surcharge(400, True) == pytest.approx(460.0)

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
