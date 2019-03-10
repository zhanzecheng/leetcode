# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/28 下午7:49
# @Author  : zhanzecheng
# @File    : 81.在旋转列表中招数.py
# @Software: PyCharm
"""


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        l = 0
        h = len(nums) - 1
        while l < h:
            mid = (l + h) // 2
            if nums[mid] > nums[h]:
                l = mid + 1
            else:
                h = mid
        print(l)
        nums[:(len(nums)-l)],nums[(len(nums) - 1):] = nums[l:], nums[:l]
        return nums
if __name__ == '__main__':
    solution = Solution()
    # data = [4, 5, 1, 2, 3 ]

    data = [2,2,2,0,2,2]
    print(solution.search(data, 2))