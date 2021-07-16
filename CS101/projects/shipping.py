# https://www.codecademy.com/paths/computer-science/tracks/cspath-cs-101/
# modules/cspath-python-control-flow/projects/python-sals-shipping

weight = input("Please input the weight in pounds of your package : ")
# Ground shipping
if weight <= 2:
    print("Ground shipping cost :", 20 + (1.50 * weight))
elif weight <= 6:
    print("Ground shipping cost :", 20 + (3.00 * weight))
elif weight <= 10:
    print("Ground shipping cost :", 20 + (4.00 * weight))
else:
    print("Ground shipping cost :", 20 + (4.75 * weight))

# Ground shipping premium
print("Ground shipping premium cost :", 125)

# Drone shipping
if weight <= 2:
    print("Ground shipping cost :", 4.50 * weight)
elif weight <= 6:
    print("Ground shipping cost :", 9.00 * weight)
elif weight <= 10:
    print("Ground shipping cost :", 12.00 * weight)
else:
    print("Ground shipping cost :", 14.25 * weight)
