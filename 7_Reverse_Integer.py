# -*- coding: utf-8 -*-
"""
# @Time    : 2017/9/22 下午3:31
# @Author  : zhanzecheng
# @File    : 7_Reverse_Integer.py
# @Software: PyCharm
"""


'''
其实利用python中自带的[::-1]操作就可以完成逆序
'''
class Solution(object):
    def reverse(self, x):
        s = cmp(x, 0)
        r = int('s*x'[::-1])
        return s * r * ( r < 2 ** 31)


