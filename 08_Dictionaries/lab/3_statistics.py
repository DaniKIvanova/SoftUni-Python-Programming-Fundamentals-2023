stock = {}

while True:
    command = input()
    if command == "statistics":
        break

    product, quantity = command.split(": ")
    if product in stock:
        stock[product] += int(quantity)
    else:
        stock[product] = int(quantity)

print("Products in stock:")
for key, value in stock.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {sum(stock.values())}")
