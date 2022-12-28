class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        cur_sum =  0
        prefix_sum = {0 : 1}
        for n in nums:
            cur_sum += n
            pre_sum_diff = cur_sum - k # (cur_sum  - pre_sum_diff =  k)
            result += prefix_sum.get(pre_sum_diff, 0)
            prefix_sum[cur_sum] = 1 +  prefix_sum.get(cur_sum, 0)
        return result    
        
def main():
    solution = Solution()
    nums = [1, 3,2,3,2]
    k = 4
    result = solution.subarraySum(nums, k)
    print('result',result)
    
if __name__ == "__main__":
    main()