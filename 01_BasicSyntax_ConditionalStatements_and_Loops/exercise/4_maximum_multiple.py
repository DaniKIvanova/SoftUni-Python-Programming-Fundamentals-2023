divisor = int(input())
bound = int(input())

max_num = 0

for num in range(1, bound + 1):
    if num % divisor == 0:
        max_num = num

print(max_num)