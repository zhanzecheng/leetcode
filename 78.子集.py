# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/28 下午7:45
# @Author  : zhanzecheng
# @File    : 78.子集.py
# @Software: PyCharm
"""
"""
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""
class Solution:
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res

