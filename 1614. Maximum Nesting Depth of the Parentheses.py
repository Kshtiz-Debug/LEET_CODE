"""


Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.



 """


class Solution:
    def maxDepth(self, s: str) -> int:
        top=0
        maximum=0
        for i in s:
            if i=='(':
                top=top+1
            elif i==')':
                top=top-1
            

            if maximum<top:
                maximum=top

        return maximum






"""


Usage of basic stack concept .... 

If u find opening parenthesis then add to the stack , n if find closing parenthesis then pop from the stack 
n keep updating maximum value , just in our case we r not doing tht .... instead we are just having a variable top keeping the value
works same as a stack just doesnt store the values coz we dont care abt em.... 😔 sad  ....


"""
