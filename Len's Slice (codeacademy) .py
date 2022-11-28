#Established variables:
toppings = ["pepperoni", "pineapple", "cheeses", "sausauge", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

#How many $2 pizzas
num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)

#Print statement
print("We sell ", num_pizzas , " different kinds of pizza!")

#New list generated - 2D
pizza_and_prices = [
  [2, "pepperoni"],
  [6, "pineapple"],
  [1, "cheese"],
  [3, "sausage"],
  [2, "olives"],
  [7, "anchovies"],
  [2, "mushrooms"]
]

#sorted by price
pizza_and_prices.sort()
#print(pizza_and_prices)

#new variables
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

#Most expensive pizza was purchased
pizza_and_prices.pop()

#New topping added
pizza_and_prices.append([2.5, "peppers"])
pizza_and_prices.sort()
print(pizza_and_prices)

#We giveaway 3 of our cheapest pizzas
three_cheapest = pizza_and_prices[:2]
print(three_cheapest)

#Final Inventory
final_pizza_and_prices = pizza_and_prices[2:]
print(final_pizza_and_prices)

#Final print
print("Our final inventory consists of ", final_pizza_and_prices, ".")
