import matplotlib.pyplot as plt
import networkx as nx
import matplotlib
#reference
#https://networkx.github.io/documentation/networkx-2.2/auto_examples/index.html#drawing
def plot(graph, weights, monitors, LMs, pos=None):
    #if multiple:
    #    plt.subplots(nrows=1, ncols=2)
    matplotlib.rcParams.update({'font.size': 15})
    fig, ax = plt.subplots(nrows=1, ncols=3)
    subp = [131, 132, 133]
    j=0
    xgroups = ["terminal", "node", "uncompromised link", "compromised link"]
    handles = []
    print("LM:{}".format(len(LMs)))
    LMs.insert(0,[])
    for LM in LMs:
        G = nx.Graph()
        Nodes=[]
        monitorNodes = []
        for edge, w in weights.items():
            G.add_edge(edge.node1.id, edge.node2.id , weight=0.1)
            if edge.node2.id not in Nodes:
                Nodes.append(edge.node2.id)
            if edge.node1.id not in Nodes:
                Nodes.append(edge.node1.id)
        plt.subplot(subp[j])
        j+=1
        for edge in LM:
            G.add_edge(edge.node1.id, edge.node2.id , weight=1.0)
        
        for m in monitors:
            monitorNodes.append(m.id)
        
        
        lm = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.5]
        l = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.5]
        if pos is None or j==0:
            pos = nx.spring_layout(G)
            
        # nodes
        
        a1= nx.draw_networkx_nodes(G, pos, node_size=400, nodelist=monitorNodes, node_color='black', alpha=0.3, label="terminals")
        a2= nx.draw_networkx_nodes(G, pos, node_size=80, nodelist=Nodes, node_color="black", alpha=1.0, label="nodes")
        a3= nx.draw_networkx_edges(G, pos, edgelist=l, width=1, edge_color="black", label="links")
        a4= nx.draw_networkx_edges(G, pos, edgelist=lm,
                           width=5, alpha=0.8, edge_color="red", label="compromised links")
        
        if j==0:
            handles.append(nx)
        plt.axis('off')
    #nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
    fig.legend(handles=[a1,a2,a3,a4], labels=xgroups, loc="lower center" , bbox_transform=fig.transFigure, mode="expand", ncol=5)
    #plt.legend(loc="lower center", mode="expand")
    
    plt.show()
    return pos