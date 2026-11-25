"""


You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

 







My approach for now was to create a hashtable n find the values
"""



class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hashtable=[0]*(len(grid)*len(grid)+1)
        double=0
        miss=0
        for i in grid:
            for j in i:
                if hashtable[j]!=0:
                    double=j
                else: hashtable[j]=j
        for i in range(1,len(grid)*len(grid)+1):
            if hashtable[i]==0:
                miss=i
                break

        return [double,miss]
                
                







