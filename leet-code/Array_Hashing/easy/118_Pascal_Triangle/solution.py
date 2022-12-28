class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        pre_arr = []
        for i in range(1, numRows + 1 ):
            cur_arr = []
            for j in range(i):
                if len(pre_arr) > 0 and j > 0:
                    val =  sum(pre_arr[j-1:j+1])
                    cur_arr.append(val)
                else:
                    cur_arr.append(1)
            result.append(cur_arr)
            pre_arr = cur_arr
        return result

def main():
    solution = Solution()
    numRows = 5
    result = solution.generate(numRows)
    print('result',result)
    
if __name__ == "__main__":
    main()