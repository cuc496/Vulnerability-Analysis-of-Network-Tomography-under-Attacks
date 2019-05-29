def edgebetw(u,v):
    for e in u.edges():
        if e in v.edges():
            return e
    return -1

def getAdjNodes(node):
    nodes = []
    for e in node.edges():
        if e.node1 != node:
            nodes.append(e.node1)
        if e.node2 != node:
            nodes.append(e.node2)
    return nodes

def shortestpath(graph, cost, source, target):
    dist = {node:float("inf") for node in graph.nodes()}
    dist[source] = 0
    #print(dist)
    pre = {node:None for node in graph.nodes()}
    while dist:
        #print("dist:{}".format(dist))
        minNode = min(dist, key = lambda x : dist.get(x))
        if minNode == target:
            break
        mindist = dist.pop(minNode)
        #print("mindist:{}".format(mindist))
        if mindist == float("inf"):
            return -1
        #print("getAdjNodes(minNode):{}".format(getAdjNodes(minNode)))
        for node in getAdjNodes(minNode):
            if node not in dist:
                continue
            #e = edgebetw(minNode, node)
            #c=cost(e)
            c = 1.0
            if dist[node] > (mindist + c):
                dist[node] = mindist + c
                pre[node] = minNode
            
    
    pathByEdge = []
    current = target
    while pre[current]:
        pathByEdge.insert(0, edgebetw(pre[current], current))
        current = pre[current]
    
    return [pathByEdge]