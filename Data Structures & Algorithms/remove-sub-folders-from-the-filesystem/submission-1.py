class TrieNode:
  
    # instructor (self, is_end_of_folder, childern_folders)
    def __init__(self, is_end_of_folder=False) -> None:
        self.is_end_of_folder = is_end_of_folder
        self.children = {}
        pass
    
    def add(self, words):
        # we are given a list of words that we must add to the Trie
        # process the words one by one
        # start at the root
        cur = self
        for word in words:
            # word is not in children -> must create it
            if word not in cur.children:
                cur.children[word] = TrieNode()
            # traverse to that child
            cur = cur.children[word]
        
        # MARK as end of folder
        cur.is_end_of_folder = True

        return None
    
    def traverse(self):

        root = self
        res = []
        # Goal is to traverse the tree and if we hit a 
        def look_for_end_of_folders(cur, word):
            if not cur:
                return 
            
            if cur.is_end_of_folder:
                res.append(word)
                return
            
            for child in cur.children:
                look_for_end_of_folders(cur.children[child], word + "/" + child)
            
            return
        look_for_end_of_folders(root, '')
        return res

class Solution:

    def removeSubfolders(self, folders: List[str]) -> List[str]:
        root = TrieNode()
        
        for folder in folders:
            clean_folder = folder.strip('/').split('/')
            root.add(clean_folder)
        
        res = root.traverse()
        return res
        # Trie problem
        # 1) need to make nodes of folder
        # 2) /a -> [a], /a/b -> [a, b] c/d -> [c, d] and /c/d/e -> [c, d, e] , /c/f -> [c, f]

