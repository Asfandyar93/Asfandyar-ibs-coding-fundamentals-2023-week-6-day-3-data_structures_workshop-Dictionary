# - Create a variable named `numbers`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Reverse the order of the elements of `numbers` programmatically
# - Print the elements of the reversed `numbers`:
#   [7, 6, 5, 4, 3]

a = [3,4,5,6,7]

b = reversed(a)

c = []

for element in b:
    c.append(element)
print(c)