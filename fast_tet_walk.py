import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter
from random import choice, shuffle

n = 3 #grid size
m = 3 #grid size
k = 5 # number of possible steps

grid = nx.grid_graph([4*n,4*m])

assignment = {}
orientation = {}
nub_pos = {}
triple_assign = {}
block_assign = {}



initial_assignments = {(0,0):0, (1,0):0, (2,0):0, (1,1):0, (0,1):1,(0,2):1,(0,3):1,(1,2):1,
                        (1,3):2,(2,3):2,(3,3):2,(2,2):2,(3,2):3,(2,1):3,(3,1):3,(3,0):3}
                        
                        
initial_orientations = {0:'u',1:'r',2:'d',3:'l'}

initial_nubs = [(1,1),(1,2),(2,2),(2,1)]

initial_pos = {0:(1,1),1:(1,2),2:(2,2),3:(2,1)}

triple_to_add = {0:(0,0),1:(0,1),2:(1,1),3:(1,0)}


for i in range(4*n):
    for j in range(4*m):
        assignment[(i,j)] = initial_assignments[(i%4,j%4)] + 4 * (int(i/4) + n* int(j/4))
        
        if (i%4,j%4) in initial_nubs:
        
            orientation[assignment[(i,j)]] = initial_orientations[assignment[(i,j)]%4]
            
            nub_pos[assignment[(i,j)]] = (i,j)
            
            triple_assign[assignment[(i,j)]] = (i+triple_to_add[assignment[(i,j)]%4][0],
            j+triple_to_add[assignment[(i,j)]%4][1])
            
            block_assign[(i+triple_to_add[assignment[(i,j)]%4][0],
            j+triple_to_add[assignment[(i,j)]%4][1])] = assignment[(i,j)]
            

nodes_by_part = {x:[j for j in assignment.keys() if assignment[j]==x] for x in range(4*m*n)}


            
#nx.draw(grid,pos= {x:x for x in grid.nodes()},node_color=[assignment[x] %4 for x in grid.nodes()],cmap = 'tab20',label=True)#cmap=plt.cm.jet,label=True)
#plt.show()





           
def mv2(assignment,labels,nub_pos,orientation): #labels sorted lr or ud

    up_nub = nub_pos[labels[0]]
    
    if orientation[labels[0]] == 'l':
        if nub_pos[labels[0]][1] > nub_pos[labels[1]][1]:
            assignment[(up_nub[0]+2,up_nub[1])] = labels[0]
            assignment[(up_nub[0]+1,up_nub[1]-1)] = labels[1]
            
            nub_pos[labels[0]] = (up_nub[0]+1,up_nub[1]+1)
            nub_pos[labels[1]] = (up_nub[0]+2,up_nub[1]-2)
            
            orientation[labels[0]] = 'u'
            orientation[labels[1]] = 'd'
            
            
        else:
            assignment[(up_nub[0]+2,up_nub[1])] = labels[0]
            assignment[(up_nub[0]+1,up_nub[1]+1)] = labels[1]
            
            nub_pos[labels[0]] = (up_nub[0]+1,up_nub[1]-1)
            nub_pos[labels[1]] = (up_nub[0]+2,up_nub[1]+2)
            
            orientation[labels[0]] = 'd'
            orientation[labels[1]] = 'u'
            
            
    else:
        if nub_pos[labels[0]][0] > nub_pos[labels[1]][0]:
            assignment[(up_nub[0],up_nub[1]-2)] = labels[0]
            assignment[(up_nub[0]-1,up_nub[1]-1)] = labels[1]
            
            nub_pos[labels[0]] = (up_nub[0]+1,up_nub[1]-1)
            nub_pos[labels[1]] = (up_nub[0]-2,up_nub[1]-2)
            
            orientation[labels[0]] = 'r'
            orientation[labels[1]] = 'l'
            
        else:
            assignment[(up_nub[0],up_nub[1]-2)] = labels[0]
            assignment[(up_nub[0]+1,up_nub[1]-1)] = labels[1]
            
            nub_pos[labels[0]] = (up_nub[0]-1,up_nub[1]-1)
            nub_pos[labels[1]] = (up_nub[0]+2,up_nub[1]-2)
            
            orientation[labels[0]] = 'l'
            orientation[labels[1]] = 'r'
            
            
            
    return assignment, nub_pos, orientation
            


    
def mv4(assignment,labels,nodes_by_part,nub_pos,orientation): #labels sorted urdl

    joined_nodes = set()
    for i in range(4):
        joined_nodes.add(nodes_by_part[labels[i]][0])
        joined_nodes.add(nodes_by_part[labels[i]][1])
        joined_nodes.add(nodes_by_part[labels[i]][2])
        joined_nodes.add(nodes_by_part[labels[i]][3])
        
    
    
    up_nub = nub_pos[labels[0]]
    #print(up_nub)
    
    if (up_nub[0]+2, up_nub[1]-1) in joined_nodes:
        #print('yes')
    
        assignment[(up_nub[0]-1, up_nub[1])] = labels[0]
        assignment[(up_nub[0]-1, up_nub[1]+1)] = labels[0]
        assignment[(up_nub[0], up_nub[1]+2)] = labels[1]
        assignment[(up_nub[0]+1, up_nub[1]+2)] = labels[1]
        assignment[(up_nub[0]+2, up_nub[1])] = labels[2]
        assignment[(up_nub[0]+2, up_nub[1]+1)] = labels[2]
        assignment[(up_nub[0], up_nub[1]-1)] = labels[3]
        assignment[(up_nub[0]+1, up_nub[1]-1)] = labels[3]
        
        
        orientation[labels[0]] = 'r'
        orientation[labels[1]] = 'd'
        orientation[labels[2]] = 'l'
        orientation[labels[3]] = 'u'
        
        
        
        
        
        
    else:
        #print('no')
    
        assignment[(up_nub[0]+1, up_nub[1])] = labels[0]
        assignment[(up_nub[0]+1, up_nub[1]+1)] = labels[0]
        assignment[(up_nub[0], up_nub[1]-1)] = labels[1]
        assignment[(up_nub[0]-1, up_nub[1]-1)] = labels[1]
        assignment[(up_nub[0]-2, up_nub[1])] = labels[2]
        assignment[(up_nub[0]-2, up_nub[1]+1)] = labels[2]
        assignment[(up_nub[0], up_nub[1]+2)] = labels[3]
        assignment[(up_nub[0]-1, up_nub[1]+2)] = labels[3]
        
        
        orientation[labels[0]] = 'l'
        orientation[labels[1]] = 'u'
        orientation[labels[2]] = 'r'
        orientation[labels[3]] = 'd'
        
        
    return assignment, orientation
    
    
'''    

#TESTS OF STEPS        

assignment, nub_pos, orientation = mv2(assignment, [12,2], nub_pos, orientation)
nx.draw(grid,pos= {x:x for x in grid.nodes()},node_color=[assignment[x] %4 for x in grid.nodes()],cmap = 'tab20')#cmap=plt.cm.jet,label=True)
plt.show()        

assignment, nub_pos, orientation = mv2(assignment, [12,2], nub_pos, orientation)
nx.draw(grid,pos= {x:x for x in grid.nodes()},node_color=[assignment[x] %4 for x in grid.nodes()],cmap = 'tab20')#cmap=plt.cm.jet,label=True)
plt.show()        

assignment, nub_pos, orientation = mv2(assignment, [3,5], nub_pos, orientation)
nx.draw(grid,pos= {x:x for x in grid.nodes()},node_color=[assignment[x] %4 for x in grid.nodes()],cmap = 'tab20')#cmap=plt.cm.jet,label=True)
plt.show()        
assignment, nub_pos, orientation = mv2(assignment, [5,3], nub_pos, orientation)

nx.draw(grid,pos= {x:x for x in grid.nodes()},node_color=[assignment[x] %4 for x in grid.nodes()],cmap = 'tab20')#cmap=plt.cm.jet,label=True)
plt.show()        

        

        
assignment, orientation = mv4(assignment,[0,1,2,3],nodes_by_part,nub_pos, orientation)  

nx.draw(grid,pos= {x:x for x in grid.nodes()},node_color=[assignment[x] %4 for x in grid.nodes()],cmap = 'tab20')#cmap=plt.cm.jet,label=True)
plt.show()        

        

nodes_by_part = {x:[j for j in assignment.keys() if assignment[j]==x] for x in range(4*m*n)}
        
assignment, orientation = mv4(assignment,[3,0,1,2],nodes_by_part,nub_pos, orientation)  

#nx.draw(grid,pos= {x:x for x in grid.nodes()},node_color=[assignment[x] %4 for x in grid.nodes()],cmap = 'tab20')#cmap=plt.cm.jet,label=True)
#plt.show()        
        
        
'''

      
    

def get_graph(nodes_by_part, block_assign, assignment):
    CG = nx.DiGraph()


    for i in range(4*n):
        for j in range(4*m):
            if i%2 == 1 and j%2 == 1:

                current_block = {(i,j),(i-1,j),(i,j-1),(i-1,j-1)}
                for h in nodes_by_part[block_assign[(i,j)]]:
                    if h not in current_block:
                        #print(h)
                        target_block = (h[0]+(1+h[0])%2,h[1]+(1+h[1])%2)
                        #print(target_block)
                
                CG.add_edge((i,j), target_block)
                
                
    #nx.draw(CG ,pos= {x:x for x in CG.nodes()},node_color=[assignment[x] %4 for x in CG.nodes()],cmap = 'tab20')
    #plt.show()
    
    return CG
    
    
CG = get_graph(nodes_by_part, block_assign, assignment)

#print(((1,1),(3,1)) in CG.edges())

#nx.draw(grid,pos= {x:x for x in grid.nodes()},node_color=[assignment[x] %4 for x in grid.nodes()],cmap = 'tab20')#cmap=plt.cm.jet,label=True)
#nx.draw(CG ,pos= {x:(x[0]-.5,x[1]-.5) for x in CG.nodes()},node_size = 5)

#plt.show()



def get_height(n, m, CG):

    X = {}
    
    
    for i in range(4*n):
        for j in range(4*m):
            if i%2 == 0 and j%2 == 0:
            
                if i == 0 or j == 0:
                    X[(i,j)] = 0
                    
                else:
                    if ((i-1,j-1),(i-1,j+1)) in CG.edges():
                        X[(i,j)] = X[(i-2,j)] - 1
                    
                    elif ((i-1,j+1),(i-1,j-1)) in CG.edges():
                        X[(i,j)] = X[(i-2,j)] + 1
                        
                    else:
                        X[(i,j)] = X[(i-2,j)]
                    
                    
    return X
    
    
X = get_height(n, m, CG)                   
            
nx.draw(grid,pos= {x:x for x in grid.nodes()},node_color=[assignment[x] %4 for x in grid.nodes()],cmap = 'tab20')#cmap=plt.cm.jet,label=True)
nx.draw(CG ,pos= {x:(x[0]-.5,x[1]-.5) for x in CG.nodes()},node_size = 5)

for nc in X.keys():
    plt.text(nc[0]-.5,nc[1]-.5,str(X[nc]))

plt.show()    


for step in range(100000):
    #print(step)
    
    nc = choice(list(grid.nodes()))
    
    #if step == 0:
    #   nc = (0,4)
    
    nub = nub_pos[assignment[nc]]
    
    
    
    if orientation[assignment[nc]] == 'u':
    
        temp = [-1,-1,-1,-1]
    
        if nub[1] >2 and nub[0] > 1 and nub[0] < 4*m -2:

            if assignment[(nub[0],nub[1]-2)] == assignment[(nub[0]-1,nub[1]-2)] == assignment[(nub[0]-2,nub[1]-2)] == assignment[(nub[0]-2,nub[1]-3)]:
                
                temp[0]=0
                
                
            elif assignment[(nub[0],nub[1]-2)] == assignment[(nub[0]+1,nub[1]-2)] == assignment[(nub[0]+2,nub[1]-2)] == assignment[(nub[0]+1,nub[1]-3)]:
                temp[1]=1
                
                
                

                       
        if nub[1]< 4*n -1:
            
            if nub_pos[assignment[(nub[0]-1,nub[1])]] == (nub[0]-1,nub[1]) and nub_pos[assignment[(nub[0]-1,nub[1]+1)]] == (nub[0]-1,nub[1]+1) and nub_pos[assignment[(nub[0],nub[1]+1)]] == (nub[0],nub[1]+1):
                temp[2] = 2
                 
   
                
                
            elif nub_pos[assignment[(nub[0],nub[1]+1)]] == (nub[0],nub[1]+1) and nub_pos[assignment[(nub[0]+1,nub[1]+1)]] == (nub[0]+1,nub[1]+1) and nub_pos[assignment[(nub[0]+1,nub[1])]] == (nub[0]+1,nub[1]):
                temp[3] = 3    
                 

                
        test = choice(range(4))
        
        if temp[test] == 0:
        
            assignment, nub_pos, orientation = mv2(assignment, [assignment[nc],
                assignment[(nub[0],nub[1]-2)]], nub_pos, orientation)
           
        if temp[test] == 1:
        
            assignment, nub_pos, orientation = mv2(assignment, [assignment[nc],
                assignment[(nub[0],nub[1]-2)]], nub_pos, orientation)
                
        if temp[test] == 2:
        
            assignment, orientation = mv4(assignment,[assignment[nc],assignment[(nub[0]-1,nub[1])],assignment[(nub[0]-1,nub[1]+1)],assignment[(nub[0],nub[1]+1)]],nodes_by_part,nub_pos, orientation)  
            
        if temp[test] == 3:
        
            assignment, orientation = mv4(assignment,[assignment[nc],assignment[(nub[0],nub[1]+1)],assignment[(nub[0]+1,nub[1]+1)],assignment[(nub[0]+1,nub[1])]],nodes_by_part,nub_pos, orientation)  
        
        

    if orientation[assignment[nc]] == 'l':
    
        temp = [-1,-1,-1,-1]
    
        if nub[0] < 4*m -3 and nub[1] > 1 and nub[0] < 4*n-1 and nub[1] < 4*m -2:

            if assignment[(nub[0]+2,nub[1])] == assignment[(nub[0]+2,nub[1]+1)] == assignment[(nub[0]+2,nub[1]+2)] == assignment[(nub[0]+3,nub[1]+1)]:
                
                temp[0]=0
                
                
            elif assignment[(nub[0]+2,nub[1])] == assignment[(nub[0]+2,nub[1]-1)] == assignment[(nub[0]+2,nub[1]-2)] == assignment[(nub[0]+3,nub[1]-1)]:
                temp[1]=1
                
                
                

                       
        if nub[1]< 4*n -1:
            
            if nub_pos[assignment[(nub[0],nub[1]-1)]] == (nub[0],nub[1]-1) and nub_pos[assignment[(nub[0]-1,nub[1]-1)]] == (nub[0]-1,nub[1]-1) and nub_pos[assignment[(nub[0]-1,nub[1])]] == (nub[0]-1,nub[1]):
                temp[2] = 2
                 
   
                
                
            elif nub_pos[assignment[(nub[0]-1,nub[1])]] == (nub[0]-1,nub[1]) and nub_pos[assignment[(nub[0]-1,nub[1]+1)]] == (nub[0]-1,nub[1]+1) and nub_pos[assignment[(nub[0],nub[1]+1)]] == (nub[0],nub[1]+1):
                temp[3] = 3    
                 

                
        test = choice(range(4))
        
        if temp[test] == 0:
        
            assignment, nub_pos, orientation = mv2(assignment, [assignment[nc],
                assignment[(nub[0]+2,nub[1])]], nub_pos, orientation)
           
        if temp[test] == 1:
        
            assignment, nub_pos, orientation = mv2(assignment, [assignment[nc],
                assignment[(nub[0]+2,nub[1])]], nub_pos, orientation)
                
        if temp[test] == 2:
        
            assignment, orientation = mv4(assignment,[assignment[(nub[0],nub[1]-1)],assignment[(nub[0]-1,nub[1]-1)],assignment[(nub[0]-1,nub[1])],assignment[nc]],nodes_by_part,nub_pos, orientation)  
            
        if temp[test] == 3:
        
            assignment, orientation = mv4(assignment,[assignment[(nub[0]-1,nub[1])],assignment[(nub[0]-1,nub[1]+1)],assignment[(nub[0],nub[1]+1)],assignment[nc]],nodes_by_part,nub_pos, orientation)         
        
        
            
             
                          
                

    
    
    nodes_by_part = {x:[j for j in assignment.keys() if assignment[j]==x] for x in range(4*m*n)}
                     

tempcolors = list(range(4*m*n))
shuffle(tempcolors)

scolors = {x: tempcolors[x] for x in range(4*m*n)}

    
CG = get_graph(nodes_by_part, block_assign, assignment)
X = get_height(n, m, CG)                   
    
nx.draw(grid,pos= {x:x for x in grid.nodes()},node_color=[scolors[assignment[x]] for x in grid.nodes()],cmap = 'tab20')#cmap=plt.cm.jet,label=True)
nx.draw(CG ,pos= {x:(x[0]-.5,x[1]-.5) for x in CG.nodes()},node_size = 5)

for nc in X.keys():
    plt.text(nc[0]-.5,nc[1]-.5,str(X[nc]))

plt.show()           
    
    
        
            
            
    
    
                



        
         
    
    
    

