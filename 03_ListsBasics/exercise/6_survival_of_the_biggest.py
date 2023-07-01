lst_of_numbers = list(map(int, input().split()))
numbers_to_remove = int(input())

for num in range(numbers_to_remove):
    smallest = min(lst_of_numbers)
    lst_of_numbers.remove(smallest)

print(", ".join(str(x) for x in lst_of_numbers))