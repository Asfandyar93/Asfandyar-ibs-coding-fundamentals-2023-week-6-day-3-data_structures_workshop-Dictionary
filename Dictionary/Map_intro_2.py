# Create a map where the keys are strings and the values are strings with the following initial values

my_map = {
    "978-1-60309-452-8": "A Letter to Jo",
    "978-1-60309-459-7": "Lupus",
    "978-1-60309-444-3": "Red Panda and Moon Bear",
    "978-1-60309-461-0": "The Lab"
}

# Print all the key-value pairs in the following format
for isbn, title in my_map.items():
   print(f"{title} (ISBN: {isbn})")

# Remove the key-value pair with key 978-1-60309-444-3

for isbn, title in my_map.items():
    del my_map["978-1-60309-444-3"]
    break
# print(f"{title} (ISBN: {isbn})")
#
# # Remove the key-value pair with value The Lab
for key, value in my_map.items():
     if value == "The Lab":
        del my_map[key]
        break
# print(my_map)

# # Add the following key-value pairs to the map
my_map["978-1-60309-450-4"] = "They Called Us Enemy"
my_map["978-1-60309-453-5"] = "Why Did We Trust Him?"
# print(my_map)

# Print whether there is an associated value with key 478-0-61159-424-8 or not
try:
     del my_map['978-1-60309-444-3']
     print("True")
except KeyError:
    print("False")
#
# # Print the value associated with key 978-1-60309-453-5
print(my_map['978-1-60309-453-5'])