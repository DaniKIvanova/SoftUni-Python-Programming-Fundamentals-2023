first_string, second_string = input().split()
first = len(first_string)
second = len(second_string)
total_sum = 0

if first == second:
    for i in range(first):
        total_sum += ord(first_string[i]) * ord(second_string[i])

elif first > second:
    for i in range(second):
        total_sum += ord(first_string[i]) * ord(second_string[i])
    diff = first - second
    for i in range(diff):
        total_sum += ord(first_string[-1 - i])

elif first < second:
    for i in range(first):
        total_sum += ord(first_string[i]) * ord(second_string[i])
    diff = second - first
    for i in range(diff):
        total_sum += ord(second_string[-1 - i])

print(total_sum)

