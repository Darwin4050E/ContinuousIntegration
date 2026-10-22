"""Módulo para calcular la cuota de membresía del gym."""

class Calculator:
    """Clase para calcular el costo de una membresía basada en reglas."""

    def __init__(self):
        """Constructor de la clase con los diccionarios de información de precios."""
        
        self.plans = {
            "BASIC": 30.0,
            "STANDARD": 45.0,
            "PREMIUM": 70.0
        }

        self.extras_prices = {
            "GROUP_CLASSES": 15.0,
            "PERSONAL_TRAINING": 25.0,
            "SPA": 30.0,
            "SPECIALIZED_PROGRAM": 40.0
        }

        self.premium_extras = ["SPA", "SPECIALIZED_PROGRAM"]

    def calculate_quote(self, plan: str) -> float:
        """R1: Cuota calculada a partir del plan y validación de plan inválido."""
        
        if plan not in self.plans:
            return -1.0

        plan_price = self.plans[plan]

        return float(plan_price)
