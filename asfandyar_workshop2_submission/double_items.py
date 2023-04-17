# - Create an array variable named `numbers`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Double all the values in the array and print the modified
#   array to the console as:
#   [6, 8, 10, 12, 14]

numbers = [3, 4, 5, 6, 7]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)