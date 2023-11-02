class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * (len(nums) * 2)
        for i in range(0,len(nums)):
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]
        return ans
solution = Solution()
nums = [1,2,1]
result = solution.getConcatenation(nums)
print(result)