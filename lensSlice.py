# Define lists of pizza toppings and prices
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

# Modify lists according to instructions
# Find how many 2 dollar slices we sell
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Find how many toppings we offer
num_pizzas = len(toppings)
print(f"We sell {num_pizzas} different kinds of pizza!")

# Sort by slice price
pizza_and_prices.sort()

# Find the cheapest pizza
cheapest_pizza = pizza_and_prices[0]

# Find the most expensive pizza
priciest_pizza = pizza_and_prices[-1]

# Sold out of anchovies (our most expensive slice). Remove it from the list.
pizza_and_prices.pop()

# Got a new topping, peppers. Insert it at the right spot.
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

# Find 3 cheapest slices for our poor mouse friends
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)