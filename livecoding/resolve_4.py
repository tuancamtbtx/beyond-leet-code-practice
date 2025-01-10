# ### Problem 4: Longest Substring Without Repeating Characters

# Given a string `s`, find the length of the longest substring without repeating characters.

# **Example**:
# ```python
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# ```

# **Solution**:

class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		set_char = set()
		result = 0
		j = 0
		for i in range (len(s)):
			while s[i] in set_char:
				set_char.remove(s[j])
				j += 1
			set_char.add(s[i])
			result = max(result, i - j + 1)
		return result

def main():
	solution = Solution()
	s = "abcdacdefa"
	result = solution.lengthOfLongestSubstring(s)
	print("s",result)
if __name__ == "__main__":
	main()