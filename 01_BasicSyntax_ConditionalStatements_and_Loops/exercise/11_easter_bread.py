cooking_budget = float(input())
price_for_flour = float(input())

price_one_pack_eggs = price_for_flour * 0.75
milk_liter_price = (price_for_flour * 0.25) + price_for_flour

one_bread_price = price_one_pack_eggs + price_for_flour + (milk_liter_price * 0.25)
loaves = cooking_budget // one_bread_price
colored_eggs = 0

for count in range(1, int(loaves) + 1):
    colored_eggs += 3
    if count % 3 == 0:
        colored_eggs -= count - 2

print(f"You made {int(loaves)} loaves of Easter bread! Now you have {colored_eggs} eggs and "
      f"{cooking_budget - (loaves * one_bread_price):.2f}BGN left.")