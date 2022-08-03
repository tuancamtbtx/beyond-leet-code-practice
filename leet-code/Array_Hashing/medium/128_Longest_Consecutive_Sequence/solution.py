import collections

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums_set: # dam bao so do la bat dau day so tang dan step = 1
                length = 1
                while (num + length) in nums_set:
                    length += 1
                longest = max(length, longest)
        return longest
       
solution = Solution()

nums = [100,4, 300, 14, 3, 1, 2, 4]

output = solution.longestConsecutive(nums)
print("output: ", output)