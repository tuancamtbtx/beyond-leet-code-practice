from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len_s1 = len(s1)
        len_s2 = len(s2)
        s1_count = Counter(s1)
        print(s1_count)
        print(len_s1)
        window_count = Counter(s2[:len_s1])
        print(window_count)
        for i in range(len_s1, len_s2):
            print(i)
            window_count[s2[i]] += 1
            window_count[s2[i - len_s1]] -= 1
            print(window_count)
            # Remove the count of the character if it becomes zero
            if window_count[s2[i - len_s1]] == 0:
                del window_count[s2[i - len_s1]]
            if s1_count == window_count:
                return True
        return False
   
        
solution = Solution()
s1 = "aba"
s2 = "aabac"
result = solution.checkInclusion(s1,s2)
print(result)