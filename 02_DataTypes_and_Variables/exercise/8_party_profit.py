group_size = int(input())
days_of_adventure = int(input())
coins = 0

for day in range(1, days_of_adventure + 1):
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    coins += 50 - (2 * group_size)  # 50 profit - 2 for food per member
    if day % 3 == 0:
        coins -= 3 * group_size  # spent for water
    if day % 5 == 0:  # boss killing
        coins += 20 * group_size
        if day % 3 == 0:  # if motivational party same day
            coins -= 2 * group_size
print(f"{group_size} companions received {coins // group_size} coins each.")