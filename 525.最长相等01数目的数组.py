# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/23 下午2:13
# @Author  : zhanzecheng
# @File    : 525.最长相等01数目的数组.py
# @Software: PyCharm
"""

# 这一题的思路真的很巧妙
# 没错，这一题是使用平衡的方法来做的
class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        count = 0
        dic = {0: -1}
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                count -= 1
            if count not in dic:
                dic[count] = i
            else:
                max_len = max(max_len, i - dic[count])
        return max_len