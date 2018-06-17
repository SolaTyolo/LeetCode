# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.


#####################
#  
# TIP:
#   水平两两比较 ,拿出最大公前缀     
# 
#   Accepted  Runtime: 44 ms
# 
#####################
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        prefix = strs[0]
        for s in strs:
            if prefix =='':
                break
            count = 0
            # 以长度小的为遍历源
            for index in range(min(len(s),len(prefix))):
                if prefix[index] != s[index]:
                    break
                count +=1
            prefix=prefix[:count]
                
        return prefix

#####################
#  
# TIP:
#   垂直扫描,遇到不是一样的字母即可返回     
# 
#   Accepted  Runtime: 40 ms
# 
#####################
class Solution1:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        ## 针对python的高级函数ZIP，可以将方法优化如下
        if not strs:   #if strs = []
            return("")
        ## 将strs用zip(*list)拆分成各字母的元组 
        for i, letter_group in enumerate(zip(*strs)):
        ## 碰到拆分元组去重后元素大于1个的就说明无公前缀了
            if len(set(letter_group)) > 1:
                return(strs[0][:i])
            
        ##if shortest string is the common prefix or strs contains ""
        else:
            return(min(strs))



# tests
def main():
    x = ["flower","flow","flight"]
    # x = ["dog","racecar","car"]
    # x = ["aca","cba"]
    sol = Solution()
    res = sol.longestCommonPrefix(x)
    print(res)

if __name__ == '__main__':
    main()
