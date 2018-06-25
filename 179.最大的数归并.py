# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/23 上午10:38
# @Author  : zhanzecheng
# @File    : 179.最大的数归并.py
# @Software: PyCharm
"""


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return '0'

        lists = self.mergeSort(nums)
        re = ""
        for i in lists:
            re += str(i)
        return re

    def mergeSort(self, lists):
        if len(lists) < 2:
            return lists

        nums = len(lists) // 2
        left = self.mergeSort(lists[:nums])
        right = self.mergeSort(lists[nums:])
        # print(left , right)
        return self.merge(left, right)

    def cmp(self, a, b):
        a = str(a)
        b = str(b)
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] > b[j]:
                return True
            elif a[i] < b[j]:
                return False
            else:
                i += 1
                j += 1
        if i == len(a):
            if self.cp(b[i:], a):
                return False
            return True
        if j == len(b):
            print(a, b, self.cp(a[j:], b), a[j:], b)
            if self.cp(a[j:], b):
                return True
            return False
        return True

    def cp(self, a, b):
        a = str(a)
        b = str(b)
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] > b[j]:
                return True
            elif a[i] < b[j]:
                return False
            else:
                i += 1
                j += 1
        if j == len(b):
            if a[j] > b[0]:
                return True
        return False

    def merge(self, numsA, numsB):
        i = 0
        j = 0
        numsC = []
        while i < len(numsA) and j < len(numsB):
            if self.cmp(numsA[i], numsB[j]):
                numsC.append(numsA[i])
                i += 1
            else:
                numsC.append(numsB[j])
                j += 1
        while i < len(numsA):
            numsC.append(numsA[i])
            i += 1
        while j < len(numsB):
            numsC.append(numsB[j])
            j += 1
        return numsC

if __name__ == '__main__':
    solution = Solution()
    data = [2281, 2]
    print(solution.largestNumber(data))

    # a = "98909827968595339456944893859149094902689398937839883538183810810780707982784676057536747174237321720571007032685668066758674466986636554651163276306626562416221603859725909578457125682552954605422520849804812479847044453428339323905384638363699366436503636357535673516346233993298316330843021297028227452732697246523622362231322281216213206020001921763154815181495141713801147114310901048"
    #
    # b = "98909827968595339456944893859149094902689398937839883538183810810780707982784676057536747174237321720571007032685668066758674466986636554651163276306626562416221603859725909578457125682552954605422520849804812479847044453428339323905384638363699366436503636357535673516346233993298316330843021297028227452732697246523622362231322812216213206020001921763154815181495141713801147114310901048"
    # count = 0
    # for i, j in zip(a, b):
    #
    #     if i != j:
    #         print(i, j, count)
    #     count += 1