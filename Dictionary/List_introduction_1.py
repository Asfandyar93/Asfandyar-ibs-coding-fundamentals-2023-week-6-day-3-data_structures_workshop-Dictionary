# Create an empty list which will contain names (strings)
names = []

# Print out the number of elements in the list
print(len(names))

# Add "William" to the list
names.append("William")
print(names)

# Print out whether the list is empty or not
if len(names) == 0:
    print("list is empty")
else:
    print("list is not empty")

# Add "John" to the list
names.append("John")

# Add "Amanda" to the list
names.append("Amanda")

# Print out the number of elements in the list
print(len(names))

# Print out the 3rd element
print(names[2])

# Iterate through the list and print out each name
for index,val in enumerate(names):
    print(val)

# Iterate through the list and print
for index,val in enumerate(names):
    print(f"{index + 1}.{val}")

# Remove the 2nd element
names.pop(1)
# print(names)

# Iterate through the list in a reversed order and print out each name
for names in reversed(names):
    print(names)

# Remove all elements
names = []

# Print out the number of elements in the list
print(len(names))