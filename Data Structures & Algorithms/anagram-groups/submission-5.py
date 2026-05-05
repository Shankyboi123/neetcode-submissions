class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        final = []
        for x, item in enumerate(strs): 
            y = str(sorted(item))

            if y not in dic: 
                dic[y] = [item]
            else: 
                dic[y].append(item)

        for key, value in dic.items(): 
            final.append(value)
        
        return final