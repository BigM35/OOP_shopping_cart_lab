
from product import Product


class ShoppingCart:
    def __init__(self):
        self.shopping_cart = []
        self.total_price = 0 
    
    def add_product(self, product):
        self.shopping_cart.append(product)

    def add_total_price(self):
        for item in self.shopping_cart:
            self.total_price += item.product_price
        print(self.total_price)

    def empty_cart(self):
        self.shopping_cart.clear()