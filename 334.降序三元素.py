# 这一题好像就是单纯的考逻辑

class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if not nums:
            return False

        stack1 = None
        stack2 = None

        for i in range(len(nums)):
            if stack1 == None:
                stack1 = nums[i]
                continue

            if stack2 == None:
                if nums[i] > stack1:
                    stack2 = stack1
                    stack1 = nums[i]
                else:
                    stack1 = nums[i]
                continue
            if nums[i] > stack1:
                return True

            if nums[i] > stack2 and nums[i] < stack1:
                stack1 = nums[i]
            if nums[i] < stack2:
                stack2 = nums[i]
        return False