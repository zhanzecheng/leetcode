# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/25 上午10:22
# @Author  : zhanzecheng
# @File    : 376.扭捏序列.py
# @Software: PyCharm
"""

# 用一个O(n2)的dp可以做出来

# 另外一种思路是O（n）

# So we can use two arrays up[] and down[] to record the max wiggle sequence length so far at index i.

"""


for(int i = 1 ; i < nums.length; i++){
    if( nums[i] > nums[i-1] ){
        up[i] = down[i-1]+1;
        down[i] = down[i-1];
    }else if( nums[i] < nums[i-1]){
        down[i] = up[i-1]+1;
        up[i] = up[i-1];
    }else{
        down[i] = down[i-1];
        up[i] = up[i-1];
    }
}
        
"""
class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        dp1 = [1] * len(nums)
        dp2 = [1] * len(nums)
        dp1[0] = 1
        dp2[0] = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if dp1[j] % 2 == 0:
                    if nums[i] < nums[j]:
                        dp1[i] = max(dp1[i], dp1[j] + 1)
                    else:
                        dp1[i] = max(dp1[i], dp1[j])
                else:
                    if nums[i] > nums[j]:
                        dp1[i] = max(dp1[i], dp1[j] + 1)
                    else:
                        dp1[i] = max(dp1[i], dp1[j])

                if dp2[j] % 2 != 0:
                    if nums[i] < nums[j]:
                        dp2[i] = max(dp2[i], dp2[j] + 1)
                    else:
                        dp2[i] = max(dp2[i], dp2[j])
                else:
                    if nums[i] > nums[j]:
                        dp2[i] = max(dp2[i], dp2[j] + 1)
                    else:
                        dp2[i] = max(dp2[i], dp2[j])
        return max(max(dp1), max(dp2))