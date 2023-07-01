number_of_electrons = int(input())
shells = []
counter = 1

while number_of_electrons != 0:
    formula = 2 * (counter ** 2)
    if number_of_electrons >= formula:
        shells.append(formula)
    else:
        shells.append(number_of_electrons)
        break
    number_of_electrons -= formula
    counter += 1
print(shells)