version = list(map(int, input().split(".")))
first_digit = version[0]
second_digit = version[1]
third_digit = version[2]

third_digit += 1
if third_digit == 10:
    second_digit += 1
    third_digit = 0
    if second_digit == 10:
        first_digit += 1
        second_digit = 0

print(f"{first_digit}.{second_digit}.{third_digit}")