class Solution(object):
    def findLIS(self, s):
        longest = 1
        LIS = []
        for i in range(len(s) - 1):
            val = s[i]
            if s[i + 1] > val:
                LIS.append(s[i+1])
                longest += 1
        print(LIS)
        print(longest)

s = [1,4,5,2,6]
solution = Solution()
solution.findLIS(s)