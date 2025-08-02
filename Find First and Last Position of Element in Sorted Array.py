class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = -1, -1

        for i in range(len(nums)):
            if nums[i] == target:
                if start == -1:
                    start = i  
                end = i     

        return [start, end]
