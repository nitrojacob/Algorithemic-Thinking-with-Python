#!/usr/bin/env python3
#Estimate pi using trial and error

import numpy as np
inside = 0;
total = 0;
for trial in range(1000000000):
    x=np.random.random()
    y=np.random.random()
    if(x*x+y*y<=1): #Check whether the point is inside the circle
        inside+=1
    total += 1
    pi = 4*inside/total
    if(total in [10**x for x in[1,2,3,4,5,6,7,8,9,10] ]):
        print(total, pi)
print(total, pi)

