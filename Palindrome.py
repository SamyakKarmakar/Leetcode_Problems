class Solution(object):
    def isPalindrome(self, x):
        temp=x
        rev=0
        if x<0:
            return False
        while(temp!=0):
            last_digit=temp%10
            rev=rev*10+last_digit
            temp=temp/10
        return x==rev
