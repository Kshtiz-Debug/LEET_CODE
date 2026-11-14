"""



Given a string s, return the longest palindromic substring in s.




 """


class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        palindrome=""
        maximum=0
        
        for i in range(len(s)):
            left=i
            right=i
            count=0
            for j in range(len(s)):
                if s[left]==s[right]:
                    count+=1
                    if count>maximum:
                        maximum=count
                        palindrome=s[left:right+1]
                    left=left-1
                    right=right+1
                    if left<0 or right>len(s)-1:
                        break
                else:
                    if count>maximum:
                        maximum=count
                        palindrome=s[left:right+1]
                    break
        for i in range(len(s)-1):
            left=i
            right=i+1
            count=1
            for j in range(len(s)):
                if s[left]==s[right]:
                    count+=1
                    if count>maximum:
                        maximum=count
                        palindrome=s[left:right+1]
                    left=left-1
                    right=right+1
                    if left<0 or right>len(s)-1:
                        break
                else:
                    if count>maximum:
                        maximum=count
                        palindrome=s[left:right+1]
                    break
            
        
        return palindrome





"""



We hve two set of for loops each having nested for loop .... to handle both odd length n even length test cases 



"""


