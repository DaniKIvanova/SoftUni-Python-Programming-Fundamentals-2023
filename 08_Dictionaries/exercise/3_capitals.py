country = input().split(", ")
city = input().split(", ")

for key, value in zip(country, city):
    print(f"{key} -> {value}")

