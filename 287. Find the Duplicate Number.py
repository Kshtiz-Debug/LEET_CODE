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




now lets think how to change that o(n^2) to something less than that

Well we know tht there are exactly n+1 elements in the array
and they are ordered from 1 to n with one repeated value 


so why dont we use dictionary to get that extra count of 2 


"""




class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        l={}
        for i in nums:
            if i not in l:
                l[i]=1
            else:
                return i



"""


This solution is accepted which is of time complexity of o(n)
but it uses extra space 


Current: Hash Table
Suggested: Two Pointers
/
Floyd's Cycle Finding Algorithm
Key Idea:
Find duplicate in array with constant space using cycle detection or binary search.
Consider:
Can you spot the hidden cycle in the array indices and use two pointers to find the entrance?



Hence we can optimize it more by optimizing the space complexity part 
"""




