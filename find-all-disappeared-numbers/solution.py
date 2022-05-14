class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        range_list = {}
        for i in range(len(nums)):
            range_list[str(i + 1)] = 1
        for i in nums:
            try:
                range_list.pop(str(i))
            except:
                pass
        return list(range_list.keys())

'''
class Solution(object):	# Alternative solution
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])
        
        ret_list = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ret_list.append(i + 1)
        return ret_list
'''