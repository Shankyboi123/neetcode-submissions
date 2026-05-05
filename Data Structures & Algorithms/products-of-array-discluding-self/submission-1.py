class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix_array = [1] * n
        
        for i in range(1,n): 
            prefix_array[i] = prefix_array[i-1] * nums[i-1]

        
        suffix_array = [1]*n

        for i in range(n-2,-1,-1):
            suffix_array[i] = suffix_array[i+1] * nums[i+1]

        result = []
        for i in range(n):
            result.append(suffix_array[i]*prefix_array[i])
        
        return result