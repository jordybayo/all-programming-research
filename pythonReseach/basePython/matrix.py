#coding:utf-8

import numpy as np
import math
from copy import deepcopy
from math import pow


#transpose of matrix

mat = np.arange(12).reshape(3,4)
print(mat)
print("le transpose de matrix est\n",mat.transpose())


#nverse of matrix
m = np.array([[3,4],[2,16]] ,dtype=float)
b = deepcopy(m)
print("la valeur initiale de m\n\n\n\nB-1",m)

for x in np.nditer(m,op_flags=['readwrite']):
    x[...] = 1/x
print("l'invrse de m est : \n\n",m)
print ("la multiplication \n",m*b)