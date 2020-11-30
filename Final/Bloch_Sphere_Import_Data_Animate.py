##Adam Altenhof
##https://github.com/adamaltenhof/FSU_Programming.git
##Program to animate time-depedent nuclear spin polarization on a 3D Bloch sphere.
##Note: need to install ffmpeg for imageio to run this
##I use anaconda/pip so that is done via: pip install imageio-ffmpeg
from qutip import *
from scipy import *
from pylab import *
import matplotlib as mpl
from matplotlib import cm
import pandas
import numpy as np
import imageio

#The input data is NMR spin polarization from a numerical simulation software
#called SIMPSON. The data are in .fid files - I programmed the simulation to have the
#various output names - mainly depending on the x, y, or z coordinate of 
#polarization. There are two columns for the data - one for the real part
#and one for the imaginary part of the data, and the precision of the output
#varies. Instead of parsing lines I found it easier to use pandas and treat
#the data as a table when reading it in, then convert to numpy array.
def readFID(name):
    x = np.array(pandas.read_csv(name + '_1.fid', sep=' ',skiprows=[0,1,2,3], skipfooter=1,
                    engine='python',index_col=1))
    y = np.array(pandas.read_csv(name + '_2.fid', sep=' ',skiprows=[0,1,2,3], skipfooter=1,
                    engine='python',index_col=1))
    z = np.array(pandas.read_csv(name + '_3.fid', sep=' ',skiprows=[0,1,2,3], skipfooter=1,
                    engine='python',index_col=1))
    return x,y,z

#Two things are done here: 1) Creating the Bloch sphere object in qutip and 
#supplying the various options for its appearance.
#2) Using the imageio writer to render an mp4 using every iteration 
#of a Bloch sphere that is created.
#Note 'runningpoint' - this works by creating progressive images that 
#include more of the data on each iteration - so it actually takes longer
#to generate individual spheres as the loop progresses.
#Also note I had to mess around with the colormap from matplotlib 
#in order to have it change colour dynamically for different polarity.
def animateBloch(name,x,y,z):
    writer = imageio.get_writer(name+'.mp4',mode='I', fps=60)
    filename='temp_file.png'
    b=Bloch() ##This is the Bloch sphere object
    b.vector_color = ['k']
    b.view = [-150,30]
    length=len(x)
    nrm = mpl.colors.Normalize(0,length) #normalize colors to the length of data
    colors = list(cm.cool_r(nrm(range(length)))) #can adjust colormap (cm)
    b.point_marker = ['o']
    b.zlabel = ['z' ,'']
    for n in range(len(x)):
        b.clear()
        b.point_color = [colors[-(n+1):]] #use some n-amount of the colormap
        point=[x[n],y[n],z[n]]
        runningpoint = [x[:n+1],y[:n+1],z[:n+1]] 
        b.add_vectors([point]) #generates single vector
        b.add_points(runningpoint) #generates all the running-points
        b.save(filename)
        writer.append_data(imageio.imread(filename)) #renders each frame/sphere into mp4
    writer.close()
    
#Straightforward html page - kept it simple.
def writeHTML(sitename = 'Altenhof_Final_Project.html'):
    f = open(sitename,'w')
    f.write('<!DOCTTYPE html>\n<html>\n<head>\n<title>Adam Altenhof Final Project</title>\n')
    f.write('<style>\n h1 {\n color:blue;\n font-family:Arial;\n }\n')
    f.write('body {\n background: black;\n color: white;\n }\n</style>\n</head>\n')
    
    f.write('<body>\n <h1>Direct Excitation WURST Inversion</h1>\n')
    f.write('<video width="360" height="360" controls><source src="DE_BRAIN_np_2000.mp4" type="video/mp4"></video>')
    
    f.write('<body>\n <h1>BRAIN-CP High-to-low Frequency Sweep</h1>\n')
    f.write('<video width="360" height="360" controls><source src="BCP_BRAIN_np_2000.mp4" type="video/mp4"></video>')
    
    f.write('<body>\n <h1>BRAIN-CP Low-to-High Frequency Sweep</h1>\n')
    f.write('<video width="360" height="360" controls><source src="BCP_BRAINr_np_2000.mp4" type="video/mp4"></video>')
    
    f.write('</body>\n </html>')

    f.close()
    
##Execute for three simulations
##This takes a long time to run / render all the videos (ca. 40 - 50 min)
name = 'DE_BRAIN_np_2000'
x,y,z = readFID(name)
animateBloch(name,x,y,z)

name = 'BCP_BRAIN_np_2000'
x,y,z = readFID(name)
animateBloch(name,x,y,z)

name = 'BCP_BRAINr_np_2000'
x,y,z = readFID(name)
animateBloch(name,x,y,z)

writeHTML()
print('Finished!')