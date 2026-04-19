"""

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.



 """

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x=set(nums1)
        y=set(nums2)
        ret=[]
        for i in x:
            for j in y:
                if i==j:
                    ret.append(i)
        return ret
