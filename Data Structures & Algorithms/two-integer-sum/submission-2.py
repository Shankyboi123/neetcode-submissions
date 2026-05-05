class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for integer in range(len(nums)):
            req = target - nums[integer]
            for j in range(integer+1,len(nums),1):
                if nums[j] == req:
                    return [integer, j]
