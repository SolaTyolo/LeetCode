# -*- coding: utf-8 -*-

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example:
#   Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#   Output: 7 -> 0 -> 8
#   Explanation: 342 + 465 = 807.
#

import sys
#####################
# 
# Accepted 136ms
#
#####################

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rtype = ListNode(None)
        self.cur_node = None
        self.carry = 0
        while l1 and l2:
            sum_l = self.cal(l1.val + l2.val)
            rtype = self.add(sum_l)
            l1 = l1.next
            l2 = l2.next
		
        while l1:
            sum_l = self.cal(l1.val)
            rtype = self.add(sum_l)
            l1 = l1.next
        while l2:
            sum_l = self.cal(l2.val)
            rtype = self.add(sum_l)
            l2 = l2.next
        if self.carry:
            rtype = self.add(self.carry)

        return self.reverse(rtype)
    
    def cal(self, data):
        if self.carry:
            data = data + 1
            self.carry = 0
        if data >= 10:
            self.carry = 1
        return data % 10


    def add(self,data):
        node = ListNode(data)
        node.next = self.cur_node
        self.cur_node = node
        return node
    
    def reverse(self,listnode):
        self.cur_node = None
        new_node = ListNode(None)
        while listnode :
            new_node = self.add(listnode.val)
            listnode = listnode.next
        return new_node
        
###############################
#
# 分析上述的程序，发现三个while可以结合成一个while，
# 其他时间的开销在于多做了一次reverse,
# 可引入一个head指针驻扎首位，另一个游标指针cur进行遍历
#
#  Accepted 120ms
#
###############################


class Solution1:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = cur = ListNode(None)
        carry = 0
        while l1 or l2 or carry:
            if l1 :
                carry = l1.val + carry
                l1 = l1.next
            if l2 :
                carry = l2.val + carry
                l2 = l2.next
            cur.next = ListNode(carry % 10) #取模
            cur = cur.next
            carry = carry // 10  #取整
        return head.next

#test

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class ListNodeHandle:
    def __init__(self):
        self.cur_node = None
    
    def add(self,data):
        node = ListNode(data)
        node.next = self.cur_node
        self.cur_node = node
        return node
    
    def printList(self,list_node):
        while list_node:
            print(list_node.val)
            print('↓')
            list_node = list_node.next
        print('None')

def main():
    nodeAction_1 = ListNodeHandle()
    l1 = ListNode(None)
    for i in [5][::-1]:
        l1 = nodeAction_1.add(i)
    #nodeAction_1.printList(l1)
    #print('======')
    nodeAction_2 = ListNodeHandle()
    l2 = ListNode(None)
    for i in [5][::-1]:
        l2 = nodeAction_2.add(i)
    #nodeAction_2.printList(l2)
    sol = Solution1()
    l3 = sol.addTwoNumbers(l1,l2)
    nodeAction_3 = ListNodeHandle()
    print('======')
    nodeAction_3.printList(l3)

if __name__ == '__main__':
    main()
