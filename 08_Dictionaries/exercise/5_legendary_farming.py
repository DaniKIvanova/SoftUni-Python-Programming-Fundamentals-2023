inventory = {"shards": 0, "fragments": 0, "motes": 0}
legendary = False

while not legendary:
    farming = input().split(" ")

    for el in range(0, len(farming), 2):
        value = int(farming[el])
        key = farming[el + 1].lower()

        if key not in inventory.keys():
            inventory[key] = 0
        inventory[key] += value
        
        if inventory["shards"] >= 250:
            print("Shadowmourne obtained!")
            legendary = True
            inventory["shards"] -= 250
        elif inventory["fragments"] >= 250:
            print("Valanyr obtained!")
            legendary = True
            inventory["fragments"] -= 250
        elif inventory["motes"] >= 250:
            print("Dragonwrath obtained!")
            legendary = True
            inventory["motes"] -= 250

        if legendary:
            break

for key, value in inventory.items():
    print(f"{key}: {value}")

