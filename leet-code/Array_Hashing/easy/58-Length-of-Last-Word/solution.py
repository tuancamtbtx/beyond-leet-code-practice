class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        length =  0
        flag_char = False
        while i >= 0 :
            if flag_char == True and s[i] == " ":
                break;
            if(s[i] != " "):
                length += 1
                flag_char = True
            i -= 1
        return length
        
solution = Solution()

s = "   fly me   to   the moon  "
result = solution.lengthOfLastWord(s)
print(result)