from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """
        @given 
        - List[str]
        
        @definitions
        - anagram = a string that contains the exact same char's as another string (order can be different for the string in terms of the char's)

        @goal 
        - group all anagrams tg in sublists

        @algo
        - use a array to represent char freq [0] * 26
        - iterate over a word 
        - add its char to the list that corresponds to the index of the char in the list -> list[char_index] += 1
        - make the list a tuple and attach it to a hashmap[key=(tuple(char_freq))] -> List[str]

        return the values of the hashmap

        @return 
        - grouped sublists in any order

        @time 
        - O()
        """
        char_freq_to_word = defaultdict(list) 
        
        for word in strs: # O (N) N = len(strs)
            
            cur_list = [0] * 26 
            for character in word: # O (L) -> L = length of the longest word in strs
                char_val = ord(character) - ord('a')
                cur_list[char_val] += 1
            
            # add the cur_list to the char_freq_to_word if not present as a key
            # append the word
            # grouping the words with the same freq for the chars present in a word
            char_freq_to_word[tuple(cur_list)].append(word)
        
        return list(char_freq_to_word.values())

    
        # Time complexity: O(N * L)
        # Space: O(N) N = len(strs) -> length of words in strs
        # O(N * L) if the output groups are counted.

    