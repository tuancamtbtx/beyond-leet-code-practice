class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        left , right = 0, len(height) - 1
        while left < right:
            area = max(min(height[left], height[right]) * (right - left), area)
            if height[left] < height[right]:
                left += 1
            elif height[left] >= height[right]:
                right -= 1
        return area

solution = Solution()

height = [1,8,100,2,100,4,8,3,7]

max_erea = solution.maxArea(height)
print('max_erea',max_erea)