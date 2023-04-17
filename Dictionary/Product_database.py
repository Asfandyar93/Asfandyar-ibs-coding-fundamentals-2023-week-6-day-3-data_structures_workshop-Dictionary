# Create a map with the following key-value pairs:

product_prices = {'Eggs': 200,
                  'Milk': 200,
                  'Fish': 400,
                  'Apples': 150,
                  'Bread': 50,
                  'Chicken': 550,
}
# How much is the fish?
a = product_prices.get("Fish")
print(a)

# What is the most expensive product?
b = max(product_prices, key=product_prices.get)
print(b)

# What was the average amount of our spendings? (print this as a float value)
total = sum(product_prices.values())
items = len(product_prices)
average = total/items
print(average)

# How many products' price is below 300?
count = 0

for price in product_prices.values():
    if price < 300:
        count = count + 1
print(count)

# Is there anything we can buy for exactly 125?
for product, price in product_prices.items():
    if price == 125:
        print("Yes")
        break
else:
    print("No")

# What is the cheapest product?
c = min(product_prices, key=product_prices.get)
print(c)
