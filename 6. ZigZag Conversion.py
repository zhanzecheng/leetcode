# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/17 下午2:53
# @Author  : zhanzecheng
# @File    : 6. ZigZag Conversion.py
# @Software: PyCharm
"""

'''
单纯的画Z字，考虑到主要是使用到了list的list
'''


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        if numRows == 1:
            return s
        answer = []
        for i in range(numRows):
            answer.append([])
        total = numRows * 2 - 2
        itera = int(len(s) / total)
        for i in range(itera):
            for j in range(total * i, total * i + numRows):
                answer[j - total * i].append(s[j])
            for j in range(total * i + numRows, total * i + numRows * 2 - 2):
                answer[numRows - (j - (total * i + numRows)) - 2].append(s[j])

        res = int(len(s) % total)
        for i in range(len(s) - res, len(s)):
            if i - (len(s) - res) >= numRows:
                answer[numRows - (i - (len(s) - res) - numRows) - 2].append(s[i])
            else:
                answer[i - (len(s) - res)].append(s[i])
        result = ""
        for i in range(numRows):
            for c in answer[i]:
                result += c
        return result