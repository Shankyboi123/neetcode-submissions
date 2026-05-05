class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        sets = list(set(nums))
        final = []

        for item in sets:
            x = nums.count(item)
            dic[item] = x 
        
        while k != 0: 
            max_value = max(dic.values())
            key = None 

            for key in dic.keys():
                if dic[key] == max_value:
                    final.append(key)
                    del dic[key]
                    break
            
            k -= 1 

        return final
        