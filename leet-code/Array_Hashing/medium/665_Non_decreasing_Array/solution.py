class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count_replace =  0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                count_replace += 1
                # dich chuyen so 
                if i > 0 and nums[i + 1] < nums[i-1]:
                     nums[i+1] = nums[i]
                else:
                    nums[i] = nums[i+1]
                 
        return count_replace <= 1
    
def main():
    solution = Solution()
    nums = [3,4,2,3]
    
    result = solution.checkPossibility(nums)
    print('result',result)
    
if __name__ == "__main__":
    main()