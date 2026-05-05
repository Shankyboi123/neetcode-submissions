class Solution:

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = ""
        for char in s:
            if char.isalnum():
                new_s += char
            
        newer_s = new_s.lower()

        if newer_s == " " or newer_s == "":
            return True 

        l, r = 0, len(newer_s)-1

        while l < r: 
            if newer_s[l] != newer_s[r]:
                return False 
            else: 
                l +=1 
                r -= 1
        
        return True 
        