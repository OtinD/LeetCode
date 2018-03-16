#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-16 11:58:46
# @Author  : ${Rongbo Wu} (${rnwu@siom.ac.cn})

import string

class Solution(object):
    'zigzag Conversion'
    s_len = 0
    gap = 0
    def get_gap(self, numRows):
        if numRows == 1:
            return 1
        return 2 * (numRows - 2) + 2
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        self.s_len = len(s)
        self.gap = self.get_gap(numRows)
        mlist = []
        for i in range(0, numRows):
            j = i
            while j < self.s_len:
                mlist.append(s[j])
                if i != 0 and i != numRows - 1:
                    if j + self.gap - 2 * i < self.s_len:
                        mlist.append(s[j + self.gap - 2 * i])
                j += self.gap
        mstr = ''.join(mlist)
        return mstr

s = 'ABCDE'
A = Solution()
print A.convert(s, 3)
print A.gap
