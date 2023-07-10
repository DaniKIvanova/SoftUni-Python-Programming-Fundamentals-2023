def unique_symbols_digits(word):
    result = []
    for char in word:
        if not char.isdigit():
            if char.upper() not in result:
                result.append(char.upper())
    return len(result)


def digits_and_symbols(word, num_symbols):
    current_symbols = ''
    current_digit = ''
    final_word = ''

    while word:
        for i in range(len(word)):
            if not word[i].isdigit():
                current_symbols += word[i]
            else:
                word = word[i::]
                break
        for i in range(len(word)):
            if word[i].isdigit() and i == len(word) - 1:
                current_digit += word[i]
                word = ''
                break
            elif word[i].isdigit() and i != len(word) - 1:
                current_digit += word[i]
            else:
                word = word[i::]
                break
        final_word += (current_symbols * int(current_digit))
        current_symbols, current_digit = '', ''

    return f"Unique symbols used: {num_symbols}\n{final_word.upper()}"


starting_word = input()
unique_symbols = unique_symbols_digits(starting_word)
print(digits_and_symbols(starting_word, unique_symbols))

