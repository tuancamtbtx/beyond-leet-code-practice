class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        for i,n in enumerate(arr):
            step = i + 1
            if i == len(arr) - 1:
                arr[i] = -1
                break
            greatest = max(arr[step : len(arr)])
            arr[i] = greatest
        return arr
        
arr = [17,18,5,4,6,1]


solution = Solution()
result = solution.replaceElements(arr)
print(result)