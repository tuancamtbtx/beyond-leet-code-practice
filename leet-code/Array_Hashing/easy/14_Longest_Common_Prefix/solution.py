class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result
        

def main():
    solution = Solution()
    strs = ["flower","flow","flight"] # sorted

    result = solution.longestCommonPrefix(strs)
    print('result',result)
    
if __name__ == "__main__":
    main()