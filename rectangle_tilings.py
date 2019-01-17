# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 13:51:58 2019

@author: daryl
"""

'''do an aggregate method where each knows its
 initial neighbos at each step try to grow the rectangle 
 upwatds or rightwards (or diagonal? - not for now). Rnadom number of growth attempts (0- k). 
 
 When a new collection of nodes is merged contract those edges after checking that it is permissible
 - need to know boundary nodes so you can check the individual +1 are still in the permissible dict
 
 Start with nxn array initialized to all zeros. Set the (0,0) entry  to 1 and check 
 '''
 
import networkx as nx
from random import randint, random
 
n = 5 #grid size
k = 3 # number of possible steps
 
grid = nx.grid_graph([n,n])
 
unassigned = list(grid.nodes())
rectangles = []

while unassigned:
	
	ll=unassigned[0]
	uboundary = [ll]
	rboundary = [ll]
	unassigned.remove(ll)
	
	numr = 0
	numu = 0
	
	
	expands = randint(0,k)
	
	for i in range(expands):
		if random() < .5:
			#move up
			temp = 0 
			for j in uboundary:
				if (j[0],j[1]+1) in unassigned:
					temp +=1
			if temp == len(uboundary):
				numu += 1
			
				for j in range(len(uboundary)):
					
					#grid = nx.contracted_edge(grid, (ll, (uboundary[j][0],uboundary[j][1]+1)), self_loops=False)

					unassigned.remove((uboundary[j][0],uboundary[j][1]+1))
					uboundary[j] = (uboundary[j][0],uboundary[j][1]+1)
					grid = nx.contracted_nodes(grid, ll, (uboundary[j][0],uboundary[j][1]), self_loops=False)


		else:
			#move right
			temp = 0 
			for j in rboundary:
				if (j[0]+1,j[1]) in unassigned:
					temp += 1
			if temp == len(rboundary):
				numr += 1
			
				for j in range(len(rboundary)):
					unassigned.remove((rboundary[j][0]+1,rboundary[j][1]))
					rboundary[j] = (rboundary[j][0]+1,rboundary[j][1])
					
					#grid = nx.contracted_edge(grid, (ll, (rboundary[j][0]+1,rboundary[j][1])), self_loops=False)
					grid = nx.contracted_nodes(grid, ll, (rboundary[j][0],rboundary[j][1]), self_loops=False)

					
					
					
	rectangles.append([ll,(ll[0]+numr,ll[1]+numu)])
	

nx.draw(grid,pos= {x:x for x in grid.nodes()},label=True)
print(rectangles)
	
