number_of_strings = int(input())
non_pure_symbols = [".", ",", "_"]
pureness = True

for string in range(number_of_strings):
    data_check = input()
    for symbol in non_pure_symbols:
        if symbol in data_check:
            pureness = False
    if pureness:
        print(f"{data_check} is pure.")
    else:
        print(f"{data_check} is not pure!")

    pureness = True