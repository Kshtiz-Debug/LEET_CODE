"""


You are given an array of integers nums.

Choose two different indices i and j of that array.

Return the maximum value of (nums[i] - 1) * (nums[j] - 1).



 """


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        out=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if ((nums[i]-1)*(nums[j]-1))>out:
                    out=((nums[i]-1)*(nums[j]-1))
        return out



"""


this will be the brute force approach of the problem 
with this we can even do it in multiple other ways 
now lets see how to optimize it a lil

"""




class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)



"""


This is like the most basic thinking 
tht if we want maximum result 
then it will only come if we take the maximum elements 
which can be easily done by sorting it 
So just make sure its sorted 
n then take the last two elements
or shld we say the maximum elements after sorting as they will give the maximum product



"""


