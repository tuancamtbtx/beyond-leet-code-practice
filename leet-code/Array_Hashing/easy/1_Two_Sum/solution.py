class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pre_map = {} # value: index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in pre_map:
                return [pre_map[diff], i]
            pre_map[n] = i

def main():
    solution = Solution()
    nums = [1, 2, 6, 7] # sorted
    target = 8 # sorted

    result = solution.twoSum(nums, target)
    print('result', result)
if __name__ == "__main__":
    main()