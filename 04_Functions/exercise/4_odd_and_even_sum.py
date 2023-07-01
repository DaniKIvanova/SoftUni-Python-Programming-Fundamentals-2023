def odd_even_sum(number):
    odd_sum = 0
    even_sum = 0
    for digit in number:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    return even_sum, odd_sum


number_for_summing = input()

even_num, odd_num = odd_even_sum(number_for_summing)
print(f"Odd sum = {odd_num}, Even sum = {even_num}")