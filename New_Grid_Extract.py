from itertools import combinations

import geopandas as gpd

from shapely import Point, Polygon

def rect_graph(input_graph,pos):
    '''This function extracts the dual graph of the 4 cycles of the input graph'''
    graph=input_graph.copy()
    
    rgraph=nx.Graph()
    nlist = list(graph.nodes)
    for n in nlist:
        nhlist=list(graph.neighbors(n))
        for i,j in combinations(nhlist,2):
            if (i,j) not in graph.edges():
                for k in graph.neighbors(i):
                    if k != n:
                        if (j,k) in graph.edges() and (n,k) not in graph.edges():


                            inside = 0

                            P = Polygon(gpd.GeoSeries([Point(pos[i]),Point(pos[j]),Point(pos[k]),Point(pos[n])]).convex_hull)

                            neighbors = set(graph.neighbors(i))
                            neighbors = neighbors.union(set(graph.neighbors(j)))
                            neighbors = neighbors.union(set(graph.neighbors(k)))
                            neighbors = neighbors.union(set(graph.neighbors(n)))
                            neighbors.remove(i)
                            neighbors.remove(j)
                            neighbors.remove(k)
                            neighbors.remove(n)
                            
                            for node in neighbors:

                                if P.intersects(Point(pos[n])):
                                    inside += 1
                                
                            
                            if inside == 0:
                                rgraph.add_node((n,i,j,k))
                        
        graph.remove_node(n)
    #plt.figure()
    #nx.draw(rgraph)    
    for i,j in combinations(list(rgraph.nodes),2):
        if len(set(i+j))<7:
            rgraph.add_edge(i,j)
        
                        
    return rgraph
