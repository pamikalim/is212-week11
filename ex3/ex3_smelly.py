class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self):
        discount = self.DISCOUNT_RATE
        discounted_price = self.price - (self.price * discount)
        print(f"Discounted price for {self.name} ({self.CATEGORY}): {discounted_price}")
        return discounted_price

    def calculate_tax(self):
        tax_rate = self.TAX_RATE
        tax = self._round_tax(self.price * tax_rate)
        print(f"Tax for {self.name} ({self.CATEGORY}): {tax}")
        return tax

    def _round_tax(self, tax):
        return tax

class Electronics(Product):
    CATEGORY = "Electronics"
    DISCOUNT_RATE = 0.10  # 10% discount
    TAX_RATE = 0.15  # 15% tax

class Clothing(Product):
    CATEGORY = "Clothing"
    DISCOUNT_RATE = 0.20  # 20% discount
    TAX_RATE = 0.08  # 8% tax

class Grocery(Product):
    CATEGORY = "Grocery"
    DISCOUNT_RATE = 0.05  # 5% discount
    TAX_RATE = 0.02  # 2% tax

    def _round_tax(self, tax):
        return round(tax, 2)

