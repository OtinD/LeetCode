#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# 
# You may assume that each input would have exactly one olution, and you may not use the same element twice.# 

class Solution(object):
#	def __init__(selt):
#		pass
	def twoSum(self, nums, target):
		'Given an array of integers, return indices of the two numbers such that they add up to a specific target.\nYou may assume that each input would have exactly one olution, and you may not use the same element twice.'
     		"""
     		:type nums: List[int]
     		:type target: int
     		:rtype: List[int]
     		"""
     		list_len = len(nums)
     		value = range(0, list_len)
     		dictionary = dict(zip(nums, value))
     		for i in range(0, list_len):
     			compliment = target - nums[i]
     			if compliment in dictionary and dictionary[compliment] != i:
     				return (i, dictionary[compliment])
     		print "no exist"
#        	list_len = len(nums)
#		flag = 0
#		for i1 in range(0, list_len - 1):
#			for i2 in range(i1 + 1, list_len):
#				if nums[i1] + nums[i2] == target:
#					flag = True
#					break
#			if flag:
#				break
#			i1 = i1 + 1
#		if flag:
#			return (i1, i2)
#		else:
#			print "no exist"

nums = [2, 7, 23, 4]
target = 6
a = Solution()
print a.twoSum(nums, target)

