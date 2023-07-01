def perfect_num(digit):
    perfect_number = True
    sum_of_digits = 0
    for digits in range(1, digit):
        if digit % digits == 0:
            sum_of_digits += digits
    if digit != sum_of_digits:
        perfect_number = False

    if perfect_number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number_for_check = int(input())
print(perfect_num(number_for_check))