"""






You are given a string moves of length n consisting only of characters 'L', 'R', and '_'. The string represents your movement on a number line starting from the origin 0.

In the ith move, you can choose one of the following directions:

move to the left if moves[i] = 'L' or moves[i] = '_'
move to the right if moves[i] = 'R' or moves[i] = '_'
Return the distance from the origin of the furthest point you can get to after n moves.




"""



class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        r=0
        l=0
        u=0
        for i in moves:
            if i=='R':
                r=r+1
            elif i=='L':
                l=l+1
            else:
                u=u+1

        if l>r:
            return l+u-r
        elif l<r:
            return r+u-l
        else:
            return u
