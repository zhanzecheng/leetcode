# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/14 上午10:14
# @Author  : zhanzecheng
# @File    : 456.132模式.py
# @Software: PyCharm
"""


class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        s3 = -123123
        st = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < s3:
                return True
            while len(st) != 0 and nums[i] > st[-1]:
                s3 = st[-1]
                st.pop()

            st.append(nums[i])
        return False

