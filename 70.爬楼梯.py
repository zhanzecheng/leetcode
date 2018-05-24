# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/24 上午9:56
# @Author  : zhanzecheng
# @File    : 70.爬楼梯.py
# @Software: PyCharm
"""

# 这个问题的核心是这个表达式   f(n): f(n-1) + f(n-2) + f(n-3)

# 第二个核心就是利用循环来替换递归提高速度
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        climb = [1, 1]
        for i in range(2, n+1):
            climb.append(climb[i-1] + climb[i-2])
        return climb[-1]

if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(35))