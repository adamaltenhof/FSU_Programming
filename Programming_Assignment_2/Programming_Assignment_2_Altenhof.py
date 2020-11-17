# -*- coding: utf-8 -*-
## Adam Altenhof
## https://github.com/adamaltenhof/FSU_Programming.git
## Programming_Assignment_2_Altenhof.py located under Programming_Assignment_2 folder in my github repository
import numpy as np
import matplotlib.pyplot as plt

f=open("superose6_50.asc")
lines = f.readlines()
l = []
for line in lines:
    l.append(line.split()) #extract the data from the file
f.close()

a = np.array(l[3:883] , dtype='float64') #turn the actual chromatogram data into a numpy array with float64 data type
g = np.gradient(a[:,1],1) #calc the gradient, where this is 0 corresponds to a peak maximum

base = 1 #adjust to find more or less peaks - basically a threshold; 
#seems we are told where the first one ought to be so I pick a value based on that fact
#0.1 or 0.2 could find roughly all the peaks

maxima = np.where( np.diff(np.sign(g[:] + base)) == -2)
#sign says if an entry is pos or neg or 0, then diff calcs the difference between consecutive pairs of entries
#then finds where the diff is -2 (i.e., -1 - 1 ) which would be a zero-point in the gradient
#Appears to miss maxima by +/-1 so add a fix for that:
k=0
for j in maxima[0]:
    if a[j,1] < a[j+1,1]:
        maxima[0][k] = j+1
    elif a[j,1] < a[j-1,1]:
        maxima[0][k] = j-1
    k+=1
    
#Non-zero entries that aren't peaks are the boundaries (i.e., other changes from 0)
#modify what is "zero" in the spectrum by adding or subtracting a baseline amount - since the baseline is rarely exactly 0
#Use the +/- base to get two boundaries per peak 
b1 = np.where( (np.diff(np.sign(g + base)) != 0) & (np.diff(np.sign(g + base)) != -2) )
b2 = np.where( (np.diff(np.sign(g - base)) != 0) & (np.diff(np.sign(g - base)) != -2) )
b = np.sort(np.append(b1 ,b2))
if len(b) > 2*len(maxima):#this deletes another boundary point outside of our peaks of interest in this example
    b = np.delete(b,0)

#plot the spectrum, with the peak maxima, and peak boundaries
plt.plot(a[:,0],a[:,1],'b',label='Spectrum')
plt.plot(a[maxima,0][0],a[maxima,1][0], 'r*',label='Peaks')
plt.plot(a[b,0],a[b,1], 'k.',label='Peak Boundaries')
plt.legend()
plt.show()

print('There are ',len(maxima[0]), 'peaks:\n')
for i in range(len(a[maxima,0][0])):
    print('Peak ',i+1,'at time',round(a[maxima,0][0][i],2),'with maximum absorbance of',round(a[maxima,1][0][i],2) ,'\n')