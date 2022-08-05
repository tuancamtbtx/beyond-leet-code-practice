class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums_set = set(nums)
        nums = sorted(nums)
        
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                
                t_sum = nums[i] + nums[left] + nums[right]
                if t_sum > 0:
                    right -= 1
                elif t_sum < 0:
                    left += 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    # duyet so khong trung
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return results
