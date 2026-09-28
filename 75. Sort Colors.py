"""


You are given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 



"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0=0
        c1=0
        c2=0
        for i in nums:
            if i==0:
                c0+=1
            if i ==1:
                c1+=1
            if i==2:
                c2+=1

        
        for i in range(0,c0):
            nums[i]=0
        for i in range(c0,c0+c1):
            nums[i]=1
        for i in range(c0+c1,c0+c1+c2):
            nums[i]=2
        





"""



This is like the brute force way to solve this type of question by simply counting the number of each n changing its value 
But this can be optimized a lot more than this 

"""
