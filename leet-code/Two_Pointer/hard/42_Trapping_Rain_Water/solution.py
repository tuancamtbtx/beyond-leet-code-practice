class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            res = min(height[left], height[right]) * (right - left)
            left += 1
            right -=1

solution = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
solution.trap(height)
print(height)