first_sequence = input().split(", ")
second_sequence = input().split(", ")

substrings = []

for substring in first_sequence:
    for string in second_sequence:
        if substring in string:
            if substring not in substrings:
                substrings.append(substring)
print(substrings)