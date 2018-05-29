# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/28 下午8:03
# @Author  : zhanzecheng
# @File    : 90.子集II.py
# @Software: PyCharm
"""

class Solution:
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            tmp = [item+[num] for item in res]
            res = res + tmp
        result = []
        for i in res:
            if i not in result:
                result.append(i)
        return result


if __name__ == '__main__':
    data = [1, 2, 2]
    solution = Solution()
    print(solution.subsets(data))