#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-11 15:51:18
# @Author  : ${Rongbo Wu} (${rnwu@siom.ac.cn})

class N_Sum(object):
    """docstring for N_Sum"""
    def __init__(self):
        pass

    def two_Sum(self, mlist, target, Sorted=False, OO=False):
        if not Sorted:
            mlist.sort()
        i = 0
        j = len(mlist) - 1
        ans_list = []
        while i < j:
            Sum = mlist[i] + mlist[j]
            if Sum == target:
                ans_list.append([mlist[i], mlist[j]])
                if OO:
                    break
                i += 1
                j -= 1
                while i < j and mlist[i - 1] == mlist[i] and mlist[j + 1] == mlist[j]:
                    i += 1
                    j -= 1
            elif Sum > target:
                j -= 1
            else:
                i += 1
        return ans_list

    def three_Sum(self, mlist, target, Sorted=False, OO=False):
        if not Sorted:
            mlist.sort()
        i = 0
        ans_list = []
        while i < len(mlist) and 3 * mlist[i] <= target:
            new_target = target - mlist[i]
            pre_ans_list = self.two_Sum(mlist[i + 1: len(mlist)], new_target, Sorted=True, OO=OO)
            while pre_ans_list != []:
                register = pre_ans_list.pop()
                ans_list.append([mlist[i], register[0], register[1]])
            if OO and ans_list != []:
                break
            i += 1
            while i < len(mlist) and mlist[i - 1] == mlist[i]:
                i += 1
        return ans_list 


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        Max = nums[len(nums) - 1] + nums[len(nums) - 2] + nums[len(nums) - 3]
        Min = nums[0] + nums[1] + nums[2]
        if target >= Max:
            return Max
        elif target <= Min:
            return Min
        else:
            flag = True
            btarget = target
            starget = target
            while flag:
                if N_Sum().three_Sum(nums, btarget, Sorted=True, OO= True) != []:
                    return btarget
                starget -= 1
                if N_Sum().three_Sum(nums, starget, Sorted=True, OO= True) != []:
                    return starget
                btarget += 1
        

mlist = [6,-18,-20,-7,-15,9,18,10,1,-20,-17,-19,-3,-5,-19,10,6,-11,1,-17,-15,6,17,-18,-3,16,19,-20,-3,-17,-15,-3,12,1,-9,4,1,12,-2,14,4,-4,19,-20,6,0,-19,18,14,1,-15,-5,14,12,-4,0,-10,6,6,-6,20,-8,-6,5,0,3,10,7,-2,17,20,12,19,-13,-1,10,-1,14,0,7,-3,10,14,14,11,0,-4,-15,-8,3,2,-5,9,10,16,-4,-3,-9,-8,-14,10,6,2,-12,-7,-16,-6,10]
A = Solution()
print A.threeSumClosest(mlist, -52)

