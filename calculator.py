class Calculator:

    def add(self, a: float, b: float) -> float:
        return a + b


def apply_group_discount(subtotal: float, members: int) -> float:
    """R4: 10% de descuento con 2 o más miembros."""
    if members >= 2:
        return subtotal * 0.9
    return subtotal


def apply_special_offer(amount: float) -> float:
    """R5: Si > 400 resta 50; si > 200 resta 20; nunca los dos."""
    if amount > 400:
        return amount - 50
    if amount > 200:
        return amount - 20
    return amount


