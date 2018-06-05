# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/4 上午9:41
# @Author  : zhanzecheng
# @File    : 31.下一个排列.py
# @Software: PyCharm
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        k = -1
        length = len(nums)
        for i in range(length -2, -1, -1):
            # 找到最后的不是降序排列的数
            if nums[i] < nums[i + 1]:
                k = i
                break
        # 如果找不到说明已经到头了
        if k == -1:
            nums[:] = nums[:][::-1]
            return
        # 找到最后的比这个枢纽要大的数
        for i in range(length -1, k, -1):
            if nums[i] > nums[k]:
                l = i
                break
        # 交换
        nums[k], nums[l] = nums[l], nums[k]
        # 逆序
        nums[k+1:] = nums[k+1:][::-1]

if __name__ == '__main__':
    solution = Solution()
    data = [1,2,3]
    solution.nextPermutation(data)
    print(data)