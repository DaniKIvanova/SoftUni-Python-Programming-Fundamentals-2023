awake_info = input()
coffee_cups = 0

while awake_info != "END":
    if awake_info in ["cat", "dog", "movie", "coding"]:
        coffee_cups += 1
    elif awake_info in ["CAT", "DOG", "MOVIE", "CODING"]:
        coffee_cups += 2
    awake_info = input()

if coffee_cups > 5:
    print("You need extra sleep")
else:
    print(coffee_cups)