class Solution(object):
    def reverse(self, x):
        rev=0
        INT_MIN = -2**31         
        INT_MAX = 2**31 - 1       

        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_x = int(str(x)[::-1]) * sign

        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        return reversed_x
        
