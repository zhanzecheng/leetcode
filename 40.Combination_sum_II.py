# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/22 下午8:29
# @Author  : zhanzecheng
# @File    : 40.Combination_sum_II.py
# @Software: PyCharm
"""

# TODO: 这里使用了剪枝的操作，可以更快
'''
if i > 1 and candidates[i] == candidates[i - 1]:
    continue
'''


class Solution:
    def __init__(self):
        self.data = []

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self._DFS(candidates, target, [])
        return self.data

    def _DFS(self, candidates, target, result=[]):
        if sum(result) > target:
            return
        if sum(result) == target and result not in self.data:
            self.data.append(result)
            return
        length = len(candidates)
        for i in range(length):
            if i > 1 and candidates[i] == candidates[i - 1]:
                continue
            tmp = result.copy()
            tmp.append(candidates[i])
            self._DFS(candidates[i + 1:], target, tmp)


# TODO：还有一种放在循环外的DFS
'''

def combinationSum(self, candidates, target):
    res = []
    candidates.sort()
    self.dfs(candidates, target, 0, [], res)
    return res

def dfs(self, nums, target, index, path, res):
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return 
    for i in xrange(index, len(nums)):
        self.dfs(nums, target-nums[i], i, path+[nums[i]], res)

'''

if __name__ == '__main__':
    solution = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    taget = 8
    solution.combinationSum(candidates, target=taget)
    print(solution.data)