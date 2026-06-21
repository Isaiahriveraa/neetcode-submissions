class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        Collect as much fruits as possbile

        2 basektas

        each baskets can have a single type of fruit.

        start from any tree of your choice must picm exactly one fruitt from everying tree while moving left to right meaning that 
        we can only hold 2 unique fruits at a time and then calculate the length

        1,2 ,3,2,2 

        bask_one = 1
        bask_two = 2

        """
        # hashmap to look for the fruit mapped to its index
        fruit_count = defaultdict(int) #fruit and its count

        # total
        res = 0

        # pointers
        left = 0
        right = 0

        for right in range(len(fruits)):

            cur_fruit = fruits[right] # update the fruit to last seen index
            fruit_count[cur_fruit] += 1 # fruit mapped to an index

            while len(fruit_count) > 2: # if the fruit hashmap is greather to then we have more than 2 unique fruits in the sliding window
                # remove from the left as much as possbile
                fruit_count[fruits[left]] -= 1 
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1
            res = max(right - left + 1, res)
        
        return res