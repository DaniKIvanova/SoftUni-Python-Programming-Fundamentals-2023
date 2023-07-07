strings = input().split()
new_string = [string * len(string) for string in strings]

print(''.join(new_string))

