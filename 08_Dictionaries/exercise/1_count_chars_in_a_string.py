data = [char for char in str(input()) if char != " "]
count = {}

for ch in data:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

for el in count:
    print(f"{el} -> {count[el]}")
