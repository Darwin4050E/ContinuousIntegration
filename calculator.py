"""Module for gym membership quote calculations."""


class Calculator:
    """Gym membership quote calculator."""

    # R1: plan catalog
    PLANS = {
        "BASIC": 30,
        "STANDARD": 45,
        "PREMIUM": 70,
    }

    # R2: extras catalog
    EXTRAS = {
        "GROUP_CLASSES": (15, False),
        "PERSONAL_TRAINING": (25, False),
        "SPA": (30, True),
        "SPECIALIZED_PROGRAM": (40, True),
    }

    def get_plan_price(self, plan: str):
        """R1: Return the plan price, or None if the plan is invalid."""
        return self.PLANS.get(plan)

    def apply_group_discount(self, subtotal: float, members: int) -> float:
        """R4: Apply 10% discount with 2 or more members."""
        if members >= 2:
            return subtotal * 0.9
        return subtotal


    def apply_special_offer(self, amount: float) -> float:
        """R5: Subtract 50 if > 400, subtract 20 if > 200."""
        if amount > 400:
            return amount - 50
        if amount > 200:
            return amount - 20
        return amount


    def apply_premium_surcharge(self, amount: float, has_premium_extra: bool) -> float:
        """R6: Add 15% surcharge if premium extra is selected."""
        if has_premium_extra:
            return amount * 1.15
        return amount
