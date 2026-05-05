class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_str = {}
        for letter in s: 
            if letter not in s_str: 
                s_str[letter] = 1 
            else: 
                s_str[letter] += 1
        
        t_str = {}
        for letter in t: 
            if letter not in t_str: 
                t_str[letter] = 1 
            else: 
                t_str[letter] += 1
        
        return t_str == s_str



        