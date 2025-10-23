import numpy as np
import math as m

# Mode of Product
mode = "cross"

# Vectors
v1 = np.array([-4, 6 ,7 ])
v2 = np.array([1, -4 , 2 ])
result = 0

def dot_product(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

def cross_product(v1, v2):
    cvx = v1[1]*v2[2] - v1[2]*v2[1]
    cvy = v1[2]*v2[0] - v1[0]*v2[2]
    cvz = v1[0]*v2[1] - v1[1]*v2[0]
    return [cvx, cvy, cvz]
    
if mode == "cross":
    # Calculate the Cross Product
    print(cross_product(v1, v2))
    print(np.cross(v1, v2))
elif mode == "dot":
    # Calculate the Dot Product
    print(dot_product(v1, v2))