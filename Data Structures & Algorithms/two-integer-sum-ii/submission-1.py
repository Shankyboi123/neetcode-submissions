class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1

        for i in range(len(numbers)): 
            l = 0 
            while l < r: 
                req = target - numbers[r]
                if numbers[l] == req: 
                    return [l+1,r+1]
                else: 
                    l += 1
            
            r -= 1