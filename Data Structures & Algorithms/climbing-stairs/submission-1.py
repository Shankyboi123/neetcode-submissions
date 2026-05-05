class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n


        combinations = [0]*(n+1)
        combinations[1] = 1
        combinations[2] = 2 

        for i in range(3,n+1):
            combinations[i] = combinations[i-1] + combinations[i-2]

        return combinations[n] 


        