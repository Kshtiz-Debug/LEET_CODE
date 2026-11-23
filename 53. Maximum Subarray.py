"""


Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

"""




' So the idea is to make a sliding window tht moves across the array n finds the array sum '


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sum = 0
        l = [0] * len(nums)
        for i in range(len(nums)):
            if sum + nums[i] < 0:
                l[i] = nums[i]
                sum = 0
            else:
                sum = sum + nums[i]
                l[i] = sum
        return max(l)




"""



So this makes sure the sum is maximum 



"""
