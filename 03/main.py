#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-14 11:03:31
# @Author  : ${Rongbo Wu} (${rnwu@siom.ac.cn})

class mylist(list):
    def exist(self, a):
        list_len = len(self)
        if list_len == 0:
            return 0
        flag = 0
        for i in range(0, list_len):
            if a == self[i]:
                flag = 1
                break
        return flag, i
    def move(self, i):
        for j in range(0, i+1):
            self.pop(0)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mlist = mylist()
        flag = 0
        for i in range(0, len(s)):
            if len(mlist) == 0:
                mlist.append(s[i])
            elif mlist.exist(s[i])[0]:
                '计数'
                if flag < len(mlist):
                    flag = len(mlist)
                mlist.move(mlist.exist(s[i])[1])
                mlist.append(s[i])
                continue
            else:
                mlist.append(s[i])
        if flag < len(mlist):
            flag = len(mlist)
        return flag



        

s = 'dvdf'


#for i in range(0, len(s)):
#    mlist.append(s[i])
# print mlist
# mlist.move(1)
# print mlist


print Solution().lengthOfLongestSubstring(s)
