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
    def dfs(self):
        visited=[False for i in range(self.nvertices)]
        self.__dfshelper(0,visited)
    def __dfshelper(self,sv,visited):
        print(sv,end=" ")
        visited[sv]=True
        for i in range(self.nvertices):
            if (self.adjmatrix[sv][i]>0 and visited[i] is False):
                self.__dfshelper(i,visited)
    def containedge(self,v1,v2):
        return True  if self.adjmatrix[v1][v2] >0 else False
g=graph(7)
g.addedge(0,1)
g.addedge(0,2)
g.addedge(1,3)
g.addedge(1,4)
g.addedge(2,6)
g.addedge(4,5)
g.addedge(5,6)
g.dfs()


"""
0 1 3 4 5 6 2
"""
