items_for_sale = input().split("|")
budget = float(input())
new_item_prices = []
old_item_prices = []

for item in items_for_sale:
    current_item = item.split("->")[0]
    price_item = float(item.split("->")[1])

    if current_item == "Clothes" and price_item <= 50:
        if budget >= price_item:
            budget -= price_item
            new_item_prices.append(price_item + (price_item * 0.4))
            old_item_prices.append(price_item)
    elif current_item == "Shoes" and price_item <= 35:
        if budget >= price_item:
            budget -= price_item
            new_item_prices.append(price_item + (price_item * 0.4))
            old_item_prices.append(price_item)
    elif current_item == "Accessories" and price_item <= 20.50:
        if budget >= price_item:
            budget -= price_item
            new_item_prices.append(price_item + (price_item * 0.4))
            old_item_prices.append(price_item)

profit = sum(new_item_prices) - sum(old_item_prices)

print(" ".join(f"{x:.2f}" for x in new_item_prices))
print(f"Profit: {profit:.2f}")

if budget + sum(new_item_prices) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")