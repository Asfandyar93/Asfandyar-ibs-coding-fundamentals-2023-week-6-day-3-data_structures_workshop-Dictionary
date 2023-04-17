# - Create an array variable named `orders`
#   with the following content: `["first", "second", "third"]`
# - Swap the first and the third element of `orders` programmatically
# - Print the swapped array into the console:
#   [third, second, first]

orders = ["first", "second", "third"]

index0, index2 = 0,2
orders[index0], orders[index2] = orders[index2],orders[index0]

print(orders)