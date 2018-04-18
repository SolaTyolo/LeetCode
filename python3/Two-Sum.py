# -*- coding: utf-8 -*-

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
# Example:
#   Given nums = [2, 7, 11, 15], target = 9,
#   Because nums[0] + nums[1] = 2 + 7 = 9,
#   return [0, 1].
#

#####################
#  
# 纯暴力超时 T-T         
# Time Limit Exceeded
#               
#####################
class Solution:
    def twoSum(self, nums, target):
        # """
        # :type nums: List[int]
        # :type target: int
        # :rtype: List[int]
        # """

        key_list = []
        for index1, value1 in enumerate(nums):
            for index2, value2 in enumerate(nums):
                if index1 == index2:
                    continue
                if value1 + value2 == target:
                    key_list = [index1, index2]
                    break
        return sorted(key_list)


##############################################
#
# Tip:
#   针对value1+value2 = target 
#   做个转化成value2 = target - value1
#   在判断value2是否在列表中即可去掉一层循环
#
# Accepted  Runtime: 1632 ms
#
############################################
class Solution1(object):
    def twoSum(self, nums, target):
        # """
        # :type nums: List[int]
        # :type target: int
        # :rtype: List[int]
        # """
        
        key_list = []
        for index1, value1 in enumerate(nums):
            value2 = target - value1
            if value2 in nums:
                index2 = nums.index(value2)
                if index1 != index2:
                    key_list = [index1,index2]
        return sorted(key_list)
# test
def main():
    nums = [3,-3]
    target = 0
    sol = Solution1()
    res = sol.twoSum(nums, target)
    print(res)

if __name__ == '__main__':
    main()
