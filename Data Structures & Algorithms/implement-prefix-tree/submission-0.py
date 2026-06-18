class Node:
    #Each node contains neighbors, if its a word, 
    def __init__(self):
        self.nei = defaultdict(Node)
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = Node()
    """
    insert a string into the prefix tree
    """
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word: # we want it to add it to the root
            # if that letter is there we must follow it
            cur = cur.nei[c]
        cur.isWord = True

    """
    if word in the prefix tree:
        return True
    return False
    """
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word: # we want it to add it to the root
            # if that letter is there we must follow it
            if c not in cur.nei:
                return False
            cur = cur.nei[c]
        return cur.isWord

    """
    if prefix in the tree:
        return true
    return False
    """
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix: # we want it to add it to the root
            # if that letter is there we must follow it
            if c not in cur.nei:
                return False
            cur = cur.nei[c]
        return True
        