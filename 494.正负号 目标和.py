# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/17 上午9:51
# @Author  : zhanzecheng
# @File    : 494.正负号 目标和.py
# @Software: PyCharm
"""

# 注意这个是没有循环的
# 这个超时了 DP的解法：dict[i] -> 给定sum i 有多少种解法


class Solution(object):
    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0

        dic = {nums[0] : 1,-nums[0] : 1} if nums[0] != 0 else {0 : 2}

        for i in range(1, len(nums)):
            tdict = {}
            for d in dic:
                tdict[d + nums[i]] = dic[d] + tdict.get(d+ nums[i], 0)
                tdict[d - nums[i]] = dic[d] + tdict.get(d- nums[i], 0)
            dic = tdict
        return dic.get(S, 0)


class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.count = 0
        length = len(nums)

        def dfs(cur, target):
            if cur == length:
                # print(cur)
                if target == S:
                    self.count += 1

            if cur >= length:

                return

            dfs(cur+1, target + nums[cur])
            dfs(cur+1, target - nums[cur])

        dfs(0, 0)
        return self.count

if __name__ == '__main__':
    solution = Solution()
    data = [1, 1, 1, 1, 1]
    s = 3
    print(solution.findTargetSumWays(data, 3))