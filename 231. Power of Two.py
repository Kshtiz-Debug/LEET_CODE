"""


Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 



"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x=0
        while(True):
            if 2**x==n:
                return True
            else:
                if 2**x>n:
                    return False
                else:
                    x=x+1

              
