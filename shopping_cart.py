
from product import Product


class ShoppingCart:
    def __init__(self):
        self.shopping_cart = []
    
    def add_product(self, product):
        self.shopping_cart.append(product)

    def total_price(self):
        price = 0
        for items in range(len(self.shopping_cart)):
            price += self.shopping_cart[items].product_price()
        return price

    def empty_cart(self):
        self.product_in_cart.clear()