# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/30 下午10:35
# @Author  : zhanzecheng
# @File    : 89.灰码.py
# @Software: PyCharm
"""


# 这个不懂

# 这一题又是一个充满了trick的题目

# TODO: check 1
class Solution(object):
    def grayCode(self, n):
        results = [0]
        for i in range(n):
            print(results)
            results += [x + pow(2, i) for x in reversed(results)]

        return results



if __name__ == '__main__':
    solution = Solution()
    n = 2
    print(solution.grayCode(n))