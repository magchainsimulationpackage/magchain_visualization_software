# --------------------------------------------------------------------------------
# Description: Visualization of 'trajectoryCG.xyz' generated by MagChain
# Input: trajectoryCG.xyz
# Last modified by: Carles, 20/12/2011
# 
# VPython script to be executed by VIDLE for VPython. Documentation on VPython
# can be found at:
#       http://vpython.org/contents/doc.html
# and it can be downloaded:
#       Linux: http://vpython.org/contents/download_linux.html
#       Windows: http://vpython.org/contents/download_windows.html
#       Mac: http://vpython.org/contents/download_mac.html
# --------------------------------------------------------------------------------

import sys
from visual import *

f = open('trajectoryCG.xyz','r')
f1 = open('logfile.log', 'w')
line = f.readline()
sysprops = line.split()
Numparts = int(sysprops[0])
line = f.readline()
sysprops = line.split()
boxz = float(sysprops[0])
boxx = float(sysprops[1])
boxy = float(sysprops[2])

# Creating simulation box
win = 500
gray = (0.7,0.7,0.7)
scene = display(title="Aggregation", width=win, height=win, x= 0, z=0, center=(boxx/2.,boxy/2.,boxz/2.), background = (0.1,0.1,0.1))
zaxis = curve(pos=[(0,0,0), (boxx,0,0)], color=gray)
xaxis = curve(pos=[(0,0,0), (0,boxy,0)], color=gray)
yaxis = curve(pos=[(0,0,0), (0,0,boxz)], color=gray)
zaxis2 = curve(pos=[(boxx,boxy,boxz), (0,boxy,boxz), (0,0,boxz), (boxx,0,boxz)], color=gray)
xaxis2 = curve(pos=[(boxx,boxy,boxz), (boxx,0,boxz), (boxx,0,0), (boxx,boxy,0)], color=gray)
yaxis2 = curve(pos=[(boxx,boxy,boxz), (boxx,boxy,0), (0,boxy,0), (0,boxy,boxz)], color=gray)

arrow(pos=vector(float(boxx)/10.0,float(boxy)/10.0,float(boxz)/10.0), axis=vector(float(boxy)/20.0,0,0), shaftwidth = 0.5, color=color.red)
text(text='y', pos = vector(float(boxx)/10.0+float(boxy)/20.0,float(boxy)/10.0,float(boxz)/10.0), axis=vector(1,0,0), height=float(boxy)/50.0, color=color.white)
arrow(pos=vector(float(boxx)/10.0,float(boxy)/10.0,float(boxz)/10.0), axis=vector(0,float(boxy)/20.0,0), shaftwidth = 0.5, color=color.green)
text(text='z', pos = vector(float(boxx)/10.0,float(boxy)/10.0+float(boxy)/20.0,float(boxz)/10.0), axis=vector(0,1,0), height=float(boxy)/50.0,color=color.white)
arrow(pos=vector(float(boxx)/10.0,float(boxy)/10.0,float(boxz)/10.0), axis=vector(0,0,float(boxy)/20.0), shaftwidth = 0.5, color=color.blue)
text(text='x', pos = vector(float(boxx)/10.0,float(boxy)/10.0,float(boxz)/10.0+float(boxy)/20.0), axis=vector(0,0,0.5), height=float(boxy)/50.0, color=color.white)

colors = [color.red, color.green, color.blue, color.yellow, color.cyan, color.magenta]
aggregate = []
nameaggsold = [0]*Numparts

Numparts0 = Numparts
x = [0.]*Numparts
y = [0.]*Numparts
z = [0.]*Numparts
length = [0.]*Numparts
radius = [0.]*Numparts
kk = 0.
dname = {}
## Initialization:
for n in range(Numparts):
	line = f.readline()
	aggprop = line.split()
	aggname = int(aggprop[0])
	dname[aggname]=n
	nameaggsold[n] = aggname
	aggz = float(aggprop[1])
	aggx = float(aggprop[2])
	aggy = float(aggprop[3])
	agglength = float(aggprop[4])
	aggradius = float(aggprop[5])
	aggregate = aggregate + [ellipsoid(pos=vector(aggx,aggy,aggz), length = aggradius, height = aggradius, width = agglength,up=(0,0,1), color=color.blue)]
        
while True:
	line = f.readline()
	if not line:break
	prop = line.split()
	Numparts = int(prop[0])
	line = f.readline()
	nameaggs = [0]*Numparts
	rate(50)
	kk = kk + 1
	for n in range(Numparts):
		line = f.readline()
		aggprop = line.split()
		aggname = int(aggprop[0])
		nameaggs[n] = aggname
		z[dname[aggname]] = float(aggprop[1])
		x[dname[aggname]] = float(aggprop[2])
		y[dname[aggname]] = float(aggprop[3])
		length[dname[aggname]] = float(aggprop[4])
		radius[dname[aggname]] = float(aggprop[5])
		nameaggsold.remove(aggname)
		

	for n in range(Numparts0):
		aggregate[n].pos = (x[n],y[n],z[n])
		aggregate[n].length = radius[n]
		aggregate[n].height = radius[n]
		aggregate[n].width = length[n]
		if length[n] < 5:
			aggregate[n].color = color.blue
		elif length[n] < 10:
			aggregate[n].color = color.green
		elif length[n] < 15:
			aggregate[n].color = color.yellow
		if length[n] > 15:
			aggregate[n].color = color.white
	for n in range(len(nameaggsold)):
		aggregate[dname[nameaggsold[n]]].visible = False
	nameaggsold = nameaggs
                
			
		
f.close()
f1.close()
