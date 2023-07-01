working_events = input().split("|")
energy = 100
coins = 100
gained_energy = 0
bakery_open = True

for day in working_events:
    event = day.split("-")[0]
    amount_of_event = int(day.split("-")[1])

    if event == "rest":
        energy += amount_of_event
        if energy <= 100:
            print(f"You gained {amount_of_event} energy.")
            print(f"Current energy: {energy}.")
        else:
            gained_energy = abs(amount_of_event - (energy - 100))
            if energy > 100:
                energy = 100
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {energy}.")
    elif event == "order":
        if energy >= 30:
            energy -= 30
            coins += amount_of_event
            print(f"You earned {amount_of_event} coins.")
        else:
            print("You had to rest!")
            energy += 50
            if energy > 100:
                energy = 100
    else:
        if coins >= amount_of_event:
            coins -= amount_of_event
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            bakery_open = False
            break

if bakery_open:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")