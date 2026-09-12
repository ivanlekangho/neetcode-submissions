class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        robbed = [0 for _ in range(n + 1)]
        skipped = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            robbed[i] = skipped[i-1] + nums[i-1]
            skipped[i] = max(robbed[i-1], skipped[i-1])

        return max(robbed[n], skipped[n])