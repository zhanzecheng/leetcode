# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/31 下午8:40
# @Author  : zhanzecheng
# @File    : 119.pascal三角形II.py
# @Software: PyCharm
"""


class Solution:
    def getRow(self, numRows):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        numRows += 1
        if numRows == 0:
            return []
        res = []
        res.append([1])
        res.append([1, 1])
        if numRows == 1:
            return [1]
        if numRows == 2:
            return res[-1]
        for i in range(2, numRows ):
            tmp = []
            pre = res[i-1].copy()
            pre.insert(0, 0)
            pre.append(0)
            length = len(pre)
            for j in range(length-1):
                tmp.append(pre[j] + pre[j+1])
            res.append(tmp)
        return res[-1]