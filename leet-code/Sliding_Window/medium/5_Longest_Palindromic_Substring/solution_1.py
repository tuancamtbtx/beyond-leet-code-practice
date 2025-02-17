class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if len(result) >= j - i + 1:
                    continue
                if self.isPalindrome(s[i:j+1]):
                    result = s[i:j+1]
        return result
        
    def isPalindrome(self, s):
        return s == s[::-1]

solution = Solution()
s = "babad"
out = solution.longestPalindrome(s)
print(out)