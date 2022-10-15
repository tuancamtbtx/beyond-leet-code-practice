A subsequence is created by deleting zero or more elements from a sequence while maintaining order.

A sequence is strictly increasing if every element in the sequence is greater than the previous element. For example, [1, 2, 3] is strictly increasing while [1, 2, 2] is not.

 

Given an array of integers, determine the length of the longest strictly increasing subsequence.

 

For example, s = [1, 2, 2, 3, 1, 6]. Two strictly increasing subsequences are (1,2), (1, 2, 3). The longest increasing subsequence has a length of 4: LIS = [1,2,3,6].

Function Description 

 

Complete the function findLIS in the editor below.

 

findLIS has the following parameter(s):

    int s[n]:  an array of integers

 

Returns:

    int: the length of the longest strictly increasing subsequence in the array

 