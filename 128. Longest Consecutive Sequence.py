"""

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 



"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        if len(nums)==0:
            return 0
        count=1
        series=[]
        for i in range(len (nums)-1):
            if nums [i]+1==nums [i + 1] :
                count+=1
            elif nums [i]==nums [i + 1] :
                continue
            else:
                series.append(count)
                count=1
        series.append(count)
        return max(series)





"""




Basic way to handle sequence 



"""
