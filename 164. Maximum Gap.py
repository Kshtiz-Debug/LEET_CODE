"""

Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.



 """


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums=sorted(nums)
        m=0
        for i in range(len(nums)-1):
            if (nums[i+1]-nums[i])>m:
                m=(nums[i+1]-nums[i])
        return m

