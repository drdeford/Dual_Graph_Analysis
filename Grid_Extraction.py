def rect_graph(graph):
    rgraph=nx.Graph()
    nlist = list(graph.nodes)
    for n in nlist:
        nhlist=list(graph.neighbors(n))
        for i,j in combinations(nhlist,2):
            if (i,j) not in graph.edges():
                for k in graph.neighbors(i):
                    if k != n:
                        if (j,k) in graph.edges() and (n,k) not in graph.edges():
                            rgraph.add_node((n,i,j,k))
                        
        graph.remove_node(n)
        
    for i,j in combinations(list(rgraph.nodes),2):
        if len(set(i+j))<7:
            rgraph.add_edge(i,j)
        
                        
    return rgraph

h=rect_graph(grid)
plt.figure()
nx.draw(h)
