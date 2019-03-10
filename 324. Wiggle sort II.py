# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/23 上午10:00
# @Author  : zhanzecheng
# @File    : 324. Wiggle sort II.py
# @Software: PyCharm
"""

# 这题好难， 很懵逼

def wiggleSort( nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    nums.sort()

    half = len(nums[::2]) - 1
    print(nums)
    print(nums[half::-1])
    print(nums[:half:-1])
    nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]
if __name__ == '__main__':
    data =  [1, 5,2, 3, 6, 4]
    wiggleSort(data)
    print(data)