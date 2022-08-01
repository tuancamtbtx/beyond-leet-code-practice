class Solution(object):
    def isSubarrayKDistinct(self, arr, k, mid):
        cnt = {}
        val = 0
        for i, cur in enumerate(arr):
            print(cnt)
            cnt[cur] = cnt.get(cur, 0) + 1
            if cnt[cur] == 1:
                val += 1
            # check when size check array == array child
            if (i >= mid - 1):
                if val >= k:
                    return True
                cnt[arr[i - mid + 1]] -= 1
                if cnt[arr[i - mid + 1]] == 0:
                    val -= 1
        return False

    def findMinimumLengthSubarray(self, arr, k):
        n = len(arr)
        left, right , result , mid = 1, n, n + 1, 0
        # use binary search
        while left <= right:
            mid = left +  (right - left) // 2 
            print(mid)
            if(self.isSubarrayKDistinct(arr, k, mid)):
                result = mid
                right = mid - 1
            else: 
                left = mid + 1
        if result == n + 1:
            return -1 
        return result

def main():
    solution = Solution()

    nums1 = [2, 2, 5, 4, 1, 3] # input array
    k = 5 # num distict in array
    lenght = solution.findMinimumLengthSubarray(nums1, k)
    print('lenght: ',lenght)
if __name__ == "__main__":
    main()

