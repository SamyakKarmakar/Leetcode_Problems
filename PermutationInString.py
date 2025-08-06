class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_sorted = ''.join(sorted(s1))  
        len_s1 = len(s1)                       

    
        for i in range(len(s2) - len_s1 + 1):
            window = s2[i:i+len_s1]  
            check_string=''.join(sorted(window))                 
            if check_string == s1_sorted: 
                return True

        return False
            
   
