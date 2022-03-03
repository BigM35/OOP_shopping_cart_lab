from customer import Customer
from product import Product


customer_one = Customer("Jim")

banana = Product("Banana", 5.99, "Fruits")
mre = Product("M.R.E.", 100, "Nasty")
tv = Product("Television", 700, "Appliances")
Gum = Product("Gum", .99, "snack")

print(customer_one.customer_name)

customer_one.add_to_customers_cart(banana)
customer_one.add_to_customers_cart(mre)
customer_one.add_to_customers_cart(tv)

customer_one.view_all_product()
customer_one.customer_cart.add_total_price()

customer_one.customer_cart.empty_cart()
print(customer_one.customer_cart.empty_cart())