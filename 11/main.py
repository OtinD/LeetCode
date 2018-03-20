#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-20 19:04:48
# @Author  : ${Rongbo Wu} (${rnwu@siom.ac.cn})

def mymax(a, b):
    return a if a > b else b

def mymin(a, b):
    return a if a < b else b

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        Smax = 0
        while i != j:
            Smax = mymax(Smax, (j - i) * mymin(height[i], height[j]))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return Smax

A = Solution()
print A.maxArea([28,342,418,485,719,670,878,752,662,994,654,504,929,660,424])
print mymax(1, 2)