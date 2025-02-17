class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert a word into the trie."""
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, word):
        """Search for a word in the trie."""
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word

    def starts_with(self, prefix):
        """Check if there is any word in the trie that starts with the given prefix."""
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True

# Example usage:
trie = Trie()
trie.insert("hello")
trie.insert("helium")

print("Search 'hello':", trie.search("hello"))    # Output: True
print("Search 'helix':", trie.search("helix"))    # Output: False
print("Starts with 'he':", trie.starts_with("he"))  # Output: True
print("Starts with 'hi':", trie.starts_with("hi"))  # Output: False