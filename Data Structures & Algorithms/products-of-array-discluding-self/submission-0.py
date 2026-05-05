import math as m


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            new_list = nums[:i] + nums[i+1:]
            dic[i] = new_list 
    
        
        final = []
        for keys, item in dic.items():
            final.append(m.prod(item))
        
        return final