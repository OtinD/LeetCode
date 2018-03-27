#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-27 14:26:50
# @Author  : ${Rongbo Wu} (${rnwu@siom.ac.cn})

import random
import time

class Sorting(object):
    def __init__(self):
        pass

    def randomlist(self, length=10000, min=-100, max=100):
        mlist = []
        for i in range(0, length):
            mlist.append(random.randint(min, max))
        return mlist

    def test(self, func, num=100):
        start = time.clock()
        for i in range(0, num):
            l = self.randomlist()
#            if i == num - 1:
#                print l
            l = func(l)
            length = len(l)
            for j in range(0, length - 1):
                if l[j] > l[j + 1]:
                    print 'Bug!'
                    print l
                    return False
#        print l
        end = time.clock()
        print 'Work well for %d turns, use %fs per turn'% (num, (end - start)/num)
        return True

    def switch(self, l, i, j):
        register = l[i]
        l[i] = l[j]
        l[j] = register
        return None

    def BubbleSort(self, ml):
        # 切片赋值则不会更改ml的值
        l = ml[:]
        length = len(l)
        register = None
        for i in range(0, length - 1):
            for j in range(0, length - i - 1):
                if l[j] > l[j + 1]:
                    self.switch(l, j, j+1)
        return l

    def SelectionSort(self, ml):
        l = ml[:]
        for i in range(0, len(l)):
            [mmin, index] = [l[i], 0]
            register = None
            for j in range(i, len(l)):
                [mmin, index] = [l[j], j] if l[j] < mmin else [mmin, index]
            if mmin < l[i]:
                self.switch(l, i, index)
        return l

    def InsertionSort(self, ml):
        l = ml[:]
        for i in range(1, len(l)):
            j = i - 1
            while j >= 0 and l[j] > l[i]:
                j -= 1
            l.insert(j + 1, l[i])
            l.pop(i + 1)
        return l

    def ShellSort(self, ml):
        l = ml[:]
        length = len(l)
        gap = length / 2
        while gap > 0:
            for i in range(0, gap):
                for j in range(i, length, gap):
                    k = j - gap
                    flag = l[j]
                    while k >= 0 and l[k] > flag:
                        self.switch(l, k, k + gap)
                        k -= gap
            gap = gap / 2
        return l

    def MergeSort(self, ml):
        l = ml[:]
        length = len(l)
        if length == 1:
            return l
        elif length == 2:
            if l[0] > l[1]:
                self.switch(l, 0, 1)
            return l
        else:
            index = length / 2
            l1 = self.MergeSort(l[0: index])
            l2 = self.MergeSort(l[index: length])
            i = 0
            j = 0
            mnl = []
            while i < len(l1) or j < len(l2):
                if i >= len(l1):
                    mnl.append(l2[j])
                    j += 1
                elif j >= len(l2) or l1[i] < l2[j]:
                    mnl.append(l1[i])
                    i += 1
                else: 
                    mnl.append(l2[j])
                    j += 1                 
            return mnl

    def QuickSort(self, ml):
        l = ml[:]
        length = len(l)
        if length == 0:
            return []
        elif length == 1:
            return l
        pivot = l[0]
        pivot_index = 0
        for i in range(1, length):
            if l[i] < pivot:
                l.insert(pivot_index, l[i])
                l.pop(i + 1)
                pivot_index += 1
            else:
                l.insert(pivot_index + 1, l[i])
                l.pop(i + 1)
        l[0: pivot_index] = self.QuickSort(l[0: pivot_index])
        if pivot_index < length - 1:
            l[pivot_index + 1: length] = self.QuickSort(l[pivot_index + 1: length])
        return l



A = Sorting()
A.test(A.ShellSort)
mlist = A.randomlist()
# print A.MergeSort(mlist)
