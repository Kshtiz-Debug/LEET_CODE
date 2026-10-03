"""


Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret=[]
        x=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j] and j not in x:
                    ret.append(nums1[i])
                    x.append(j)
                    break
        return ret



""" 


this is like the brute force of it 
can be optimized 


"""
