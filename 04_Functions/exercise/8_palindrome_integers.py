def palindrome(nums: list):
    for num in nums:
        if num == num[::-1]:
            print(True)
        else:
            print(False)


sequence_of_numbers = input().split(", ")
palindrome(sequence_of_numbers)