class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # anagrams are words that share the same characters and the same amt
        # we can use map
        # the key can be the [0] * 26 and if the word can match this then thats the key
        # we must make the list a tuple meaning it cannot be modified so we can use as a key
        # then we can return a list of values
        
        word_list = defaultdict(list)

        for w in strs:
            key = [0] * 26
            for c in w:
                key[ord(c) - ord('a')] += 1
            word_list[tuple(key)].append(w)
        
        return list(word_list.values())