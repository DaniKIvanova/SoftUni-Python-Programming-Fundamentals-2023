numbers_for_robbing = list(map(int, input().split(", ")))
numbers_of_beggars = int(input())

lst_beggars = [0] * numbers_of_beggars
counter = 0

for number in range(len(numbers_for_robbing)):
    lst_beggars[counter] += numbers_for_robbing[number]
    counter += 1
    if counter >= numbers_of_beggars:
        counter = 0

print(lst_beggars)