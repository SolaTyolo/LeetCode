# -*- coding: utf-8 -*-

# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# 
# Example:
#   Input: 121
#   Output: true
#
#   Input: -121
#   Output: false
#
#   Input: 10
#   Output: false
#
# Follow up:

# Coud you solve it without converting the integer to a string?
#####################
#  
# TIP:
#   根据定义来执行翻转        
# 
#   Accepted  Runtime: 308 ms
# 
#####################
# -*- coding: UTF-8 -*-
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x%10 == 0 and x!=0):
            return False 
        new = 0 
        old = x
        while x:
            new = new * 10 + x %10
            x //= 10 

        return  new == old

# tests
def main():
    x = 121
    #x = -123
    #x = 120
    sol = Solution()
    res = sol.isPalindrome(x)
    print(res)

if __name__ == '__main__':
    main()
