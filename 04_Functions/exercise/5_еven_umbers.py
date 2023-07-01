def str_to_int(nums: list):
    for index in range(len(nums)):
        nums[index] = int(nums[index])
    return nums


def even_nums(nums):
    if nums % 2 == 0:
        return True


sequence_of_numbers = input().split()
sequence_of_numbers = str_to_int(sequence_of_numbers)
print(list(filter(even_nums, sequence_of_numbers)))