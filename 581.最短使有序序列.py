# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/22 上午11:08
# @Author  : zhanzecheng
# @File    : 581.最短使有序序列.py
# @Software: PyCharm
"""

# TODO: check 1

class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 先对异常值做判断
        if len(nums) == 1:
            return 0
        n = len(nums)
        # 这块理解的不对的
        begin = -1
        end = -2
        max_one = nums[0]
        min_one = nums[-1]
        for i in range(1, len(nums)):
            max_one = max(max_one, nums[i])
            min_one = min(min_one, nums[n - i - 1])
            if max_one != nums[i]:
                end = i
            if min_one != nums[n-i-1]:
                begin = n - i - 1
        print(begin, end)
        return end - begin + 1
if __name__ == '__main__':
    solution = Solution()
    data = [2, 6, 4, 8, 10, 9, 15]
    print(solution.findUnsortedSubarray(data))