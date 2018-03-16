#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-16 15:46:14
# @Author  : ${Rongbo Wu} (${rnwu@siom.ac.cn})

'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

 

Requirements for atoi:

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
'''

class Solution(object):
    def exist(self, l, a):
        for i in range(0, len(l)):
            if l[i] == a:
                return True
        return False
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str == '':
            return 0
        num_list = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        sign_list = ['+', '-']
        mlist = []
        i = 0
        sign = 1
        num = 0
        while str[i] == ' ':
            i += 1
        if str[i] == '-':
            sign = -1
        if self.exist(sign_list, str[i]):
            i += 1
        while i < len(str) and str[i] in num_list:
            mlist.append(str[i])
            i += 1
        if mlist == []:
            return 0
        for j in range(0, len(mlist)):
            yushu = num_list[mlist[j]]
            num = num * 10 + yushu
        num = num * sign
        if num > 2147483647:
            return 2147483647
        if num < -2147483648:
            return -2147483648
        return num

s = '123'
A = Solution()
print A.myAtoi(s)
