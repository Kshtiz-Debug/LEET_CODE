

"""

You are given a positive integer array sides of length 3.

Determine if there exists a triangle with positive area whose three side lengths are given by the elements of sides.

If such a triangle exists, return an array of three floating-point numbers representing its internal angles (in degrees), sorted in non-decreasing order. Otherwise, return an empty array.

Answers within 10-5 of the actual answer will be accepted.

Note: Please do not copy the description during the contest to maintain the integrity of your submissions.

"""


""" code """


import math
class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        if sides[0]+sides[1]>sides[2] and sides[1]+sides[2]>sides[0] and sides[0]+sides[2]>sides[1]:
            a=math.acos(((sides[1]*sides[1])+(sides[2]*sides[2])-(sides[0]*sides[0]))/(2*sides[1]*sides[2]))
            b=math.acos(((sides[0]*sides[0])+(sides[2]*sides[2])-(sides[1]*sides[1]))/(2*sides[0]*sides[2]))
            c=math.acos(((sides[1]*sides[1])+(sides[0]*sides[0])-(sides[2]*sides[2]))/(2*sides[1]*sides[0]))
            M=[math.degrees(a),math.degrees(b),math.degrees(c)]
            return sorted(M)
        return []



"""


So first we r using the concept of LAW OF COSINES


usinng acos() we r getting the values of the angles
yuppp ....
and just use math.degrees() to convert the default radians to degrees


"""
