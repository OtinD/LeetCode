#!/usr/bin/python
# -*- coding: UTF-8 -*-

'Definition for singly-linked list.'
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getnum(self, mNode):
        mlist = [mNode.val]
        A = mNode.next
        while A != None:
            mlist.insert(0, A.val)
            A = A.next
        return reduce(lambda x, y: x*10 + y, mlist)
    def addTwoNumbers(self, l1, l2):
        'You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.'
        jinwei = (l1.val + l2.val)/10
        yushu = (l1.val + l2.val)%10
        l3 = ListNode(yushu)
        A = l3
        while l1.next != None or l2.next != None or jinwei != 0:
            if l1.next == None and l2.next == None:
                A.next = ListNode(jinwei)
                return l3
            elif l1.next == None:
                yushu = l2.next.val
                A.next = ListNode((yushu + jinwei)%10)
                A = A.next
                jinwei = (yushu + jinwei)/10
                l2 = l2.next
            elif l2.next == None:
                yushu = l1.next.val
                A.next = ListNode((yushu + jinwei)%10)
                A = A.next
                jinwei = (yushu + jinwei)/10
                l1 = l1.next
            else:
                yushu = (l1.next.val + l2.next.val)%10
                A.next = ListNode((yushu + jinwei)%10)
                A = A.next
                jinwei = (l1.next.val + l2.next.val + jinwei)/10
                l1 = l1.next
                l2 = l2.next
        return l3



l1 = ListNode(3)
l1.next = ListNode(7)

l2 = ListNode(9)
l2.next = ListNode(2)
# l2.next.next = ListNode(1)

#
#a = 807998
#l3 = ListNode(a % 10)
#a = a / 10
#A = ListNode(a % 10)
#l3.next = A
#a = a / 10
#while a != 0:
#	A.next = ListNode(a % 10)
#	A = A.next
#	a = a / 10

a = Solution().addTwoNumbers(l1, l2)

print Solution().getnum(Solution().addTwoNumbers(l1, l2))
print a.next.next.val


