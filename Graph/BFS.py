from collections import deque

class Edge:
    def __init__(self, src, des):
        self.src = src
        self.des = des

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
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

    def bfs(self):
        q = deque()
        visited = [False] * self.vertices

        q.append(0)

        while q:
            current = q.popleft()

            if not visited[current]:
                print(current, end=" ")
                visited[current] = True

                for edge in self.graph[current]:
                    if not visited[edge.des]:
                        q.append(edge.des)

# Usage
vertices = 4
graph = Graph(vertices)
graph.create_graph()
graph.bfs()
