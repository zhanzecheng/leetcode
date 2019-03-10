# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/2 上午11:49
# @Author  : zhanzecheng
# @File    : 22.产生合法括号.py
# @Software: PyCharm
"""

# 这一题的递归也是用的很好
# TODO: check 1
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self.generate(n, 0, "")
        return self.result

    def generate(self, m, n, tmp):
        if m == 0 and n == 0:
            self.result.append(tmp)
            return
        if n > 0:
            self.generate(m, n - 1, tmp + ')')
        if m > 0:
            self.generate(m - 1, n + 1, tmp + '(')

if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))