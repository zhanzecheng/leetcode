# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/10 上午11:49
# @Author  : zhanzecheng
# @File    : 300.最长增序列.py
# @Software: PyCharm
"""
# 用一个dp数组来保存值
# 用二分查找来加快时间
# TODO: 这里的二分查找是有等号的！！！！！
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
                continue
            else:
                # 这里要使用查找的方式来查找合适点
                # 那么其实是o(n^2)
                # 如果使用二叉查找时间复杂度可以下降o(nlog(n))
                flag = False
                # 这里使用二分查找来进行改进
                l , h = 0, len(dp) - 1
                while l < h:
                    mid = (l + h) // 2
                    print(l, h, mid)
                    if dp[mid] == nums[i]:
                        flag = True
                        break
                    elif dp[mid] > nums[i]:
                        h = mid
                    else:
                        l = mid + 1
                if flag:
                    continue
                dp[l] = nums[i]
        return len(dp)
if __name__ == '__main__':
    solution = Solution()
    data = [10,9,2,5,3,7,101,18]
    solution.lengthOfLIS(data)
# 这个是另外一种解法
"""

class Solution:

    def lengthOfLIS(self, nums):
        if nums == []:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            dp[i] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
        
"""