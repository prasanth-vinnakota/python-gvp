
n = int(input("Enter n :"))

lst = []

for i in range(n):
    lst.append(int(input()))

winner = max(lst)

while max(lst) == winner:
    lst.remove(winner)

print(max(lst))

