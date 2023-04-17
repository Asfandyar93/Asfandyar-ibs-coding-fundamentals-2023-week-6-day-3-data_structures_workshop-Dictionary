# Create a list with the following items:
Expenses = [500, 1000, 1250, 175, 800, 120]

# How much did we spend?
total_spending = sum(Expenses)
print(total_spending)

# Which was our greatest expense?
a = max(Expenses)
print(a)

# Which was our cheapest spending?
b = min(Expenses)
print(b)

# What was the average amount of our spendings? (print this as a float value)
c = total_spending/len(Expenses)
print("The average amount of our spendings " + str(c))

