class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current_node = self.root
        for char in word:
            # check char is exist in chirldren of root
            if char not in current_node.children:
                # if not exist then create a new node and assign to the char
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# Example usage:
trie = Trie()
trie.insert("hello")
trie.insert("helium")
print("Search 'hello':", trie.search("hello"))    # Output: True
print("Search 'helix':", trie.search("helix"))    # Output: False
print("Starts with 'he':", trie.startsWith("he"))  # Output: True
print("Starts with 'hi':", trie.startsWith("hi"))  # Output: False