# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/11 下午7:26
# @Author  : zhanzecheng
# @File    : 826.最有益的工作划分.py
# @Software: PyCharm
"""
# 这个感觉没啥意义呀

def maxProfitAssignment(difficulty, profit, worker):
    jobs = sorted([a, b] for a, b in zip(difficulty, profit))
    print(jobs)
    res = i = maxp = 0
    for ability in sorted(worker):
        while i < len(jobs) and ability >= jobs[i][0]:
            maxp = max(jobs[i][1], maxp)
            i += 1
        res += maxp
    return res
if __name__ == '__main__':
    difficulty = [68,35,52,47,86]
    profit = [67,17,1,81,3]
    worker = [92,10,85,84,82]
    maxProfitAssignment(difficulty, profit, worker)