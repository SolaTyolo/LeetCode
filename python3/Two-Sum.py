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
# 时间复杂度O(n^2)
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
# Accepted  Runtime: 1080 ms
#
# 时间复杂度O(n)
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
                    break
        return sorted(key_list)

##############################################
#
# Tip:
#   上述方法耗时超过了1s
#   而当nums的列表较大时nums.index()就比较耗时了
#   转化个思想把每次的num及索引存在一个集合中(哈希表)
#   这个每次查询 target-num 时都是子集合查询
#   
# Accepted  Runtime: 36 ms
#
# 时间复杂度O(n)
############################################


class Solution2(object):
    def twoSum(self, nums, target):
        # """
        # :type nums: List[int]
        # :type target: int
        # :rtype: List[int]
        # """

        hashtable = {}
        for i, num in enumerate(nums):
            if target-num in hashtable:
                return [hashtable[target-num], i]
            hashtable[num] = i

# test
def main():
    nums = [2, 3,4,2,7, 11, 15]
    target = 9
    sol = Solution2()
    res = sol.twoSum(nums, target)
    print(res)

if __name__ == '__main__':
    main()
