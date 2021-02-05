class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None] * 26
        self.start_indexes = []
        self.start_indexes_continue = []
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False
