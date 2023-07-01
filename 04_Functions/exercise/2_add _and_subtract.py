def sum_numbers(number_one, number_two):
    return number_one + number_two


def subtract(summed_number, number_three):
    return summed_number - number_three


def add_and_subtract(number_one, number_two, number_three):
    return subtract(sum_numbers(number_one, number_two), number_three)


num_one = int(input())
num_two = int(input())
num_three = int(input())

print(add_and_subtract(num_one, num_two, num_three))