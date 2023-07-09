text = input()
clear_text = ""

for el in range(len(text) - 1):
    if text[el] == text[el + 1]:
        continue
    else:
        clear_text += text[el]
clear_text += text[-1]
print(clear_text)

