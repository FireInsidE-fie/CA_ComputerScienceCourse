# https://www.codecademy.com/paths/computer-science/tracks/cspath-cs-101/modules/cspath-python-lists/projects/python-lens-slice

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slice = prices.count(2)

num_pizzas = len(toppings)

print("We sell", num_pizzas, "different kinds of pizza!")

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

print(pizza_and_prices)

pizza_and_prices = sorted(pizza_and_prices)
print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]

priciest_pizza = pizza_and_prices[-1]

pizza_and_prices.pop()

pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
