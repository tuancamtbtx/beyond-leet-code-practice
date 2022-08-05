class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1 
        print('size', len(s))
        while left < right:
            if not self.alphanum(s[left]):
                left += 1
            if not self.alphanum(s[right]):
                right -= 1
            if (s[left].lower() != s[right].lower()):
                return False
            right -= 1
            left += 1
        return True
    
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )
solution = Solution()

s = "A man a plan a canal PanAma"
print(s[24])
c = solution.isPalindrome(s)
print(c)