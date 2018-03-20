#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-20 19:51:30
# @Author  : ${Rongbo Wu} (${rnwu@siom.ac.cn})

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        l1 = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        l2 = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        l3 = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        l4 = ['', 'M', 'MM', 'MMM']
        l = [l1, l2, l3, l4]
        R = []
        print l[0][num % 10]
        for i in range(0, 4):
            R.insert(0, l[i][num % 10])
            num = num/10
        print R[0] + R[1] + R[2] + R[3]

A = Solution()
A.intToRoman(3999)


