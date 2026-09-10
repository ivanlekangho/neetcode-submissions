class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # num_dict = {}
        # for num in nums:
        #     if num not in num_dict:
        #         num_dict[num] = 0
        #     num_dict[num] += 1
        
        # for num in num_dict:
        #     if num_dict[num] > 1:
        #         return True

        # return False
        num_set = set()
        for num in nums:
            if num not in num_set:
                num_set.add(num)
            else:
                return True
        return False
        