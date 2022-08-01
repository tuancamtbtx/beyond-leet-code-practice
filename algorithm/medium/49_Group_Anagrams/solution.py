import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        key_dict = collections.defaultdict(list)
        for item in strs:
            hashed_key = hash(''.join(sorted(item)))
            key_dict[hashed_key].append(item)
        return list(key_dict.values())
def main():
    solution = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    out = solution.groupAnagrams(strs)
    print(out)
if __name__ == "__main__":
    main()