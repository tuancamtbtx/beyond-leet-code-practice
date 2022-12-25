class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        while i <= r:
            if nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            elif nums[i] == 0:
                swap(l, i) 
                l += 1
            i += 1
        return nums      
            


def main():
    solution = Solution()
    nums = [2,0,2,1,1,0]

    result = solution.sortColors(nums)
    print('result',result)
    
if __name__ == "__main__":
    main()