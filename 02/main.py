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
	def num2node(self, num):
		'Transform number to ListNode'
		A = ListNode(num % 10)
		mNode = A
		num = num / 10
		while num != 0:
			A.next = ListNode(num % 10)
			A = A.next
			num = num / 10
		return mNode
    	def addTwoNumbers(self, l1, l2):
    		'You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.'
    		return self.num2node(self.getnum(l1) + self.getnum(l2))

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
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

print Solution().getnum(Solution().addTwoNumbers(l1, l2))

print Solution().num2node(0).next
