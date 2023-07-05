force = {}

while True:
    command = input()
    side_num = 0
    user_num = 0

    if command == "Lumpawaroo":
        break

    if "|" in command:
        side, user = command.split(" | ")

        for key, value in force.items():
            if key == side:
                side_num += 1
            if user in value:
                user_num += 1

        if side_num == user_num == 0:
            force[side] = []
            force[side].append(user)

        if side_num > 0 and user_num == 0:
            force[side].append(user)

    elif "->" in command:
        user, side = command.split(" -> ")

        for key, value in force.items():
            if user in value:
                force[key].remove(user)
            if side == key:
                side_num += 1

        if side_num == user_num == 0:
            force[side] = []
            force[side].append(user)

        if side_num > 0 and user_num == 0:
            force[side].append(user)

        print(f"{user} joins the {side} side!")

for key, value in force.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")

        for i in range(len(value)):
            print(f"! {value[i]}")

