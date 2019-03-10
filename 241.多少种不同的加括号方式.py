# -*- coding: utf-8 -*-
"""
# @Time    : 2018/7/5 上午11:13
# @Author  : zhanzecheng
# @File    : 241.多少种不同的加括号方式.py
# @Software: PyCharm
"""
class Solution:
    def help(self, m, n, op):
        if op == '+':
            return m + n
        elif op == '-':
            return m - n
        else:
            return m * n
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        # 这一题很有意思
        if input.isdigit():
            return [int(input)]
        ans = []
        for i in range(len(input)):
            if input[i] in '+-*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        ans.append(self.help(l, r, input[i]))
        return ans