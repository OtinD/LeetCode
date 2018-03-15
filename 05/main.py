#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-15 13:40:53
# @Author  : ${Rongbo Wu} (${rnwu@siom.ac.cn})

class Solution(object):
    flag = 0
    s_len = 0
    string = ''
    def Pa_or_not(self, s, i):
        if 2 * (self.s_len - 1 - i) < self.flag or i == 0:
            if self.s_len >= 2 and s[0] == s[1]:
                return 2, s[0: 2]
            return 1, s[i]
        length1 = 0
        if s[i] == s[i + 1]:
            length1 = 2
            ista = i
            isto = i + 1
            while (ista - 1 >= 0 and isto + 1 <= self.s_len - 1) and s[ista - 1] == s[isto + 1]:
                ista -= 1
                isto += 1
                length1 += 2
        ista = i
        isto = i
        length2 = 1
        while (ista - 1 >= 0 and isto + 1 <= self.s_len - 1) and s[ista - 1] == s[isto + 1]:
            ista -= 1
            isto += 1
            length2 += 2
        length = length1 if length1 > length2 else length2
        string = s[i - length/2 + 1: i + length / 2 + 1] if length % 2 == 0 else s[i - length / 2: i + length / 2 + 1]
        return length, string

    def longestPalindrome(self, s):
        self.s_len = len(s)
        for i in range(0, self.s_len):
            [length, string] = self.Pa_or_not(s, i)
            [self.flag, self.string] = [length, string] if length > self.flag else [self.flag, self.string]
        return self.string

s = 'ccc'
A = Solution()
A.longestPalindrome(s)
print A.flag
print A.string