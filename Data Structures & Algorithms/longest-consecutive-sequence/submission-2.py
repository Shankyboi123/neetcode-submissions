class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0

        start = []
        noms = set(nums)
        for num in nums: 
            if num - 1 in noms: 
                continue 
            else: 
                start.append(num)
        
        longest_streak = 0

        for num in start:
            curren_num = num
            x = 1

            while (curren_num + 1) in noms: 
                x += 1
                curren_num += 1
            
            longest_streak = max(longest_streak, x)
        
        return longest_streak
        