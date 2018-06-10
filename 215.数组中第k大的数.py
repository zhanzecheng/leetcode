# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/7 下午7:18
# @Author  : zhanzecheng
# @File    : 215.数组中第k大的数.py
# @Software: PyCharm
"""


class Solution:
    def findKthLargest(self, num, n):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n -= 1
        self.result = -1
        self.findK(num, n, 0, len(num) - 1)
        return self.result

    def findK(self, num, k, l, h):
        if l <= h:
            split = self.partition(num, l, h)
            if h - split == k:
                self.result = num[split]
                return
            else:
                if h - split > k:
                    self.findK(num, k, split + 1, h)
                else:
                    self.findK(num, k - (h - split) - 1, l, split - 1)

    # TODO: 这里的快拍一定要大于等于！！！！！！不然会出现死循环
    def partition(self, num, l, h):
        cur = num[l]
        while l < h:

            while l < h and num[h] >= cur:
                h -= 1
            num[l] = num[h]
            while l < h and num[l] <= cur:
                l += 1
            num[h] = num[l]
        num[l] = cur
        return l
if __name__ == '__main__':
    solution = Solution()
    data = [3,2,3,1,2,4,5,5,6]
    k = 1
    print(solution.findKthLargest(data, k))