from shopping_cart import ShoppingCart



class Customer:
    def __init__(self,c_name):
        self.customer_name = c_name
        self.customer_cart = []

    def add_to_customers_cart(self):
        self.customer_cart = ShoppingCart.shopping_cart

    def view_all_product(self):
        for item in range(len(self.customer_cart)):
            print(self.customer_cart[item])