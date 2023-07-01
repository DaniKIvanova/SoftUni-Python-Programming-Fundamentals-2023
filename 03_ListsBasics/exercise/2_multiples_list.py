factor = int(input())
count = int(input())
multiplies = [factor]

for _ in range(1, count):
    multiplies.append(factor + multiplies[-1])

print(multiplies)
