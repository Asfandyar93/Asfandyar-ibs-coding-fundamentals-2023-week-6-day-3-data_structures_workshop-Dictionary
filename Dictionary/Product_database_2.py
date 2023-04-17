# Create a map with the following key-value pairs:

product_prices = {'Eggs': 200,
                  'Milk': 200,
                  'Fish': 400,
                  'Apples': 150,
                  'Bread': 50,
                  'Chicken': 550,
}

# Which products cost less than 201? (just the name)
for product, price in product_prices.items():
    if price < 201:
        print(product)

# Which products cost more than 150? (name + price)
for product, price in product_prices.items():
    if price > 150:
        print(product, price)

