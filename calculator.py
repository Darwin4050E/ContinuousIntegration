class Calculator:

    def add(self, a: float, b: float) -> float:
        return a + b


def apply_group_discount(subtotal: float, members: int) -> float:
    """R4: 10% de descuento con 2 o más miembros."""
    if members >= 2:
        return subtotal * 0.9
    return subtotal