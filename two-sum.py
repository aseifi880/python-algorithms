"""
given an array of integers and an integer target return the indices of two numbers that add up to the target
"""



## this is a brute force method
## not recommended 
def findPair(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]




# TEST 1
nums = [-2, -4, -6, -8, 5]
target = 3
res = findPair(nums, target)
print(res)