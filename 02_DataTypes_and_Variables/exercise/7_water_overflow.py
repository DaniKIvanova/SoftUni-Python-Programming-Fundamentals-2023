tank_fullness = 0
number_of_lines = int(input())

for line in range(number_of_lines):
    water = int(input())
    if water <= 255 - tank_fullness:
        tank_fullness += water
    else:
        print("Insufficient capacity!")
print(tank_fullness)