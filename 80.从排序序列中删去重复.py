# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/29 上午9:34
# @Author  : zhanzecheng
# @File    : 80.从排序序列中删去重复.py
# @Software: PyCharm
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        if length <= 2:
            return length
        pre = nums[-1]
        count = 1
        for i in range(length - 2, -1, -1):
            if nums[i] == pre:
                count += 1
            else:
                if count > 2:
                    length = length - count + 2
                count = 1
            pre = nums[i]
            if count > 2:
                del nums[i]


        if count > 2:
            length = length - count + 2
        return length

if __name__ == '__main__':
    solution = Solution()
    data = [1,1,1,2,2,3]
    print(solution.removeDuplicates(data))