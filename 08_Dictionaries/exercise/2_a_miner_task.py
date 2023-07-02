my_dict = {}

while True:
    command = input()

    if command == "stop":
        break

    quantity = int(input())

    if command not in my_dict:
        my_dict[command] = quantity
    else:
        my_dict[command] += quantity

for keys in my_dict:
    print(f"{keys} -> {my_dict[keys]}")

