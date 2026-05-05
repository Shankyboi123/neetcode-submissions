class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_set = set()
        for inter in nums:
            new_set.add(inter)
        return len(new_set) != len(nums)