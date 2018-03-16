#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-16 13:05:26
# @Author  : ${Rongbo Wu} (${rnwu@siom.ac.cn})

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        [x, sign] = [x, 1] if x >= 0 else [-x, -1]
        mlist = []
        num = 0
        while x > 0:
            mlist.append(x%10)
            x = x/10
        for i in range(0, len(mlist)):
            num = num * 10 + mlist[i]
        if num > 2 ** 31 - 1:
            return 0
        num = sign * num
        return num

x = 1534236469
print Solution().reverse(x)