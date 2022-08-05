class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        results  = []
        left = 0
        right = len(numbers) - 1
        while left < right:
            cur_sum = numbers[left] + numbers[right]
            if cur_sum > target:
                right -= 1
            if cur_sum < target:
                left += 1
            else:
                return [left, right]
        
        return results

solution = Solution()
numbers = [5,25,75]
target = 100
results = solution.twoSum(numbers, target)
print('results:', results)