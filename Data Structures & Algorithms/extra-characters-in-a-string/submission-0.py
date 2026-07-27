class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False

    def add(self, words):

        for word in words:
            cur = self # must start at the root for each word
            for ch in word:
                cur = cur.children[ch]
            cur.is_end = True # we are the last char for this word

    def traverse(self, s):
        
        # Goal is to collect as much unique char's
        # if we do not include a char then 
        memo = {}

        def dfs(i):

            if i == len(s):
                return 0
            
            if i in memo:
                return memo[i]

            res = 1 + dfs(i + 1)
            cur = self

            for j in range(i, len(s)):
                
                ch = s[j]

                if ch not in cur.children:
                    break

                cur = cur.children[ch]

                # if we found a complete word
                if cur.is_end:
                    res = min(res, dfs(j + 1))

            memo[i] = res
            return res
        return dfs(0)

class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        """
        given s string s and a dict 

        break s into one or more nonoverlapping strings

        such that each substring is present in dictionary

        so we have to opitmially split the words

        1) build a word
        2) if the word is in the dictionary add to the res
        3) maybe we can split the word?
        # prefix meaning we can create a trie
        """
        root = TrieNode()
        root.add(dictionary)
        return root.traverse(s)



