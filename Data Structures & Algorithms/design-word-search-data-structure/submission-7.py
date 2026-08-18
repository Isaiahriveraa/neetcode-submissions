from collections import defaultdict
class TrieNode:

    def __init__(self, is_end=False) -> None:

        self.children = defaultdict(TrieNode)
        self.is_end = is_end

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        
        root = self.root

        for c in word:
            root = root.children[c]
        root.is_end = True

    def search(self, word: str) -> bool:

        def dfs(root, i):
            if root.is_end and i == len(word):
                return True

            if i >= len(word):
                return False
            
            if word[i] not in root.children and word[i] != '.':
                return False
            
            if word[i] == '.':
                for child in root.children:
                    if not root.children:
                        return False

                    if dfs(root.children[child], i + 1):
                        return True
            
            
            return dfs(root.children[word[i]], i + 1)
        
        return dfs(self.root, 0)


