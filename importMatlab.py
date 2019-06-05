from scipy.io import loadmat
from pygraphml import Graph

def loadgraph(addr):
    gphml = Graph()
    gmatrix = loadmat(addr)["A"].toarray()
    for i in range(len(gmatrix)):
        n = gphml.add_node()
        n.id = str(i)
    for i in range(len(gmatrix)):
        for j in range(i+1, len(gmatrix)):
            if gmatrix[i,j] == 1:
                gphml.add_edge_by_id(str(i), str(j))
    return gphml
                