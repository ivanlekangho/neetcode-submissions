class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #seen values: index of orig

        for i in range(len(nums)):
            num = nums[i]

            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i