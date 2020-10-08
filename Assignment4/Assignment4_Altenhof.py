# -*- coding: utf-8 -*-
##Adam Altenhof
##https://github.com/adamaltenhof/FSU_Programming.git
##Assignment4_Altenhof.py located under Assignment4 folder in my github repository
f=open("2FA9noend.pdb")
g=open('Out_Altenhof.pdb','w')
lines = f.readlines()
l=[None]*len(lines) #preallocate list size, this will be the list of lists
j=0
s="{}\n"
for line in lines:
    l[j]=line.split()
    g.write(s.format(l[j]))
    j+=1
f.close()
g.close()
print('All Done!')