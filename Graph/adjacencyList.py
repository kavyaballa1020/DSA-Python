class Edge:
    def __init__(self, src, des):
        self.src = src
        self.des = des

class AdjacencyList:
    def __init__(self, vertices):
        self.graph = [[] for _ in range(vertices)]
        
    def create_graph(self):
        self.graph[0].append(Edge(0, 1))
        self.graph[1].append(Edge(1, 2))
        self.graph[1].append(Edge(1, 3))
        self.graph[2].append(Edge(2, 0))
        self.graph[2].append(Edge(2, 1))
        self.graph[2].append(Edge(2, 3))
        self.graph[3].append(Edge(3, 2))
        self.graph[3].append(Edge(3, 1))
        
    def print_graph(self):
        for i in range(len(self.graph)):
            print(f"Vertex {i}: ", end="")
            for edge in self.graph[i]:  
                print(f"({edge.src} -> {edge.des})", end=" ")
            print()

vertices = 4
graph = AdjacencyList(vertices)
graph.create_graph()
graph.print_graph()
