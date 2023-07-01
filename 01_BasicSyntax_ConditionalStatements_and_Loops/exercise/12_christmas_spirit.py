quantity_of_decorations = int(input())
days_till_christmas = int(input())
christmas_spirit = 0
shopping_costs = 0

for day in range(1, days_till_christmas + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        shopping_costs += 2 * quantity_of_decorations
        christmas_spirit += 5
    if day % 3 == 0:
        shopping_costs += 8 * quantity_of_decorations
        christmas_spirit += 13
    if day % 5 == 0:
        shopping_costs += 15 * quantity_of_decorations
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        shopping_costs += 23
        christmas_spirit -= 20
        if days_till_christmas == day:
            christmas_spirit -= 30
print(f"Total cost: {shopping_costs}")
print(f"Total spirit: {christmas_spirit}")