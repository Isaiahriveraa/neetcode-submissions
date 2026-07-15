class Solution:
    def simplifyPath(self, path: str) -> str:
        
        # strip and split 
        new_path = path.strip('/').split('/')
        print(new_path)
        stack = []
        for word in new_path:
            if not word or word == '.': # empty string
                continue
            if stack and word == '..':
                stack.pop()
            elif word != '..':
                stack.append(word)
        
        return '/' + "/".join(stack)
            
            