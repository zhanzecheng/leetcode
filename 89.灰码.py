# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/30 下午10:35
# @Author  : zhanzecheng
# @File    : 89.灰码.py
# @Software: PyCharm
"""


def grayCode(self, n):
    results = [0]
    for i in range(n):
        results += [x + pow(2, i) for x in reversed(results)]
    return results