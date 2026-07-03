class TrieNode:
    def __init__(self, is_end=False):
        self.children = defaultdict(TrieNode)
        self.is_end = is_end

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add(self, folder) -> None:
        cur = self.root

        parts = folder.strip("/").split("/")
        
        for part in parts:
            cur = cur.children[part]
        cur.is_end = True
        
    def search_par_folder(self) -> List[str]:
        res = []
        
        def dfs(cur, path):
            # if the node is None
            if cur.is_end:
                res.append(path) 
                return

            if not cur:
                return

            # if we are at an end of a par, add it to the res
            
            for child in cur.children:
                dfs(cur.children[child], path + "/" + child)

            return
        
        dfs(self.root, "")
        return res

class Solution:

    def removeSubfolders(self, folders: List[str]) -> List[str]:
        
        root = Trie()

        for fold in folders:
            root.add(fold)
        
        return root.search_par_folder()

