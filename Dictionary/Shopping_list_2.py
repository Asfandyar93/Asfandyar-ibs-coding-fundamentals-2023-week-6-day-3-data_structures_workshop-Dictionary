# Represent the following products with their prices:
prices = {
    "Milk": 1.07,
    "Rice": 1.59,
    "Eggs": 3.14,
    "Cheese": 12.60,
    "Chicken Breasts": 9.40,
    "Apples": 2.31,
    "Tomato": 2.58,
    "Potato": 1.75,
    "Onion": 1.10
}

# Represent Bob's shopping list:
bob_shopping_list = {
    'Milk': 3,
    'Rice': 2,
    'Eggs': 2,
    'Cheese': 1,
    'Chicken Breasts': 4,
    'Apples': 1,
    'Tomato': 2,
    'Potato': 1
}

# Represent Alice's shopping list:
Alice_shopping_list = {
    'Rice': 1,
    'Eggs': 5,
    'Chicken Breasts': 2,
    'Apples': 1,
    'Tomato': 10
}
#
# How much does Bob pay?
total_cost = 0
for product, amount in bob_shopping_list.items():
    cost = prices[product]
    total_cost = total_cost + cost * amount
print("Bob's total cost is ",total_cost)

# How much does Alice pay?
total_cost = 0
for product, amount in Alice_shopping_list.items():
    cost = prices[product]
    total_cost = total_cost + cost * amount
print("Alice's total cost is ",total_cost)

# Who buys more Rice?
bob_r = bob_shopping_list.get("Rice")
alice_r = Alice_shopping_list.get("Rice")

if bob_r > alice_r:
    print("Bob")
else:
    print("Alice")

# Who buys more Potato?
bob_p = bob_shopping_list.get("Potato", 0)
alice_p = Alice_shopping_list.get("Potato", 0)

if bob_p > alice_p:
    print("Bob")
else:
    print("Alice")

# Who buys more Ham?
bob_h = bob_shopping_list.get("Ham", 0)
alice_h = Alice_shopping_list.get("Ham", 0)

if bob_h > alice_h:
    print("Bob")
elif bob_h > alice_h:
    print("Alice")
else:
    print("No one")

# Who buys more Apples?
bob_a = bob_shopping_list.get("Apples", 0)
alice_a = Alice_shopping_list.get("Apples", 0)

if bob_a > alice_a:
    print("Bob")
elif bob_h > alice_h:
    print("Alice")
else:
    print("No one")

# Who buys more of different products?
if len(bob_shopping_list.keys()) > len(Alice_shopping_list.keys()):
    print("Bob")
else:
    print("Alice bought more items.")

# Who buys more items? (more pieces)
bob_pieces = sum(bob_shopping_list.values())
alice_pieces = sum(Alice_shopping_list.values())

if bob_pieces > alice_pieces:
    print("Bob")
else:
    print("Alice")

