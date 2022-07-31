class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))

        return hash(s) == hash(t)
        
def main():
    solution = Solution()
    str1 = "tuancam" # sorted
    str2 = "camtuan" # sorted

    is_anagram = solution.isAnagram(str1, str2)
    print('isAnagram',is_anagram)
    str = ''.join(sorted("ba"))
    print(hash(str))
    print(hash("ab"))
if __name__ == "__main__":
    main()