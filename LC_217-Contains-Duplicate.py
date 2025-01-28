def has_consecutive_duplicates(nums):
    nums.sort()  # Sort the list in ascending order
    for i in range(len(nums) - 1):  # Check for consecutive duplicates
        if nums[i] == nums[i + 1]:
            return True
    return False

nums = [4, 2, 1, 3, 2]  # Example list
print("Input list:", nums)
result = has_consecutive_duplicates(nums)
print("Contains consecutive duplicates:", result)
