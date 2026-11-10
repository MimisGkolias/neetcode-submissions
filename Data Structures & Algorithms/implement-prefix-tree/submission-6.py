class TrieNode:
    def __init__(self):
        self.letters = {}
        self.isWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.letters:
                curr.letters[char] = TrieNode()
            curr = curr.letters[char]
        curr.isWord = True
            

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.letters[char]:
                return False
            curr = curr.letters[char]
        return curr.isWord
            

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.letters[char]:
                return False
            curr = curr.letters[char]
        return True































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
            if char not in curr.letters:
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





        