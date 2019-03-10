# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/18 上午9:54
# @Author  : zhanzecheng
# @File    : 491.找出全部递增字串.py
# @Software: PyCharm
"""

# TODO: check 1
# 每一个dfs有自己的visit，并且用了nums[i+1:]的形式来避免引用
class Solution(object):
    def findSubsequences(self, nums):
        res = []

        def dfs(nums, path):
            if len(path) > 1:
                res.append(path)

            # 这里其实是每一个搜索有一个自己的visit
            visited = []
            for i in range(len(nums)):
                if nums[i] in visited:
                    # 去掉重复的情况
                    continue

                # 这里就很巧妙的使用了visited数组
                if not path or nums[i] >= path[-1]:
                    visited.append(nums[i])
                    dfs(nums[i + 1:], path + [nums[i]])

        if nums:
            dfs(nums, [])

        return res