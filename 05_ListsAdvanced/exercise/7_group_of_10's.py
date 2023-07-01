number_of_sequence = list(map(int, input().split(", ")))
counter = 0
tens = []

num_for_loop = (max(number_of_sequence) // 10) + 1
if max(number_of_sequence) % 10 == 0:
    num_for_loop -= 1

for index in range(num_for_loop):
    counter += 10
    print(f"Group of {counter}'s:", [x for x in number_of_sequence if x <= counter])
    number_of_sequence = [x for x in number_of_sequence if x > counter]