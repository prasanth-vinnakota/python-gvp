
i = None
j = None
k = None
n = None

try:
    i = int(input("Enter X value: "))
    j = int(input("Enter Y value: "))
    k = int(input("Enter Z value: "))
    n = int(input("Enter N value: "))

    if i == 0 or j == 0 or k == 0:
        raise ValueError
except ValueError:
    print("input must be number and greater than zero")
    exit(1)

print('[', end="")
for a in range(i+1):
    for b in range(j+1):
        for c in range(k+1):
            if a+b+c != n:
                print([a, b, c], end=" ")

print('\b]')
