# -*- coding: utf-8 -*-
## Adam Altenhof
## https://github.com/adamaltenhof/FSU_Programming.git
## Programming_Assignment_1_Altenhof.py located under Programming_Assignment_1 folder in my github repository
import numpy as np
f=open("2FA9noend.pdb")
g=open('Out_Altenhof.pdb','w')
lines = f.readlines()

l = [None]*len(lines)     #preallocate everything
A = [None]*len(lines)
x  = np.zeros(len(lines))
xm = np.zeros(len(lines))
y  = np.zeros(len(lines))
ym = np.zeros(len(lines))
z  = np.zeros(len(lines))
zm = np.zeros(len(lines))
M  = np.zeros(len(lines))
j=0
for line in lines:
    l[j] = line.split()
    l[j][1] = int(l[j][1])
    l[j][5] = int(l[j][5])
    l[j][9] = float(l[j][9])
    l[j][10] = float(l[j][10])
    x[j] = float(l[j][6])
    y[j] = float(l[j][7])
    z[j] = float(l[j][8])
    A[j] = l[j][11]
    if A[j] == 'C':
        M[j] = 12.0
    if A[j] == 'N':
        M[j] = 14.0
    if A[j] == 'O':
        M[j] = 16.0
    if A[j] == 'S':
        M[j] = 32.0
    xm[j] = x[j]*M[j]
    ym[j] = y[j]*M[j]
    zm[j] = z[j]*M[j]
    j+=1

r = int(input("Enter 0 to center pdb to geometric center, or enter 1 for center of mass: "))

k = float(len(lines))
if r == 0:
    xc = sum(x)/k  ##Calc based on geometric center, or 'centroid' formula
    yc = sum(y)/k
    zc = sum(z)/k
else:   ##r = 1 executes the else statement, slightly more robust to leave as else in case input is anything else
    xc = sum(xm)/sum(M)
    yc = sum(ym)/sum(M)
    zc = sum(zm)/sum(M)

s="{0:<6s}{1:>5d}  {2:<4s}{3:1s} {4:2s}{5:>3d}{6:12.3f}{7:8.3f}{8:8.3f}{9:>6.2f}{10:>6.2f}{11:>12s}\n"
for i in range(len(lines)):
    l[i][6] = x[i] - xc
    l[i][7] = y[i] - yc
    l[i][8] = z[i] - zc
    g.write(s.format(l[i][0],l[i][1],l[i][2],l[i][3],l[i][4],l[i][5], 
                     l[i][6],l[i][7],l[i][8],l[i][9],l[i][10],l[i][11]))
    
f.close()
g.close()
print('All Done!')