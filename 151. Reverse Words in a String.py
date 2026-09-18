"""


A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.




"""




class Solution:
    def reverseWords(self, s: str) -> str:
        x=s.split()
        y=len(x)
        l=""
        for i in range(y):
            l=l+ " " +x[y-i-1]
        return l.strip()







"""


from this i learnt wht is the difference between split n strip ...  


so split is used to split the character into multiple substrings .... its like it breaks the string in multiple parts .... with that it also stores all the splitted part of the string inside a list 
while strip removes any trailing whitespace characters from the string 



"""
