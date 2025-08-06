# exercises.py
fruits = ["apple", "orange", "banana"]
fruits.append("mango")          # add
fruits[1] = "grape"             # modify
print(fruits)

# tuple unpacking
lat, lon = (34.05, -118.25)
print("Latitude:", lat)

# set operations
a = {1, 2, 3}
b = {3, 4}
print("Union:", a | b)          # {1, 2, 3, 4}
print("Difference:", a - b)     # {1, 2}

# dict update
prices = {"apple": 1.2, "orange": 0.8}
prices["banana"] = 0.5
for fruit, price in prices.items():
    print(f"{fruit}: ${price}")

# using enumerate()
for index,fruit in enumerate(fruits):
    print(f"Fruit {index + 1}: {fruit}")

# using zip()
stock = [10, 8, 5]
zipped = list(zip(fruits, stock))
print(zipped)


