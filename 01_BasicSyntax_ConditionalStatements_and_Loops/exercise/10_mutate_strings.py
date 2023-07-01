first_word = input()
second_word = input()
already_mutated = [first_word]
mutated_word = ""

for letter in range(len(first_word)):
    mutated_word = second_word[:letter + 1] + first_word[letter + 1:]
    if mutated_word not in already_mutated:
        print(mutated_word)
        already_mutated.append(mutated_word)