def second_largest(nums):
    unique_nums = list(set(nums))
    unique_nums.sort()
    return unique_nums[-2] if len(unique_nums) > 1 else "No second largest number"

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Second largest number:", second_largest(numbers))
