receive_data = input()
new_word = ""
while receive_data != "End":
    if receive_data != "SoftUni":
        for letter in receive_data:
            new_word += letter+letter
        print(new_word)
    receive_data = input()
    new_word = ""