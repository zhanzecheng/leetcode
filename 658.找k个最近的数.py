# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/11 下午7:57
# @Author  : zhanzecheng
# @File    : 658.找k个最近的数.py
# @Software: PyCharm
"""

# 我的想法是使用二叉搜索 再加指针的形式来添加
class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # 不论怎么样，这里先使用二叉搜索试一下, 这里写一下二叉搜索
        low = 0
        high = len(arr) - 1
        while low < high:
            mid = (low + high) // 2
            if arr[mid] == x:
                l = mid
                break
            elif arr[mid] > x:
                high = mid - 1
            else:
                low = mid + 1
        i = low - 1
        j = low + 1
        length = len(arr)
        re = [arr[low]]
        k -= 1
        while k > 0:
            if i < 0 and j >= length:
                break
            if i < 0:
                re = re + [arr[j]]
                j += 1
                if j >= length:
                    break
                k -= 1
                continue
            if j >= length:
                re = [arr[i]] + re
                i -= 1
                if i < 0:
                    break
                k -= 1
                continue
            if abs(x - arr[i]) > abs(x - arr[j]):
                re = re + [arr[j]]
                j += 1
                k -= 1
                continue
            else:
                re = [arr[i]] + re
                i -= 1
                k -= 1
        return re
