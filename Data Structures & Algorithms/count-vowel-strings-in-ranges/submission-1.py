class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        res = [0] * len(queries)
        j = 0
        for start, end in queries:
            vowels_count = 0
            for i in range(start, end + 1):
                word = words[i]
                if word[0] in vowels and word[len(word) - 1] in vowels:
                    vowels_count += 1

            res[j] = vowels_count
            j += 1

        return res
