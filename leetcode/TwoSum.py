def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j



"""
Step-by-step Explanation:
Outer loop (for i in range(len(nums))):

This goes through each element of the list one by one. i is the index of the first number.

Inner loop (for j in range(i+1, len(nums))):

For each element nums[i], this loop goes through all the following elements nums[j] (where j > i). This ensures you don’t check the same pair twice or pair an element with itself.

Condition (if nums[i] + nums[j] == target):

It checks if the sum of the two numbers at index i and j equals the target.

Return (return i, j):

If such a pair is found, it returns their indices as a tuple.

"""
