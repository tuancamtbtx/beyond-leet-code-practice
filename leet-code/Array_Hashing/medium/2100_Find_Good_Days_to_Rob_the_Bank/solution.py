class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """
        # goodDays = []
        # for i in range(len(security) - time + 1):
        #     if max(security[i:i + time]) == security[i]:
        #         goodDays.append(i)
        # return goodDays

sl = Solution()
print(sl.goodDaysToRobBank([1, 2, 3, 4, 5], 3))
