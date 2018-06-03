# -*- coding: utf-8 -*-

# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example:
#   Input: 123
#   Output: 321
#
#   Input: -123
#   Output: -321
#
#   Input: 120
#   Output: 21
#
#  Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

#####################
#  
# TIP:
#   将整数转为字符串，再进行倒序(对首位进行判别)         
# 
#   Accepted  Runtime: 60 ms
# 
#####################
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x >= 0 else -1
        x_str = str(x)
        if flag > 0:
            x_int = x_str[::-1] 
        else:
            x_int = x_str[1:][::-1]
        
        res = flag * int(x_int)


        # 参考Discuss可进行行数的减少
        # flag = [1,-1][x<0]   ##code amaing!!
        # res = flag * int(str(abs(x))[::-1])
        return  res if -(2**31)<=res<=(2**31) - 1 else 0


# tests
def main():
    x = 123
    # x = -123
    # x = 120
    sol = Solution()
    res = sol.reverse(x)
    print(res)

if __name__ == '__main__':
    main()
