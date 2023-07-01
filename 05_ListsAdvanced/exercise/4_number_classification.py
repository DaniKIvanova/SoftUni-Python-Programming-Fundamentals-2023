def filtering_numbers(nums):
    positive_filter = ", ".join(f"{x}" for x in nums if x >= 0)
    negative_filter = ", ".join(f"{x}" for x in nums if x < 0)
    even_filter = ", ".join(f"{x}" for x in nums if x % 2 == 0)
    odd_filter = ", ".join(f"{x}" for x in nums if x % 2 != 0)

    print(f"""Positive: {positive_filter}
Negative: {negative_filter}
Even: {even_filter}
Odd: {odd_filter}""")


numbers_for_filter = list(map(int, input().split(", ")))
filtering_numbers(numbers_for_filter)