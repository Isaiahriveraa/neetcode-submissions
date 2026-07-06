class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(str(len(word)) + '#' + word)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:

        res = []

        i = 0

        while i < len(s):
            # need to get the len of the str
            j = i
            while s[j] != '#':
                j += 1
            
            length_of_word = int(s[i: j])

            # at the start of the word
            j += 1

            res.append(s[j:j + length_of_word])

            i = j + length_of_word # start of the next number index
    
        return res
        
            