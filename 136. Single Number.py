"""



Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.


"""



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l=set(nums)
        d={}
        for i in nums:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        for key,value in d.items():
            if value==1:
                return key

          
