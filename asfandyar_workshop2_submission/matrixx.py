# Write a program that asks for an integer n,
# then it creates a two-dimensional array (of integers) of the specified
# size (nxn) with the value of 1 on the main diagonal and the value of 0
# everywhere else. Print the 2d array into the output
# Example:
# Please enter the array (matrix) size: 4
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

r = int(input("Enter the size of matrix: "))
for x in range(r):
    for y in range(r):
        if x == y:
            print(1, end="")
        else:
            print(0, end="")
    print()
