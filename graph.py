class graph:
    def __init__(self,nvertices):
        self.nvertices=nvertices
        self.adjmatrix=[[0 for i in range(nvertices)] for j in range (nvertices)]
    def addedge(self,v1,v2):
        self.adjmatrix[v1][v2]=1
        self.adjmatrix[v2][v1]=1
    def removeedge(self,v1,v2):
        if self.containedge(v1,v2) is False:
            return
        self.adjmatrix[v1][v2]=0
        self.adjmatrix[v2][v1]=0
    def containedge(self,v1,v2):
        return True  if self.adjmatrix[v1][v2] >0 else False
    def __str__(self):
        return str(self.adjmatrix)
g=graph(5)
g.addedge(0,1)
g.addedge(1,3)
g.addedge(2,4)
print(g)

"""
[[0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0]]"""
