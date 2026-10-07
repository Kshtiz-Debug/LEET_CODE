"""


Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]



So one approach is ofcourse brute force 
where we will just do using o(n^2) time complexity but there is a better approach to it and that is  ..........


"""



class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        mul=1
        l=[]
        zero =0
        for i in nums:
            if i==0:
                zero +=1
            else:
                mul = mul * i
        
        for i in nums:
            if zero > 1:
                l.append(0)
            elif zero == 1:
                l.append( mul if i==0 else 0)
            else:
                l.append(mul//i)



        return l




"""



So this way we do this problem with much less time complexity 




"""



