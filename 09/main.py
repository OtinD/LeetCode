#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-16 16:21:58
# @Author  : ${Rongbo Wu} (${rnwu@siom.ac.cn})

'''
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        y = 0
        while y <= x:
            y = y * 10 + x % 10
            if y == 0:
                return False
            x = x / 10
            if y == x or y == x/10:
                return True
        return False

x = 21120
A = Solution()
print A.isPalindrome(x)