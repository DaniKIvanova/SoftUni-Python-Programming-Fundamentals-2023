string = input()
new_string = ""
strength = 0

for i in range(len(string)):

    if strength > 0 and string[i] != ">":
        strength -= 1

    elif string[i] == ">":
        new_string += string[i]
        strength += int(string[i + 1])

    else:
        new_string += string[i]

print(new_string)

