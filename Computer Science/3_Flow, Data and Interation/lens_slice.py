toppings = ['pepperoni',
'pineapple',
'cheese',
'sausage',
'olives',
'anchovies',
'mushrooms']

prices = [2,
6,
1,
3,
2,
7,
2]

num_pizzas = len(toppings)
print("We sell {} different kinds of pizza!".format(num_pizzas))

pizzas = list(zip(toppings,prices))
print(pizzas)
print()
pizzas.sort(key=lambda x: x[1])
print(pizzas)
print()
cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]

three_cheapest = pizzas[:3]
print(three_cheapest)
print()
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)