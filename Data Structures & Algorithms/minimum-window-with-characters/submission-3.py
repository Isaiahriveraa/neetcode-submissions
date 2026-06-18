from collections import defaultdict
from collections import Counter
class Solution:

    def minWindow(self, s: str, t: str) -> str:
        """
        So thinking out loud for this problem, I'm given S and T and I need to return the shortest string of S such that every 
        character in T, including duplicates, so is present in the string. If the substring does not exist, return an empty 
        string.

        possible DS:
        Sliding window, because substring, meaning that we need a winsow substring meaning that it has to be continuous.
        Dicitonary = (char, freq) or defaultdict && additonaly we can use constants too keep track how much matches we have that way we dont have to rescan the map
        
        Variables:
        matches, that way we can track if num of matches = len of the t_map
        t_map
        char_freq
        

        - res = [start: end, min_window] #start and the end refer to when the windopw starts and ends and we need + 1 for the end because py 
            is exclusive for the indexes

        Edge cases:

        - if the char we just removed affects how much characters we needed to match the freq of t we remove a match
        - if we added a character that is needed to match the amt of chracters needed for the chracter that is t we add a match

        IN SUMMARY:
        = That means that we have to keep track when we remove or add characters to the Dicitonary, KEEP TRACK OF MATCHES 

        if we no such substring exists return ""

        Input: s = "OUZODYXAZV", t = "XYZ"

        We want the smallest substring that contains t in the window, so that means that we have to remove from the left most character
        ONCE we finally get the t in the window
        -> shrink the left side of the window as much as we can if we have all the characters in t and the freq of them
        ->

        Output: "YXAZ"

        
        ABC needed
        ADOBEC len(6)
        DOBECODEBA len(10)
        ----CODEBA
        -----ODEBANC
        --------BANC

        """

        t_map = Counter(t) # map of char's count 
        char_freq = defaultdict(int) # char -> count 
        matches = 0
        res = [0, 0, float('inf')] # start of the window, end of the window, and if its still max then no such substring exists containing T
        max_freq = 0
        l = 0

        for r in range(len(s)):
            char = s[r] # cur char
            char_freq[char] += 1
            if char in t_map and char_freq[char] == t_map[char]: # we are matching the amt of char's we need for that char in t
                matches += 1
            print("window",s[l: r + 1])
            #max_freq = max(max_freq, char_freq[char])
            # if we got the matches that we needed then we have to shrink the window as much as we can we awnat the min window
            while (matches == len(t_map)): # if something the window and l and r
                #if the char we are going remove is the character we needed to maintain the matches
                if (r - l + 1 < res[2]):
                    res = [l, r, r - l + 1]

                char_freq[s[l]] -= 1
                if (s[l] in t_map and t_map[s[l]] == char_freq[s[l]] + 1): # if we are one below than needed rmeove the matches
                    matches -= 1
                l += 1 # we can move the left ptr bc we removed the char from the window
                print(s[l: r + 1])
        
        return "" if res[2] == float('inf') else s[res[0]: res[1] + 1] # if no substring exists