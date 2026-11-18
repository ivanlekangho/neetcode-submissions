class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max = [0] * len(height)
        prefix_max[0] = height[0]
        suffix_max = [0] * len(height)
        suffix_max[len(height) - 1] = height[len(height) - 1]
        for i in range(1, len(height)-1):
            prefix_max[i] = max(height[i], prefix_max[i - 1])
        for i in range(len(height) - 2, -1, -1):
            suffix_max[i] = max(height[i], suffix_max[i + 1])
        
        volume = 0
        for i in range(1, len(height) - 1):
            volume += max(0, min(prefix_max[i - 1], suffix_max[i + 1]) - height[i])
        
        return volume
            
