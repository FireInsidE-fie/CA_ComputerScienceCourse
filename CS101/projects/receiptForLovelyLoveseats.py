# https://www.codecademy.com/paths/computer-science/tracks/cspath-cs-101/
# modules/cspath-python-hello-world/projects/python-furniture-store

# Defining articles...
lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood.
32 inches high x 40 inches wide x 30 inches deep. Red or white."""
lovely_loveseat_price = 254.00

stylish_settee_description = """Stylish Settee. Faux leather on birch.
29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""
stylish_settee_price = 180.50

luxurious_lamp_description = """Luxiurious Lamp. Glass and iron. 36 inches tall.
Brown with cream shade."""
luxurious_lamp_price = 52.15

sales_tax = .088

# Preparing total price and itemization variables...
customer_one_total = 0
customer_one_itemization = ""

# Customer one buys the Lovely Loveseat.
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

# Customer one also buys the Luxurious Lamp.
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

# Checking out...
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

print("Customer One Items:")  # Itemization header
print(customer_one_itemization)
print("Customer One Total:")  # Total price header
print(customer_one_total)
