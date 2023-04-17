# Create an empty map where the keys are integers and the values are characters
my_map = dict()
my_map = {}

# Print out whether the map is empty or not
if bool(my_map):
    print("The map is not empty")
else:
    print("The map is empty")

# Add the following key-value pairs to the map
my_map = {97: 'a',
          98: 'b',
          99: 'c',
          65: 'A',
          66: 'B',
          67: 'C',
          68:'D'}

# Print all the keys
key_list = [key for key in my_map]
print(key_list)

# Print all the values
val_list = list(my_map.values())
print(val_list)

# Print how many key-value pairs are in the map
print(len(my_map))

# Print the value that is associated with key 99
val = my_map.get(99)
print(val)

# Remove the key-value pair with key 97 and print the associated value
val = my_map.pop(97)
print(val)

# Print whether there is an associated value with key 100 or not
if 100 in my_map:
    print("True")
else:
    print("False")

# Remove all the key-value pairs
my_map.clear()
print(my_map)

# Print how many key-value pairs are in the map
print(len(my_map))
