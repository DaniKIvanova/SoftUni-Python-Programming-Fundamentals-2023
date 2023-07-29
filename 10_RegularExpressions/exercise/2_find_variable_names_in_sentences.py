import re

text = input()
pattern = r"\b_([A-Za-z0-9]+)\b"
match_variables = re.findall(pattern, text)

print(",".join(match_variables))

