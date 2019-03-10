# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/2 下午7:48
# @Author  : zhanzecheng
# @File    : -1.在乱序数组中找第k大的数.py
# @Software: PyCharm
"""

class Solution:


    def findK(self, num, k, l, h):
        if l <= h:
            split = self.partition(num, l, h)
            if h - split == k:
                self.result = num[split]
                return
            else:
                if h - split > k:
                    self.findK(num, k,split+1, h)
                else:
                    self.findK(num, k - ( h -split), l, split-1)


    def partition(self, num, l, h):
        cur = num[l]
        while l < h:
            while l < h and num[h] > cur:
                h -= 1
            num[l] = num[h]
            while l < h and num[l] < cur:
                l += 1
            num[h] = num[l]
        num[l] = cur
        return l

    def majorityElement(self, num, n):
        self.result = -1
        self.findK(num, n, 0, len(num) - 1)
        return self.result

if __name__ == '__main__':
    data = [3,2,1,5,6,4]
    solution = Solution()
    print('--------> 中间大的数是： ', solution.majorityElement(data, len(data) // 2 - 1))
