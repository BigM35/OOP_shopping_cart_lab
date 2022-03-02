
from product import Product


class ShoppingCart:
    def __init__(self):
        self.shopping_cart = []
    
    def add_product(self, product):
        self.shopping_cart.append(product)

    def total_price(self):
        for items in range(len(self.shopping_cart)):
            price += self.product_in_cart.product_price[items]
        return price

    def empty_cart(self):
        self.product_in_cart.clear()