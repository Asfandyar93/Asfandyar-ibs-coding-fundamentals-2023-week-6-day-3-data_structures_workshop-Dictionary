# - Create a variable named `numbers`
#   with the following content: `[54, 23, 66, 12]`
# - Print the sum of the second and the third element

numbers = [54, 23, 66, 12]
sum = 0

for i in range(1,3):
    sum = sum + numbers[i]

print("The sum is",sum)
