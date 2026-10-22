"""Module for gym membership quote calculations."""


class Calculator:
    """Basic calculator class."""

    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtract two numbers."""
        return a - b


def apply_group_discount(subtotal: float, members: int) -> float:
    """R4: Apply 10% discount with 2 or more members."""
    if members >= 2:
        return subtotal * 0.9
    return subtotal


def apply_special_offer(amount: float) -> float:
    """R5: Subtract 50 if > 400, subtract 20 if > 200."""
    if amount > 400:
        return amount - 50
    if amount > 200:
        return amount - 20
    return amount


def apply_premium_surcharge(amount: float, has_premium_extra: bool) -> float:
    """R6: Add 15% surcharge if premium extra is selected."""
    if has_premium_extra:
        return amount * 1.15
    return amount

PLANS = {"BASIC": 30.0, "STANDARD": 45.0, "PREMIUM": 70.0}

def calculate_quote(plan: str) -> float:
    """Calculate the total quote by applying R1 to R7."""
    # R1. Plans. Any other plan is invalid.
    if plan not in PLANS:
        return -1.0
    
    return 0.0