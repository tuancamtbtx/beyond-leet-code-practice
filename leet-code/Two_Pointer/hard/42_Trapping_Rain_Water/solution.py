class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        res = 0
        val_left = height[left]
        val_right = height[right]
        while left < right:
            if val_left < val_right:
                left += 1
                val_left = max(val_left, height[left])
                res += val_left - height[left]
            else:
                right -=1
                val_right = max(val_right, height[right])
                res += val_right - height[right]
        return res
            

solution = Solution()
height = [4,2,0,3,2,5]#[0,1,0,2,1,0,1,3,2,1,2,1]
res = solution.trap(height)
print(res)