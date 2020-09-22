# -*- coding: utf-8 -*-
#https://github.com/adamaltenhof/FSU_Programming.git
import math
#import numpy as np

#x = input("Supply three points in Cartesean space: ")

#Point A
x1=1
y1=2
#Point B
x2=3
y2=4
#Point C
x3=4
y3=0
#Side lengths
c = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )
a = math.sqrt( (x2-x3)**2 + (y2-y3)**2 )
b = math.sqrt( (x1-x3)**2 + (y1-y3)**2 )
#angles
gamma = math.degrees(math.acos( (a**2+b**2-c**2)/(2*a*b) ))
alpha = math.degrees(math.acos( (b**2+c**2-a**2)/(2*b*c) ))
beta = math.degrees(math.acos( (a**2+c**2-b**2)/(2*a*c) ))

print('alpha, beta, and gamma in deg = ')
print(round(alpha,2),round(beta,2),round(gamma,2))