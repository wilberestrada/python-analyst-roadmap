# exercises.py
fruits = ["apple", "banana", "orange", "blueberries"]
fruits.append("mango")          # add
fruits[1] = "grape"             # modify
print("\nList representiton")
print(fruits)

# tuple unpacking
lat, lon = (34.05, -118.25)
print("\nTuple representiton")
print("Latitude:", lat)

# set operations
a = {1, 2, 3}
b = {3, 4}
print("Union:", a | b)          # {1, 2, 3, 4}
print("Difference:", a - b)     # {1, 2}

# dict update
print("\nSet representiton")
prices = {"apple": 1.2, "orange": 0.8}
prices["banana"] = 0.5
for fruit, price in prices.items():
    print(f"{fruit}: ${price}")

# using enumerate()
print("\nUsing ZIP()")
for index,fruit in enumerate(fruits):
    print(f"Fruit {index + 1}: {fruit}")

# using zip()
print("\nUsing ZIP()")
stock = [10, 8, 5]
zipped = list(zip(fruits, stock))
for prod, qty in zipped:
    print(f"{prod}: {qty}")

print("\nEnumerate example:")
for idx, fruit in enumerate(fruits, start=1):
    print(f"{idx}. {fruit}")

# comprehension: dict mapping fruit to length
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print("\nFruit lengths:", fruit_lengths)
print("\n")

# dict comprehensions
products = ["apple", "banana", "orange", "blueberries"]
prices   = [1.2, 0.5, 0.8, 3.2]
discounted = [round(p*0.9, 2) for p in prices if p > 1.0]
print(discounted)
price_map = {prod: price for prod, price in zip(products, prices)}
print(price_map)
premium = {prod for prod, price in zip(products, prices) if price > 2.0}
print(premium)

