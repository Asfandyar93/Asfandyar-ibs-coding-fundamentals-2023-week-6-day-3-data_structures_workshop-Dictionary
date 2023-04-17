# - Create a variable named `numbers`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Print the sum of the elements of `numbers`

x = [3, 4, 5, 6, 7]
sum = 0

for i in range(0,len(x)):
    sum = sum + x[i]

print("The sum of the list is",sum)