class TrieNode:
    def __init__(self):
        self.letters = {}
        self.isWordInserted = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if curr.letters.get(char, 0) == 0:
                curr.letters[char] = TrieNode()
            curr = curr.letters[char]
        curr.isWordInserted = True


    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.letters:
                return False
            curr = curr.letters[char]
        return curr.isWordInserted
            

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.letters:
                return False
            curr = curr.letters[char]
        return True





        