class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        greatest_set = {}
        result = []
        for i,n in enumerate(arr):
            step = i + 1
            if i == len(arr) - 1:
                arr[i] = -1
                break
            print("tmp: ", arr, arr[step : len(arr) - 1])
            greatest = max(arr[step : len(arr)])
            arr[i] = greatest
        return arr
        
arr = [17,18,5,4,6,1]


solution = Solution()
result = solution.replaceElements(arr)
print(result)