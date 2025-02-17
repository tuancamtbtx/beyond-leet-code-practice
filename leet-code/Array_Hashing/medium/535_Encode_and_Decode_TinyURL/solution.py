import random
import string

class Solution:
    def __init__(self):
        self.url_to_code = {}  # Maps long URLs to short codes
        self.code_to_url = {}  # Maps short codes to long URLs
        self.base_url = "http://tinyurl.com/"
        self.code_length = 6  # Length of the short code

    def _generate_code(self):
        """Generates a random short code."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=self.code_length))

    def encode(self, longUrl):
        """
        Encodes a long URL to a short URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.url_to_code:
            # If the URL is already encoded, return the existing short URL
            code = self.url_to_code[longUrl]
        else:
            # Generate a new code and ensure it's unique
            code = self._generate_code()
            while code in self.code_to_url:
                code = self._generate_code()
            
            # Store the mapping
            self.url_to_code[longUrl] = code
            self.code_to_url[code] = longUrl
        
        return self.base_url + code

    def decode(self, shortUrl):
        """
        Decodes a short URL to the original long URL.
        
        :type shortUrl: str
        :rtype: str
        """
        # Extract the code from the short URL
        code = shortUrl[len(self.base_url):]
        return self.code_to_url.get(code, "")

# Example usage
solution = Solution()
url = "https://leetcode.com/problems/design-tinyurl"
tiny = solution.encode(url)
print("Encoded:", tiny)  # Returns the encoded tiny URL
original = solution.decode(tiny)
print("Decoded:", original)  # Returns the original URL