# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/31 上午9:34
# @Author  : zhanzecheng
# @File    : 118.pascal三角形.py
# @Software: PyCharm
"""

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = []
        res.append([1])
        res.append([1, 1])
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return res
        for i in range(2, numRows ):
            tmp = []
            pre = res[i-1].copy()
            pre.insert(0, 0)
            pre.append(0)
            length = len(pre)
            for j in range(length-1):
                tmp.append(pre[j] + pre[j+1])
            res.append(tmp)
        return res
if __name__ == '__main__':
    solution = Solution()
    print(solution.generate(5))
