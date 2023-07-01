def factorial_calculator(number):
    factorial_number = 1
    for num in range(1, number + 1):
        factorial_number *= num
    return factorial_number


first_number = int(input())
second_number = int(input())

division_of_numbers = factorial_calculator(first_number) / factorial_calculator(second_number)
print(f"{division_of_numbers:.2f}")