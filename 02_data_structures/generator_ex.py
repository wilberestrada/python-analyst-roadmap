# ex1
def squares_generator(n):
    for i in range(n):
        yield i**2

print("Result Squares List:")
print(list(squares_generator(5)))
gen = squares_generator(5)
print("Result Squares Generator:")
for value in gen:
    print(value)

# ex2
def even_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
print("Result Even List:")
print(list(even_generator(10)))
print("Result Even Generator:")
gen = even_generator(10)
for value in gen:
    print(value)

# ex3
def fibonacci_generator(n):
    a, b = 0, 1 # values by Fibonacci numbers
    count = 0 # counter

    while count < n:
        yield a # Produce sequence currect number
        a, b = b, a + b  # Calculate the next Fibonacci number
        count += 1

fib_sequence = list(fibonacci_generator(10))

print("List numbers Fibonacci are: ", fib_sequence)
