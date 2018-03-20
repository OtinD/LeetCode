#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-20 16:18:11
# @Author  : ${Rongbo Wu} (${rnwu@siom.ac.cn})

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        while p != '':
            if len(p) < 2 or p[1] != '*':
                if s == '' :
                    return False
                if s[0] != p[0] and p[0] != '.':
                    return False
                s = s[1: len(s)] if len(s) != 1 else ''
                p = p[1: len(p)] if len(p) != 1 else ''
            else:
                if p[0] != '.':
                    if len(p) > 2:
                        while not self.isMatch(s, p[2: len(p)]):
                            if s == '':
                                return False
                            if s[0] == p[0]:
                                s = s[1: len(s)] if len(s) != 1 else ''
                            else:
                                return False
                        return True
                    else:
                        s = s.lstrip(p[0])
                        return s == ''
                elif len(p) > 2:
                    while not self.isMatch(s, p[2: len(p)]):
                        if s == '':
                            return False
                        s = s[1: len(s)] if len(s) != 1 else ''
                    return True
                else:
                    return True
#                p = p[2: len(p)] if len(p) != 2 else ''
        return len(s) == 0

A = Solution()
print A.isMatch('bbbba', '.*a*a')
# aa = 'bbbb'
# print aa.lstrip('b') 