class Solution:
    def rob(self, nums: List[int]) -> int:
        # max(best plan avoiding house 0, best plan avoiding the last house)
        n = len(nums)
        if n == 1:
            return nums[0]

        robbed = [0 for _ in range(n)]
        skipped = [0 for _ in range(n)]

        for i in range(1, n):
            robbed[i] = skipped[i-1] + nums[i]
            skipped[i] = max(robbed[i-1], skipped[i-1])

        best_avoiding_first = max(robbed[n-1], skipped[n-1])

        robbed = [0 for _ in range(n)]
        skipped = [0 for _ in range(n)]

        for i in range(0, n-1):
            robbed[i] = (skipped[i-1] if i > 0 else 0) + nums[i]
            skipped[i] = max(robbed[i-1] if i > 0 else 0, skipped[i-1] if i > 0 else 0)

        best_avoiding_last = max(robbed[n-2], skipped[n-2])
        
        return max(best_avoiding_first, best_avoiding_last)