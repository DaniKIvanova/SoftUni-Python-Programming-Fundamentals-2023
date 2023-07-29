import re

text = input()

while text:
    pattern = r"((w{3})\.([A-Za-z0-9]+)([A-Za-z0-9\-]+)*(\.[a-z]+)+)"
    match_links = re.search(pattern, text)
    if match_links:
        print(match_links.group())
    text = input()

    