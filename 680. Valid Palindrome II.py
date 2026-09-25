"""



Given a string s, return true if the s can be palindrome after deleting at most one character from it.




 """


class Solution:
    def validPalindrome(self, s: str) -> bool:


        y=""


        for i in s:
            if i.isalnum():
                y+=i.lower()


        a=0
        b=len(y)-1
        count=0
        while(a<b):
            if(y[a]==y[b]):
                a+=1
                b-=1
            else:
                count+=1
                l1=y[a+1:b+1]
                l2=y[a:b]

                return l1==l1[::-1] or l2==l2[::-1]
                

            
        if count<2:
            return True
        else:
            return False






