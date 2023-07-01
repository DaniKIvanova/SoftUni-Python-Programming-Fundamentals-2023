texts = input().split()
even_length = [x for x in texts if len(x) % 2 == 0]

for word in even_length:
    print(word)