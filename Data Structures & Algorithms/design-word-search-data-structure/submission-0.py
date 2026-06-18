class Node:
    def __init__(self):
        self.nei = defaultdict(Node)
        self.isWord = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.nei[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        
        def dfs(i, cur) -> bool:
            if i == len(word): # if we reached the last character return true
                return cur.isWord
            # bounds check
            if i >= len(word) and word[i] != '.':
                return False
            if word[i] == '.': # we have to search all paths
                for nei in cur.nei:
                    if dfs(i + 1, cur.nei[nei]):
                        return True
            if word[i] in cur.nei:
                return dfs(i + 1, cur.nei[word[i]])
            return False
        return dfs(0, self.root)
        
"""
We need a data strucutre that I need to add words to the data structure
that makes me think of a prefix tree.

Process the word by each character at a time and traverse the trie to find
the word but there is a a brute force wildcard trigger where if we get a .
that means that we want to consider each branch in the trie from that letter and return true
if any string is that word 
"""