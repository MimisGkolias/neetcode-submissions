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
        
        def dfs(j, root):
            curr = root
            
            for i in range(j, len(word)):
                char = word[i]

                if char == '.':
                    for node in curr.letters.values():
                        if dfs(i + 1, node):
                            return True
                    return False

                else:
                    if char not in curr.letters:
                        return False
                    curr = curr.letters[char]
            return curr.isWord

        return dfs(0, self.root)





