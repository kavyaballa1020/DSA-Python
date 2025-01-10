class Edge:
    def __init__(self,src,des):
        self.src=src
        self.des=des
class Graph:
    def __init__(self,vertices):
        self.graph=[[] for i in range(vertices)]
        
    def create_graph(self): 
        self.graph[0].append(Edge(0,1))
        self.graph[1].append(Edge(1, 2))
        self.graph[1].append(Edge(1, 3))
        self.graph[2].append(Edge(2, 0))
        self.graph[2].append(Edge(2, 1))
        self.graph[2].append(Edge(2, 3))
        self.graph[3].append(Edge(3, 2))
        self.graph[3].append(Edge(3, 1))
    
    def dfs(self,graph,current,visited):
        visited[current]=True
        print(current,end=" ")
        for edge in graph[current]:
            if not visited[edge.des]:
                self.dfs(graph,edge.des,visited)
vertices=4
current=0
visited=[False]*vertices
graph=Graph(vertices)
graph.create_graph()
graph.dfs(graph.graph,current,visited)