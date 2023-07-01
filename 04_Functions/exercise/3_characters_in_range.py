def char_in_range(start, end):
    for char in range(ord(start) + 1, ord(end)):
        print(chr(char), end=" ")


start_symbol = input()
finish_symbol = input()
char_in_range(start_symbol, finish_symbol)