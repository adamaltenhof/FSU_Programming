# -*- coding: utf-8 -*-
#https://github.com/adamaltenhof/FSU_Programming.git
#Under folder /Assignment3

import math
import numpy as np

x = input("Supply three points of the form x1,y1,x2,y2,... : ")
x = np.fromstring(x, dtype=float, sep=',')
#Point A
x1=x[0]
y1=x[1]
#Point B
x2=x[2]
y2=x[3]
#Point C
x3=x[4]
y3=x[5]
#Side lengths
c = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )
a = math.sqrt( (x2-x3)**2 + (y2-y3)**2 )
b = math.sqrt( (x1-x3)**2 + (y1-y3)**2 )
#angles, convention is alpha is opposite side length a; beta opposite b; and gamma opposite c
gamma = math.degrees(math.acos( (a**2+b**2-c**2)/(2*a*b) ))
alpha = math.degrees(math.acos( (b**2+c**2-a**2)/(2*b*c) ))
beta = math.degrees(math.acos( (a**2+c**2-b**2)/(2*a*c) ))

print('alpha, beta, and gamma in degrees = ')
print(round(alpha,2),round(beta,2),round(gamma,2))