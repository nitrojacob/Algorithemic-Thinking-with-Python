#!/usr/bin/env python3
#Estimate pi using trial and error

import numpy as np
import time
for res in range(5):
    start = time.time()
    step = 10**(-res)
    inside = 0;
    total = 0;
    for x in np.arange(-1,1,step):
        for y in np.arange(-1,1,step):
            if(x*x+y*y<=1): #Check whether the point is inside the circle
                inside+=1
            total += 1
    pi = 4*inside/total
    duration = time.time()-start
    print(res, pi, duration)

