# -*- coding: utf-8 -*-
"""
# @Time    : 2017/9/21 下午1:40
# @Author  : zhanzecheng
# @File    : 1_Two_Sum.py
# @Software: PyCharm
"""

'''
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i


def stringToIntegerList(input):
    input = input.strip()
    input = input[1:-1]
    return [int(number) for number in input.split(",")]


def integerListToString(nums, len_of_list=None):
    result = ""
    if not len_of_list:
        len_of_list = len(nums)
    for index in range(len_of_list):
        num = nums[index]
        result += str(num) + ", "
    return result[:-2]


import sys


def readlines():
    for line in sys.stdin:
        yield line.strip('\n')


def main():
    lines = readlines()
    while True:
        try:
            line = lines.next()
            nums = stringToIntegerList(line)
            line = lines.next()
            target = int(line)

            ret = Solution().twoSum(nums, target)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()