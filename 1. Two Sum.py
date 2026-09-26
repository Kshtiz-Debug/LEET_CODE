"""


Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



code:

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                if nums[i]+nums[j]==target:
                    return [i,j] 




"""


Well that one is like the brute force approach for this problem , but we can very much optimize this problem ....
Think abt it ... two integers whose sum should be equals to the target .... now this looks like something we have seen in some problems 


Two pointers ...
we have to use two pointers to track the indicies n tht can be done in just one for loop 
with time complexity only O(n) n space as O(1).




"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a=0
        b=len(numbers)-1
        while(a<b):
            if numbers[a]+numbers[b]==target:
                return [a+1,b+1]
            elif numbers[a]+numbers[b] > target:
                b=b-1
            elif numbers[a]+numbers[b] < target:
                a=a+1
        return -1






"""


Well cool 
but will it work on this problem 
not really 
cozzż
the list is not sorted in all cases
so if the list is not sorted then in that case we cant use two pointers

So we have to use HASHMAP now to deal with this 




"""



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x={}
        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in x:
                return [x[needed],i]


            x[nums[i]]= i 
            



"""


This is the hashmap approach 
if the list is not sorted then we can use this 




Hence 



Two pointers - When list is sorted
HashMap - When not sorted 


"""
