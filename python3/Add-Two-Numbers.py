# -*- coding: utf-8 -*-

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example:
#   Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#   Output: 7 -> 0 -> 8
#   Explanation: 342 + 465 = 807.
#


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rtype = ListNode(None)
        self.cur_node = None
        carry = 0
        while l1 and l2:
            sum_l = l1.val + l2.val
            if carry:
                sum_l = sum_l + 1
            if sum_l >= 10:
                carry = 1
            rtype = self.add(sum_l%10)
            l1 = l1.next
            l2 = l2.next
		
        if l1:
            rtype.next = l1
        if l2 :
            rtype.next = l2

        return self.reverse(rtype)
    
    def add(self,data):
        node = ListNode(data)
        node.next = self.cur_node
        self.cur_node = node
    
    def reverse(self,listnode):
        self.cur_node = None
        new_node = ListNode(None)
        while listnode :
            new_node = self.add(listnode.val)
            listnode = listnode.next
        return new_node
        


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

def main():
    nodeAction_1 = ListNodeHandle()
    l1 = ListNode(None)
    for i in [2,4,3][::-1]:
        l1 = nodeAction_1.add(i)

    nodeAction_2 = ListNodeHandle()
    l2 = ListNode(None)
    for i in [5,6,4][::-1]:
        l2 = nodeAction_2.add(i)
    sol = Solution()
    l3 = sol.addTwoNumbers(l1,l2)
    print(l3.val)

if __name__ == '__main__':
    main()