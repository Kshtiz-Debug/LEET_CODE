"""


You are given an integer array nums.

In one move, you may increase the value of any single element nums[i] by 1.

Return the minimum total number of moves required so that all elements in nums become equal.



 """


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)
        count=0
        for i in range(len(nums)):
            if nums[i]<m:
                count += (m-nums[i])
        return count




