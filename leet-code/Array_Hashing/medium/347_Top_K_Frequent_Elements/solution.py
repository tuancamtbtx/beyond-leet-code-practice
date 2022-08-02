import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        my_dict = {}
        frequent = []
        for num in nums:
            if my_dict.get(num) is None:
                my_dict[num] = 1
            else:
                my_dict[num] += 1
        frequent = sorted(list(my_dict.values()),reverse=1)
        results = []
        for num in nums:
            if my_dict[num] in frequent[0:k]:
                if(num not in results):
                    results.append(num)
        return results
def main():
    solution = Solution()
    nums = [4,1,-1,2,-1,2,3]
    k = 2
    frequent = solution.topKFrequent(nums, k)
    print('length:',frequent)
if __name__ == "__main__":
    main()