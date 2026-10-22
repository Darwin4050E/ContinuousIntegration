class Calculator:

    def __init__(self):
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

    def calculate_quote(self, plan: str, extras: list, members: int) -> float:
        
        # R1. Plans
        if plan not in self.plans:
            return -1.0

        plan_price = self.plans[plan]

        return float(plan_price)
