class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area=0
        left=0
        right=len(height)-1
        while left<right:
            h=min(height[left],height[right])
            w=right-left
            area=max(area,h*w)
            if (height[left]<height[right]):
                left=left+1
            else:
                right=right-1
        return area        
        
