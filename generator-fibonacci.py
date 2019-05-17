def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        yield a
        a, b = b, a + b


size = None
try:
    size = int(input("Enter size of fibonacci series: "))
    if size == 0:
        raise ValueError

except ValueError:
    print("input must be a number and greater than 0")
    exit(0)

for j in fibonacci(size):
    print(j, end=" ")
