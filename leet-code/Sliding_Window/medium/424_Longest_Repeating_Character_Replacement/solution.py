from collections import Counter
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        right = 0
        max_count = 0
        max_length = 0
        count = Counter()
        for right in range(1, len(s)):
            count[s[right - 1]] += 1
            max_count = max(max_count, count[s[right - 1]])
            if right - left - max_count > k:
                count[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left)
        print('count:', count)
        return max_length
solution = Solution()

s = "AABAABBA"
k = 1
longest = solution.characterReplacement(s,k)
print('longest:', longest)