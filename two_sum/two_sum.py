class Solution(object):
    def twoSum(self, nums, target):
        
        past_vals = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in past_vals:
                return [past_vals[diff], i]
            past_vals[nums[i]] = i