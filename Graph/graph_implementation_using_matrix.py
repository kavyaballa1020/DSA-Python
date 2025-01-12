class graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.adj_matrix=[]
        
        for i in range(vertices):
            row=[]
            for j in range(vertices):
                row.append(0)
            self.adj_matrix.append(row)
            
    def add_edge(self,src,des):
        self.adj_matrix[src][des]=1
        self.adj_matrix[des][src]=1
    
    def remove_edge(self,src,des):
        self.adj_matrix[src][des]=0
        self.adj_matrix[des][src]=0
    
    def display(self):
        for row in self.adj_matrix:
            print(row)

g=graph(4)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,3)
g.display()
