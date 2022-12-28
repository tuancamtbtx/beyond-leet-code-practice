class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # tinh tan so xuat hien
        p_count = {}
        s_count = {}
        result = []
        for i in range(len(p)):
            p_count[p[i]] = 1 + p_count.get(p[i], 0)
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
        result = [0] if p_count == s_count else []
        left = 0
        for right in range(len(p), len(s)):
            s_count[s[right]] = 1 + s_count.get(s[right], 0)
            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                s_count.pop(s[left])
            left += 1
            if s_count == p_count:
                result.append(left)
        return result
        
def main():
    solution = Solution()
    s = "cbaebabacd"
    p = "abc"
    result = solution.findAnagrams(s, p)
    print('result',result)
    
if __name__ == "__main__":
    main()