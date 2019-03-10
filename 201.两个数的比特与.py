# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/6 上午10:45
# @Author  : zhanzecheng
# @File    : 201.两个数的比特与.py
# @Software: PyCharm
"""

# 这题是一个范围的与运算

# trick味十足
# TODO: check 1

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        result = 1
        while m != n:
            m = m >> 1
            n = n >> 1
            result = result << 1


        return result * m

if __name__ == '__main__':
    solution = Solution()
    print(solution.rangeBitwiseAnd(5,7))
