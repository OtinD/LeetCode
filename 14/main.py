#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-27 13:37:08
# @Author  : ${Rongbo Wu} (${rnwu@siom.ac.cn})

class Solution(object):
    def LCPo2str(self, str1, str2):
        mlist = []
        length = min(len(str1), len(str2))
        for i in range(0, length):
            if str1[i] == str2[i]:
                mlist.append(str1[i])
            else:
                return ''.join(mlist)
        return ''.join(mlist)
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        elif len(strs) == 2:
            return self.LCPo2str(strs[0], strs[1])
        else:
            return self.longestCommonPrefix([self.LCPo2str(strs[0], strs[1])] + strs[2: len(strs)])

            