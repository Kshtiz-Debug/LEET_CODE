"""

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 



"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if sorted(s)==sorted(t):
            return True
        else:
            return False





"""


just sort n check if they r same


"""
