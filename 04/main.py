#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-14 17:54:27
# @Author  : ${Rongbo Wu} (${rnwu@siom.ac.cn})

class Solution(object):
    def sortlists(self, list1, list2):
        len1 = len(list1)
        len2 = len(list2)
        lenall = len1 + len2
        j = 0
        k = 0
        mlist = []
        for i in range(0, lenall):
            if j == len1:
                for kk in range(k, len2):
                    mlist.append(list2[kk])
                break
            elif k == len2:
                for jj in range(j, len1):
                    mlist.append(list1[jj])
                break
            elif list1[j] < list2[k]:
                mlist.append(list1[j])
                j += 1
            else:
                mlist.append(list2[k])
                k += 1
        return mlist, lenall
    def findMedianSortedArrays(self, nums1, nums2):
        [nums, lenall] = self.sortlists(nums1, nums2)
        if lenall % 2 == 0:
            return (nums[lenall/2] + nums[lenall/2 - 1]) / 2.0
        else:
            return nums[lenall/2]

nums1 = [1, 2]
nums2 = [3, 4]
print Solution().findMedianSortedArrays(nums1, nums2)
