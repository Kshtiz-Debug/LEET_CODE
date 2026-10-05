"""



Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.




 """


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return nums[j]



"""


The brute force ----  sadly wont give u the answer --- time complexity is not good o(n^2)
So lets try to optimize it 



"""
