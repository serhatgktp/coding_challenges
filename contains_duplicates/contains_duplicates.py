class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        past_nums = []
        
        for num in nums:
            if num in past_nums:
                return True
            past_nums.append(num)
        return False