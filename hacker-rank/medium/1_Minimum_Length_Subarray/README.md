For an array of n positive integers arr[n] and an integer k, a subarray is considered good if it consists of at least k distinct integers.

Find the minimum length subarray that is good. If there is no such subarray, return -1.


arr = [1,2,3,4,3,4,2,1] 
k = 3

1. use binary search find sub array distinct k
2. use set to check sub array is array with k distinct
