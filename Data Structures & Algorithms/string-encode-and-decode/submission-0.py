class Solution:
    def encode(self, strs: List[str]) -> str:
        # "neet" -> "4#neet"
        res = ""
        for w in strs:
            res += (str(len(w)) + '#' + w)

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        length = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1
            res.append(s[j:j+length])
            i = j + length

        return res
