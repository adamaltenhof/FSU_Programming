# -*- coding: utf-8 -*-
## Adam Altenhof
## https://github.com/adamaltenhof/FSU_Programming.git
## Assignment_5_Altenhof.py located under Assignment_5 folder in my github repository
def readpdb(name):
    """Supply the name of the pdb file you want to import as an argument. This function will return a list of every line in the file and a list of the x, y, and z coordinates."""
    f=open(name)
    lines = f.readlines()
    l=[]
    x=[]
    y=[]
    z=[]
    coord=[]
    j=0
    for line in lines:
        l.append(line.split())
        if l[j] == ['END']:  #Second pdb has END on the last line
            l[j] = None
        else:
            l[j][1] = int(l[j][1])
            l[j][5] = int(l[j][5])
            l[j][9] = float(l[j][9])
            l[j][10] = float(l[j][10])
            x.append(float(l[j][6]))
            y.append(float(l[j][7]))
            z.append(float(l[j][8]))
            j+=1
    coord = [x,y,z] #Put everything in coord so the input for RMSD is less cumbersome
    f.close()
    return l,coord

def RMSD(coord1,coord2):
    """Calculate root mean square deviation (RMSD) bewtween two 3D cartesean coordiante systems"""
    import math as m
    #constructs a list for all the difference of squares and then does the normalization, sum, and sqrt on the lsit
    t=[]
    for i in range(len(coord1[0])):
        t.append( (coord1[0][i] - coord2[0][i])**2 + (coord1[1][i] - coord2[1][i])**2 + (coord1[2][i] - coord2[2][i])**2 )
    rmsd = m.sqrt(sum(t) / len(t))
    return rmsd

#Execute the read function for each file and then use the RMSD function for the two coord lists
l1,coord1 = readpdb("2FA9noend.pdb")
l2,coord2 = readpdb("2FA9noend2mov.pdb")
rmsd = RMSD(coord1,coord2)

print('Root mean square deviation = ',round(rmsd,3))
print('Finished!')