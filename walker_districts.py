# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 07:56:10 2019

@author: daryl
"""

import networkx as nx
from random import randint, random, choice
import matplotlib.pyplot as plt

n = 10#grid size
m = 10#grid size
k = 8# number of walkers


grid = nx.grid_graph([n,m])
 
unassigned = list(grid.nodes())

walkers=[]

cdict={x:0 for x in grid.nodes()}


for i in range(k):
    walkers.append(choice(unassigned))
    unassigned.remove(walkers[-1])
    cdict[walkers[-1]]=i+1
    
    
nx.draw(grid,pos= {x:x for x in grid.nodes()},node_color=[cdict[x] for x in grid.nodes()],node_size=600,cmap='tab20')#cmap=plt.cm.jet,label=True)



move = 0

while unassigned:
	
    for i in range(k):
        walkers[i]=choice(list(grid.neighbors(walkers[i])))
        if walkers[i] in unassigned:
            unassigned.remove(walkers[i])
            cdict[walkers[i]]=i+1
    #plt.figure()
    #nx.draw(grid,pos= {x:x for x in grid.nodes()},node_color=[cdict[x] for x in grid.nodes()],node_size=600,cmap='tab20')#cmap=plt.cm.jet,label=True)

            
plt.figure()
nx.draw(grid,pos= {x:x for x in grid.nodes()},node_color=[cdict[x] for x in grid.nodes()],node_size=600,cmap='tab20')#cmap=plt.cm.jet,label=True)


        