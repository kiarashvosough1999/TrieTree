from TrieNode import TrieNode
import re


class Trie:

    def __init__(self):
        self.root = self.getNode()
        self.end_index = 0
        self.f = open("Result.txt", "w+")

    def __del__(self):
        self.f.close()

    def getNode(self):
        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self, ch):
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
        return ord(ch) - ord('a')

    def import_from_file(self):
        pass

    def from_input(self):
        _input = input('enter your text:\n')
        self.f.write('inputed text:\n' + _input + '\n')
        _input_tokenized = re.sub(r'[^a-zA-Z]', r' ', _input.lower()).split()
        for key in _input_tokenized:
            self.insert(key)

    def search_from_input(self):
        _input = input('enter your search text:\n')
        self.search(_input.lower())

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)

        for level in range(length):
            index = self._charToIndex(key[level])
            # print(key[level]," ", level)

            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl.children[index].start_indexes.append(self.end_index + level + 1)
            if level == length - 1:
                pCrawl.children[index].start_indexes_continue.append(False)
            else:
                pCrawl.children[index].start_indexes_continue.append(True)

            pCrawl = pCrawl.children[index]

        # mark last node as leaf
        self.end_index += length
        pCrawl.isEndOfWord = True

    def search(self, key):

        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        count = 0
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            # print("cal ", pCrawl.start_indexes)
            pCrawl = pCrawl.children[index]
            count += 1
        #
        if pCrawl is not None and pCrawl.isEndOfWord:
            list_of_ints = self.find(count, pCrawl.start_indexes, pCrawl.start_indexes_continue)
            self.f.write(key + ':\t' + ', '.join(str(x) for x in list_of_ints) + '\n')
            print(key, ' : ', ', '.join(str(x) for x in list_of_ints))
        # print("end ", pCrawl.start_indexes)
        # print("count is", count)
        # print("bool is", pCrawl.start_indexes_continue)

    def find(self, count, second_array, bool_array):
        first_array = []
        length = len(second_array)
        for i in range(length):
            if not bool_array[i]:
                first_array.append(second_array[i] - count + 1)
        return first_array
