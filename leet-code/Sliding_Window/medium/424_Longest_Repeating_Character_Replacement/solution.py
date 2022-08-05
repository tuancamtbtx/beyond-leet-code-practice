class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        res = 0
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1

        print(count)
solution = Solution()

s = "abcabcbb"
k = 2
'''
 abaadabad
'''
longest = solution.characterReplacement(s,k)
print('longest', longest)