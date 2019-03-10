# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/27 下午4:54
# @Author  : zhanzecheng
# @File    : 55.跳跳游戏.py
# @Software: PyCharm
"""

# 从后往前遍历， 用dis标示距离，判断是否可以到，最后用nums【0】来判断是否可以到

# TODO: check 1
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        dis = 1
        length = len(nums)
        for i in range(length - 2, -1, -1):
            if nums[i] >= dis:
                dis = 0
            dis += 1
        return nums[0] >= dis



if __name__ == '__main__':
    solution = Solution()
    example = [2,3,1,1,4]
    print(solution.canJump(example))