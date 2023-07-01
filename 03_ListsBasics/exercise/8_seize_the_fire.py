type_of_fire = input().split("#")
amount_of_water = int(input())
cells_extinguished = []
effort = 0

for fire in type_of_fire:
    fire = fire.split(" = ")
    type_current_fire = fire[0]
    power_current_fire = int(fire[1])

    if power_current_fire <= amount_of_water:
        if type_current_fire == "High":
            if 81 <= power_current_fire <= 125:
                amount_of_water -= power_current_fire
                effort += power_current_fire * 0.25
                cells_extinguished.append(power_current_fire)
        elif type_current_fire == "Medium":
            if 51 <= power_current_fire <= 80:
                amount_of_water -= power_current_fire
                effort += power_current_fire * 0.25
                cells_extinguished.append(power_current_fire)
        elif type_current_fire == "Low":
            if 1 <= power_current_fire <= 50:
                amount_of_water -= power_current_fire
                effort += power_current_fire * 0.25
                cells_extinguished.append(power_current_fire)

print("Cells:")

for cell in cells_extinguished:
    print(f" - {cell}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(cells_extinguished)}")