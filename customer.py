from shopping_cart import ShoppingCart



class Customer:
    def __init__(self,c_name):
        self.customer_name = c_name
        self.customer_cart = ShoppingCart()

    def add_to_customers_cart(self, product):
        self.customer_cart.add_product(product)

    def view_all_product(self):
        for att in range(len(self.customer_cart.shopping_cart)):
            print(self.customer_cart.shopping_cart[att])