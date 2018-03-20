#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-20 20:15:50
# @Author  : ${Rongbo Wu} (${rnwu@siom.ac.cn})

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        num = 0
        while i != len(s):
            if i != len(s) - 1:
                [i, num] = [i + 1, num + d[s[i]]] if d[s[i]] >= d[s[i + 1]] else [i + 2, num + d[s[i + 1]] - d[s[i]]]
            else:
                [i, num] = [i + 1, num + d[s[i]]]
            print num
        return num

A = Solution()
print A.romanToInt('MCMXCVI')