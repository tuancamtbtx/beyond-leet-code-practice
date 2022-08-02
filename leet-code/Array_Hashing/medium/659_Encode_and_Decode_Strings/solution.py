class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        result = ""
        for str in strs:
            result += str + "$"
        return result
        # write your code here

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        results = []
        i = 0
        tmp = ""
        while i < len(str):
            if str[i] != '$':
                tmp += str[i]
            elif str[i] == '$':
                results.append(tmp)
                tmp = "" # reset
            i  += 1
        return results
def main():
    solution = Solution() # O(n)
    nums = ["lint","code","love","you"]
    encode = solution.encode(nums)
    print("endode: ", encode)
    decode = solution.decode(encode)
    print("decode: ", decode)
if __name__ == "__main__":
    main()