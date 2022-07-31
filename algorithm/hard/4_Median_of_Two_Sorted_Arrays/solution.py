# use Binary Search
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        total =  len(A) +  len(B)
        haft = total // 2
        if len(B) < len(A):
            A, B = B, A
        left, right = 0, len(A) - 1
        while True:
            i = (left + right) // 2 # A
            j = haft - i - 2 # B
            A_left =  A[i] if i >= 0 else float("-infinity")
            B_left = B[j] if j >= 0 else float("-infinity")
            A_right = A[i + 1] if i + 1 < len(A) else float("infinity")
            B_right = B[j + 1] if j + 1 < len(B) else float("infinity")
            print(A_left, A_right)
            if A_left <= B_right and B_left <= A_right:
                if total % 2:
                    return min(A_right, B_right)
                return (max(A_left + B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                right = i - 1
            else:
                left = i + 1




        
def main():
    solution = Solution()
    nums1 = [1, 2] # sorted
    nums2 = [3, 4, 6] # sorted

    median = solution.findMedianSortedArrays(nums1, nums2)
    print('median',median)
if __name__ == "__main__":
    main()