### Problem 1: Two Sum

# **Description**:  
# Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

# **Example**:
# ```python
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# ```

class Solution(object):
    def twoSum(self, nums, target):
        dict_num = dict()
        for i, num  in enumerate(nums):
            if target - num in dict_num:
                return [dict_num[target - num], i]
            dict_num[num] = i
        return []


def main():
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(result)
if __name__ == "__main__":
    main()