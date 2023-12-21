class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        

solution = Solution()
nums = [1,8,100,2,100,4,8,3,7]

four_sum = solution.fourSum(nums=nums, target=10)
print('four_sum',four_sum)