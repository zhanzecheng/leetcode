# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/22 下午6:10
# @Author  : zhanzecheng
# @File    : 39. Combination_Sum.py
# @Software: PyCharm
"""
"""
这个使用了深度优先的策略来做搜索
"""
class Solution:
    def __init__(self):
        self.data = []
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(candidates)
        for i in range(length):
            self._DFS(candidates[i:], target, [candidates[i]].copy())
        return self.data

    def _DFS(self, candidates, target, result=[]):
        length = len(candidates)
        for i in range(length):
            if sum(result) > target:
                return
            if sum(result) == target and result not in self.data:
                self.data.append(result)
            tmp = result.copy()
            tmp.append(candidates[i])
            self._DFS(candidates[i:], target, tmp)

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
    candidates = [2,3, 5]
    taget = 8
    solution.combinationSum(candidates, target=taget)
    print(solution.data)