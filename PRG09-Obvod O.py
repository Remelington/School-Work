import math

def obvod (r):
    return round (2*math.pi*r, 3)
    
print (obvod(r+1) - obvod(r))
r=6378
