"""




Given an integer array of size n, find all elements that appear more than ⌊n / 3⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]


"""




class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count = {}
        result = []

        for i in nums:
            count[i] = count.get(i, 0) + 1

        for i in count:
            if count[i] > len(nums) // 3:
                result.append(i)

        return result





"""


this is hashmap method .... quite optimal but not completely ...

Boyer-Moore Voting Algorithm


this algo is the most optimal for this problem 


"""


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        l = []

        for i in nums:
            if nums.count(i) > len(nums) // 3:
                if i not in l:
                    l.append(i)

        return l





"""


This is like the brute force approach for this type of question 



"""
