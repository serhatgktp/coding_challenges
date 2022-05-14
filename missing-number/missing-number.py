class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        min = nums[0]
        max = nums[0]
        total = 0
        count = 0
        contains_zero = 0
        contains_one = 0
        
        for num in nums:
            if num == 0:
                contains_zero = 1
            if num == 1:
                contains_one = 1
            if num < min:
                min = num
            elif num > max:
                max = num
            total += num
            count += 1
            
        if contains_zero == 0:
            return 0
        elif contains_one == 0:
            return 1
        
        if 2*total == (count*(min + max)):
            return max + 1
        
        return (count + 1)*(min + max)/2 - total