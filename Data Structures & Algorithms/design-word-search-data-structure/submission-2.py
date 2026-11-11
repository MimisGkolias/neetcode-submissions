class TrieNode:
    def __init__(self):
        self.letters = {}
        self.isWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.letters:
                curr.letters[char] = TrieNode()
            curr = curr.letters[char]
        curr.isWord = True

    def search(self, word: str) -> bool:
        
        def dfs(node, index):
            curr = node
            for i in range(index, len(word)):
                if word[i] == ".":
                    for child in curr.letters.values():
                        if dfs(child, i + 1):
                            return True
                    return False

                else:
                    if word[i] not in curr.letters:
                        return False
                    curr = curr.letters[word[i]]
            return curr.isWord
        return dfs(self.root, 0)

