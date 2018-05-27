# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/27 下午4:54
# @Author  : zhanzecheng
# @File    : 55.跳跳游戏.py
# @Software: PyCharm
"""
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