class Solution(object):
    def twoSum(self, nums, target):
        new_list=[]
        for i in range (len(nums)):
            for j in range (i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                        new_list.append(i);
                        new_list.append(j);
        return new_list;

    nums=[2,7,11,15]
    target=17        

        