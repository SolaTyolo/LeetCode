# -*- coding: utf-8 -*-

# Given a string, find the length of the longest substring without repeating characters.
# 
# Example:
#   Given "abcabcbb", the answer is "abc", which the length is 3.
#
#   Given "bbbbb", the answer is "b", with the length of 1.
#
#   Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#

#####################
#  
# 循环遍历         
# Accepted  Runtime: 348 ms
# 
#####################
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        cur_sub = ''
        max_sub = ''

        for i,c in enumerate(s):
            cur_sub = c
            for v in s[i+1:]:
                if v not in cur_sub:
                    cur_sub += v
                    continue
                break
            if len(cur_sub) > len(max_sub):
                max_sub = cur_sub
    
        return len(max_sub)

#####################
#  
# Tip:
#   分析上述方法可知
#   用个小集合来判断是否存在重复值时低效的
#   可用哈希来记录字符和位置的映射
#   而上述方法都是通过step by step的
#   分析可知道当遇到重复值S[i]和S[j](i < j)时
#   可直接从i+1开始(因为从start到i的遍历都会遇到s[j]这个重复值)
#         
# Accepted  Runtime: 76 ms
# 时间复杂度O(n)
#####################
class Solution1:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        hashTable = {}
        max_len = 0
        cur = 0

        for i,c in enumerate(s):
            if c in hashTable and cur <= hashTable[c] :
                cur = hashTable[c] + 1
            else:
                max_len = max(max_len,i - cur + 1)
            hashTable[c] = i 

        return max_len



# tests
def main():
    #s = 'abcabcbb'
    s = 'pwwkew'
    sol = Solution()
    res = sol.lengthOfLongestSubstring(s)
    print(res)

if __name__ == '__main__':
    main()
