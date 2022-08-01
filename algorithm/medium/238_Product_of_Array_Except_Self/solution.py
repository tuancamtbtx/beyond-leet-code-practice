class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        result = []
        prefix = 1
        postfix = 1
        prefix_list = []
        postfix_list = []
        for i in range(len(nums)):
            prefix_list.append(prefix)
            prefix *= nums[i] 
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            result.insert(0,prefix_list[i] * postfix)
            postfix *= nums[i]
        return result
def main():
    solution = Solution() # O(n)
    nums = [-1,1,0,-3,3]
    out = solution.productExceptSelf(nums)
    print("out", out)
if __name__ == "__main__":
    main()