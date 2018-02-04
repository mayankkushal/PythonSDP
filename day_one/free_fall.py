'''
Compute speed of an object when it hits the ground after being dropped
'''
from math import sqrt

#Define constant for accelearion due to gravity
GRAVITY = 9.8

#Read the height from which the object is dropped
d = float(input("height from which the object is dropped(in meters): "))

vf = sqrt(2 * GRAVITY *d)

print("It will hit the ground at %.2f m/s" % vf)