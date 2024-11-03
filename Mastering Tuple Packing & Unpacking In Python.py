# Task 1: 
# Customer Order Processing 
# Refine your skills in tuple unpacking by managing customer orders.


orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]



def unpacking():
   for name,product,quantity,*more_orders in orders:
      print(f"Name: {name}, Product: {product}, Quantity: {quantity} More Orders: {more_orders}")




unpacking()