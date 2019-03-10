# -*- coding: utf-8 -*-
"""
# @Time    : 2019/3/10 下午2:16
# @Author  : zhanzecheng
# @File    : 521.continuous_subarray_sum.py
# @Software: PyCharm
"""

# if pre_sum % k in the dict, then [i, j] is the answer. record every pre_sum % k in the dict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        if len(nums) <= 1:
            return False
        if k == 0:
            for i in range(len(nums) - 1):
                if nums[i] == nums[i + 1] == 0:
                    return True
                return False
        presum, dic = 0, {0: 1}
        for i in range(len(nums)):
            presum += nums[i]
            if presum % k in dic and (nums[0] == nums[1] == k or nums[i] != k):
                return True
            else:
                dic[presum % k] = 1
        return False