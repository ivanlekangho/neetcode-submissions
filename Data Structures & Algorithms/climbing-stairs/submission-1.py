class Solution:
    def climbStairs(self, n: int) -> int:
        # i  = [1, 2, 3, 4, 5] -> number of total steps I've climbed
        # dp = [1, 2, ...]
        if n <= 1: return 1
        if n == 2: return 2
        dp = [None for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for total in range(3, n + 1):
            dp[total] = dp[total - 1] + dp[total - 2]
        return dp[n]