# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 07:56:10 2019

@author: daryl
"""

import networkx as nx
from random import randint, random, choice, shuffle
import matplotlib.pyplot as plt

n = 100#grid size
m = 100#grid size
k = 1000# number of walkers


grid = nx.grid_graph([n,m])
 
unassigned = list(grid.nodes())

walkers=[]

cdict={x:0 for x in grid.nodes()}


for i in range(k):
    walkers.append(choice(unassigned))
    unassigned.remove(walkers[-1])
    cdict[walkers[-1]]=i+1
    
plt.figure()
nx.draw(grid,pos= {x:x for x in grid.nodes()},node_color=[cdict[x] for x in grid.nodes()],node_size=600,cmap='tab20')#cmap=plt.cm.jet,label=True)
plt.title("Initial Walkers")


move = 0

while unassigned:
    order = list(range(k))
    shuffle(order)
	
    for i in order:
        old=walkers[i]
        #print(old)
        walkers[i]=choice(list(grid.neighbors(walkers[i])))
        #print(walkers[i])
        if walkers[i] in unassigned:
            unassigned.remove(walkers[i])
            cdict[walkers[i]]=i+1
            grid = nx.contracted_nodes(grid, walkers[i], old, self_loops=False)
        else:
            walkers[i]=old
    #plt.figure()
    #nx.draw(grid,pos= {x:x for x in grid.nodes()},node_color=[cdict[x] for x in grid.nodes()],node_size=600,cmap='tab20')#cmap=plt.cm.jet,label=True)

            
plt.figure()
nx.draw(grid,pos= {x:x for x in grid.nodes()},node_color=['r' for x in grid.nodes()],label=True)
plt.title("Dual Graph")

grid2 = nx.grid_graph([n,m])
plt.figure()
nx.draw(grid2,pos= {x:x for x in grid2.nodes()},node_color=[cdict[x] for x in grid2.nodes()],node_size=400,cmap='tab20')#cmap=plt.cm.jet,label=True)
plt.title("Full Partition")


        
