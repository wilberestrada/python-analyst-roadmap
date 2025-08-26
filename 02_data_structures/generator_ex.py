# ex1
def squares_generator(n):
    for i in range(n):
        yield i**2

gen = squares_generator(5)
print("Result Squares Generator:")
for value in gen:
    print(value)


# ex2
def even_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
print("Result Even Generator:")
gen = even_generator(10)
for value in gen:
    print(value)