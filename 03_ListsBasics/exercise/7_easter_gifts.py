gifts = input().split()
command = input()

while command != "No Money":
    command = command.split()

    if command[0] == "OutOfStock":
        for gift in range(len(gifts)):
            if gifts[gift] == command[1]:
                gifts[gift] = "None"
    elif command[0] == "Required":
        if 0 < int(command[2]) < len(gifts):
            gifts[int(command[2])] = command[1]
    elif command[0] == "JustInCase":
        gifts[-1] = command[1]
    command = input()

print(" ".join(x for x in gifts if x != "None"))