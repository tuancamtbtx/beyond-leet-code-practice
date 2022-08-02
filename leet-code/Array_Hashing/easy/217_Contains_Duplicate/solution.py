class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_set = set()
        for i in nums:
            if i in num_set:
                return True
            num_set.add(i)
        return False

def main():
    solution = Solution()
    nums1 = [1, 2, 3 , 4, 5,1] # sorted

    is_dup = solution.containsDuplicate(nums1)
    print('is_dup',is_dup)
if __name__ == "__main__":
    main()