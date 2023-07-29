import re

dates_match = input()
pattern = re.compile(r"(^|(?<=\s))-?(0|[1-9][0-9]*)(\.\d+)?($|(?=\s))")
matches = pattern.finditer(dates_match)

for el in matches:
    print(el[0], end=" ")
    
