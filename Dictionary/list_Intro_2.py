# Create a list ('List A') which contains the following values
list_A = ["Apple", "Avocado", "Blueberries", "Durian", "Lychee"]

# Create a new list ('List B') with the values of List A
list_B = ["Apple", "Avocado", "Blueberries", "Durian", "Lychee"]

# Print out whether List A contains "Durian" or not
print("Durian" in list_A)

# Remove "Durian" from List B
list_B.remove("Durian")
# print(list_A)

# Add "Kiwifruit" to List A after the 4th element
list_A.insert(4,"Kiwifruit")
# print(list_A)

# Compare the size of List A and List B
print("List A is greater than List B:", len(list_A) > len(list_B))

# Get the index of "Avocado" from List A
avacado_index = list_A.index("Avocado")
print(avacado_index)

# Get the index of "Durian" from List B

index = list_B.index("Durian") \
    if "Durian" in list_B else -1
print(index)

# Add "Passion Fruit" and "Pomelo" to List B in a single statement
list_B.extend(["Passion Fruit", "Pomelo"])
# print(list_B)

# Print out the 3rd element from List A
print(list_A[2])

# Print all elements of List A
print(list_A)

# Print all elements of List B
print(list_B)

