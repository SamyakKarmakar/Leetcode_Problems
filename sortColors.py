class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None. Modify nums in-place.
        """
        l0 = []
        l1 = []
        l2 = []

        for i in range(len(nums)):
            if nums[i] == 0:
                l0.append(nums[i])
            elif nums[i] == 1:
                l1.append(nums[i])
            elif nums[i] == 2:
                l2.append(nums[i])

        l0.extend(l1)
        l0.extend(l2)

        for i in range(len(nums)):
            nums[i] = l0[i]
