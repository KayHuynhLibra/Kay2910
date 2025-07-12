# GRAPH ALGORITHMS - 20 LEVELS TỪ CƠ BẢN ĐẾN NÂNG CAO

## 🎯 Tổng quan
20 level này được thiết kế để bạn học Graph Algorithms từ cơ bản đến nâng cao.

---

## 📚 **LEVEL 1: Hiểu cơ bản về Graph**
**Mục tiêu**: Hiểu khái niệm và cách biểu diễn graph

### Bài toán: Number of Islands
```python
def num_islands(grid):
    """
    Đếm số đảo trong ma trận 2D
    """
    if not grid:
        return 0
    
    def dfs(i, j):
        if (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or 
            grid[i][j] == '0'):
            return
        
        grid[i][j] = '0'  # Mark as visited
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    
    return count
```

**Độ khó**: ⭐  
**Thời gian**: O(m * n)  
**Không gian**: O(m * n)

---

## 📚 **LEVEL 2: Graph Representation**
**Mục tiêu**: Hiểu các cách biểu diễn graph

### Bài toán: Graph Representation
```python
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]
    
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)  # Undirected graph
    
    def print_graph(self):
        for i in range(self.V):
            print(f"Vertex {i}: {self.adj[i]}")
```

**Độ khó**: ⭐⭐  
**Thời gian**: O(1) cho add_edge  
**Không gian**: O(V + E)

---

## 📚 **LEVEL 3: Depth First Search (DFS)**
**Mục tiêu**: Thành thạo DFS traversal

### Bài toán: DFS Traversal
```python
def dfs_traversal(graph, start):
    """
    DFS traversal của graph
    """
    visited = [False] * len(graph)
    result = []
    
    def dfs(vertex):
        visited[vertex] = True
        result.append(vertex)
        
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    dfs(start)
    return result
```

**Độ khó**: ⭐⭐⭐  
**Thời gian**: O(V + E)  
**Không gian**: O(V)

---

## 📚 **LEVEL 4: Breadth First Search (BFS)**
**Mục tiêu**: Thành thạo BFS traversal

### Bài toán: BFS Traversal
```python
from collections import deque

def bfs_traversal(graph, start):
    """
    BFS traversal của graph
    """
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return result
```

**Độ khó**: ⭐⭐⭐  
**Thời gian**: O(V + E)  
**Không gian**: O(V)

---

## 📚 **LEVEL 5: Detect Cycle in Undirected Graph**
**Mục tiêu**: Phát hiện cycle trong undirected graph

### Bài toán: Detect Cycle in Undirected Graph
```python
def has_cycle_undirected(graph):
    """
    Phát hiện cycle trong undirected graph
    """
    visited = [False] * len(graph)
    
    def dfs(vertex, parent):
        visited[vertex] = True
        
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                if dfs(neighbor, vertex):
                    return True
            elif neighbor != parent:
                return True
        
        return False
    
    for i in range(len(graph)):
        if not visited[i]:
            if dfs(i, -1):
                return True
    
    return False
```

**Độ khó**: ⭐⭐⭐⭐  
**Thời gian**: O(V + E)  
**Không gian**: O(V)

---

## 📚 **LEVEL 6: Detect Cycle in Directed Graph**
**Mục tiêu**: Phát hiện cycle trong directed graph

### Bài toán: Detect Cycle in Directed Graph
```python
def has_cycle_directed(graph):
    """
    Phát hiện cycle trong directed graph
    """
    visited = [False] * len(graph)
    rec_stack = [False] * len(graph)
    
    def dfs(vertex):
        visited[vertex] = True
        rec_stack[vertex] = True
        
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif rec_stack[neighbor]:
                return True
        
        rec_stack[vertex] = False
        return False
    
    for i in range(len(graph)):
        if not visited[i]:
            if dfs(i):
                return True
    
    return False
```

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(V + E)  
**Không gian**: O(V)

---

## 📚 **LEVEL 7: Topological Sort**
**Mục tiêu**: Sắp xếp topo cho DAG

### Bài toán: Topological Sort
```python
def topological_sort(graph):
    """
    Sắp xếp topo cho DAG
    """
    visited = [False] * len(graph)
    stack = []
    
    def dfs(vertex):
        visited[vertex] = True
        
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                dfs(neighbor)
        
        stack.append(vertex)
    
    for i in range(len(graph)):
        if not visited[i]:
            dfs(i)
    
    return stack[::-1]
```

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(V + E)  
**Không gian**: O(V)

---

## 📚 **LEVEL 8: Shortest Path - Dijkstra**
**Mục tiêu**: Tìm đường đi ngắn nhất với Dijkstra

### Bài toán: Dijkstra's Algorithm
```python
import heapq

def dijkstra(graph, start):
    """
    Tìm đường đi ngắn nhất với Dijkstra
    """
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        dist, vertex = heapq.heappop(pq)
        
        if dist > distances[vertex]:
            continue
        
        for neighbor, weight in graph[vertex]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return distances
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O((V + E) log V)  
**Không gian**: O(V)

---

## 📚 **LEVEL 9: Shortest Path - Bellman Ford**
**Mục tiêu**: Tìm đường đi ngắn nhất với Bellman Ford

### Bài toán: Bellman Ford Algorithm
```python
def bellman_ford(edges, n, start):
    """
    Tìm đường đi ngắn nhất với Bellman Ford
    """
    distances = [float('inf')] * n
    distances[start] = 0
    
    # Relax edges n-1 times
    for _ in range(n - 1):
        for u, v, w in edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
    
    # Check for negative cycles
    for u, v, w in edges:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            return None  # Negative cycle detected
    
    return distances
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(V * E)  
**Không gian**: O(V)

---

## 📚 **LEVEL 10: All Pairs Shortest Path - Floyd Warshall**
**Mục tiêu**: Tìm đường đi ngắn nhất giữa tất cả cặp đỉnh

### Bài toán: Floyd Warshall Algorithm
```python
def floyd_warshall(graph):
    """
    Tìm đường đi ngắn nhất giữa tất cả cặp đỉnh
    """
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Initialize
    for i in range(n):
        dist[i][i] = 0
        for j, weight in graph[i]:
            dist[i][j] = weight
    
    # Floyd Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(V³)  
**Không gian**: O(V²)

---

## 📚 **LEVEL 11: Minimum Spanning Tree - Kruskal**
**Mục tiêu**: Tìm cây khung nhỏ nhất với Kruskal

### Bài toán: Kruskal's Algorithm
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

def kruskal(edges, n):
    """
    Tìm cây khung nhỏ nhất với Kruskal
    """
    edges.sort(key=lambda x: x[2])  # Sort by weight
    uf = UnionFind(n)
    mst = []
    total_weight = 0
    
    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            total_weight += w
    
    return mst, total_weight
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(E log E)  
**Không gian**: O(V)

---

## 📚 **LEVEL 12: Minimum Spanning Tree - Prim**
**Mục tiêu**: Tìm cây khung nhỏ nhất với Prim

### Bài toán: Prim's Algorithm
```python
import heapq

def prim(graph, start):
    """
    Tìm cây khung nhỏ nhất với Prim
    """
    n = len(graph)
    visited = [False] * n
    mst = []
    total_weight = 0
    
    pq = [(0, start, -1)]  # (weight, vertex, parent)
    
    while pq:
        weight, vertex, parent = heapq.heappop(pq)
        
        if visited[vertex]:
            continue
        
        visited[vertex] = True
        if parent != -1:
            mst.append((parent, vertex, weight))
            total_weight += weight
        
        for neighbor, w in graph[vertex]:
            if not visited[neighbor]:
                heapq.heappush(pq, (w, neighbor, vertex))
    
    return mst, total_weight
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O((V + E) log V)  
**Không gian**: O(V)

---

## 📚 **LEVEL 13: Strongly Connected Components**
**Mục tiêu**: Tìm các thành phần liên thông mạnh

### Bài toán: Kosaraju's Algorithm
```python
def kosaraju(graph):
    """
    Tìm các thành phần liên thông mạnh với Kosaraju
    """
    n = len(graph)
    visited = [False] * n
    order = []
    
    # First DFS to get order
    def dfs1(vertex):
        visited[vertex] = True
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                dfs1(neighbor)
        order.append(vertex)
    
    for i in range(n):
        if not visited[i]:
            dfs1(i)
    
    # Transpose graph
    transposed = [[] for _ in range(n)]
    for i in range(n):
        for j in graph[i]:
            transposed[j].append(i)
    
    # Second DFS to find SCCs
    visited = [False] * n
    sccs = []
    
    def dfs2(vertex, scc):
        visited[vertex] = True
        scc.append(vertex)
        for neighbor in transposed[vertex]:
            if not visited[neighbor]:
                dfs2(neighbor, scc)
    
    for i in reversed(order):
        if not visited[i]:
            scc = []
            dfs2(i, scc)
            sccs.append(scc)
    
    return sccs
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(V + E)  
**Không gian**: O(V + E)

---

## 📚 **LEVEL 14: Articulation Points**
**Mục tiêu**: Tìm các điểm khớp trong graph

### Bài toán: Articulation Points
```python
def find_articulation_points(graph):
    """
    Tìm các điểm khớp trong graph
    """
    n = len(graph)
    visited = [False] * n
    disc = [0] * n
    low = [0] * n
    parent = [-1] * n
    articulation_points = set()
    time = 0
    
    def dfs(vertex):
        nonlocal time
        visited[vertex] = True
        disc[vertex] = low[vertex] = time
        time += 1
        children = 0
        
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                parent[neighbor] = vertex
                children += 1
                dfs(neighbor)
                
                low[vertex] = min(low[vertex], low[neighbor])
                
                if parent[vertex] == -1 and children > 1:
                    articulation_points.add(vertex)
                elif parent[vertex] != -1 and low[neighbor] >= disc[vertex]:
                    articulation_points.add(vertex)
            elif neighbor != parent[vertex]:
                low[vertex] = min(low[vertex], disc[neighbor])
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    return list(articulation_points)
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(V + E)  
**Không gian**: O(V)

---

## 📚 **LEVEL 15: Bridges**
**Mục tiêu**: Tìm các cầu trong graph

### Bài toán: Bridges
```python
def find_bridges(graph):
    """
    Tìm các cầu trong graph
    """
    n = len(graph)
    visited = [False] * n
    disc = [0] * n
    low = [0] * n
    parent = [-1] * n
    bridges = []
    time = 0
    
    def dfs(vertex):
        nonlocal time
        visited[vertex] = True
        disc[vertex] = low[vertex] = time
        time += 1
        
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                parent[neighbor] = vertex
                dfs(neighbor)
                
                low[vertex] = min(low[vertex], low[neighbor])
                
                if low[neighbor] > disc[vertex]:
                    bridges.append((vertex, neighbor))
            elif neighbor != parent[vertex]:
                low[vertex] = min(low[vertex], disc[neighbor])
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    return bridges
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(V + E)  
**Không gian**: O(V)

---

## 📚 **LEVEL 16: Bipartite Graph**
**Mục tiêu**: Kiểm tra graph có phải bipartite không

### Bài toán: Bipartite Graph
```python
def is_bipartite(graph):
    """
    Kiểm tra graph có phải bipartite không
    """
    n = len(graph)
    color = [-1] * n
    
    def dfs(vertex, c):
        color[vertex] = c
        
        for neighbor in graph[vertex]:
            if color[neighbor] == -1:
                if not dfs(neighbor, 1 - c):
                    return False
            elif color[neighbor] == c:
                return False
        
        return True
    
    for i in range(n):
        if color[i] == -1:
            if not dfs(i, 0):
                return False
    
    return True
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(V + E)  
**Không gian**: O(V)

---

## 📚 **LEVEL 17: Network Flow - Ford Fulkerson**
**Mục tiêu**: Tìm luồng cực đại với Ford Fulkerson

### Bài toán: Ford Fulkerson Algorithm
```python
def ford_fulkerson(graph, source, sink):
    """
    Tìm luồng cực đại với Ford Fulkerson
    """
    def bfs(graph, source, sink, parent):
        visited = [False] * len(graph)
        queue = [source]
        visited[source] = True
        
        while queue:
            u = queue.pop(0)
            for v, capacity in enumerate(graph[u]):
                if not visited[v] and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False
    
    n = len(graph)
    parent = [-1] * n
    max_flow = 0
    
    while bfs(graph, source, sink, parent):
        path_flow = float('inf')
        v = sink
        
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = parent[v]
        
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
        
        max_flow += path_flow
    
    return max_flow
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(VE²)  
**Không gian**: O(V²)

---

## 📚 **LEVEL 18: Hamiltonian Path**
**Mục tiêu**: Tìm đường đi Hamilton

### Bài toán: Hamiltonian Path
```python
def hamiltonian_path(graph):
    """
    Tìm đường đi Hamilton
    """
    n = len(graph)
    
    def backtrack(path, visited):
        if len(path) == n:
            return path
        
        current = path[-1]
        for next_vertex in range(n):
            if (next_vertex not in visited and 
                graph[current][next_vertex] == 1):
                visited.add(next_vertex)
                result = backtrack(path + [next_vertex], visited)
                if result:
                    return result
                visited.remove(next_vertex)
        
        return None
    
    for start in range(n):
        result = backtrack([start], {start})
        if result:
            return result
    
    return None
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n!)  
**Không gian**: O(n)

---

## 📚 **LEVEL 19: Advanced Graph Algorithms**
**Mục tiêu**: Thuật toán graph nâng cao

### Bài toán: Advanced Graph
```python
def advanced_graph_algorithm(graph, start, end, k):
    """
    Thuật toán graph nâng cao với nhiều điều kiện
    """
    from collections import deque
    
    n = len(graph)
    # dp[i][j] = số đường đi từ start đến i với j edges
    dp = [[0] * (k + 1) for _ in range(n)]
    dp[start][0] = 1
    
    for edges in range(k):
        for vertex in range(n):
            if dp[vertex][edges] > 0:
                for neighbor in graph[vertex]:
                    dp[neighbor][edges + 1] += dp[vertex][edges]
    
    return dp[end][k]
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(V * K)  
**Không gian**: O(V * K)

---

## 📚 **LEVEL 20: Master Level - Complex Graph Applications**
**Mục tiêu**: Ứng dụng graph trong bài toán phức tạp nhất

### Bài toán: Master Graph
```python
def master_graph_algorithm(graph, constraints):
    """
    Thuật toán graph master với nhiều ràng buộc phức tạp
    """
    n = len(graph)
    
    def is_valid_path(path):
        # Kiểm tra các ràng buộc
        for constraint in constraints:
            if not constraint(path):
                return False
        return True
    
    def find_optimal_path():
        # Tìm đường đi tối ưu với các ràng buộc
        best_path = None
        best_cost = float('inf')
        
        def backtrack(path, cost, visited):
            nonlocal best_path, best_cost
            
            if len(path) == n:
                if is_valid_path(path) and cost < best_cost:
                    best_cost = cost
                    best_path = path[:]
                return
            
            current = path[-1]
            for next_vertex in range(n):
                if next_vertex not in visited:
                    new_cost = cost + graph[current][next_vertex]
                    if new_cost < best_cost:
                        visited.add(next_vertex)
                        backtrack(path + [next_vertex], new_cost, visited)
                        visited.remove(next_vertex)
        
        for start in range(n):
            backtrack([start], 0, {start})
        
        return best_path, best_cost
    
    return find_optimal_path()
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n!)  
**Không gian**: O(n)

---

## 🎯 **Lộ trình học tập**

### **Giai đoạn 1 (Level 1-5)**: Nền tảng
- Hiểu khái niệm graph
- Thành thạo DFS/BFS
- Làm quen với pattern cơ bản

### **Giai đoạn 2 (Level 6-10)**: Nâng cao
- Shortest path algorithms
- Minimum spanning tree
- Tối ưu hóa thuật toán

### **Giai đoạn 3 (Level 11-15)**: Chuyên sâu
- Advanced graph algorithms
- Network flow
- Tối ưu hóa bộ nhớ

### **Giai đoạn 4 (Level 16-20)**: Master
- Complex applications
- Multiple constraints
- Edge cases phức tạp

## 💡 **Mẹo cho từng level**

- **Level 1-5**: Tập trung vào hiểu pattern cơ bản
- **Level 6-10**: Chú ý đến việc chọn thuật toán phù hợp
- **Level 11-15**: Hiểu sâu về graph theory
- **Level 16-20**: Thực hành nhiều và phân tích các trường hợp đặc biệt

## 🔥 **Common Patterns**

### **DFS Pattern**
```python
def dfs(graph, start):
    visited = set()
    def dfs_helper(vertex):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs_helper(neighbor)
    dfs_helper(start)
```

### **BFS Pattern**
```python
def bfs(graph, start):
    from collections import deque
    queue = deque([start])
    visited = {start}
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### **Shortest Path Pattern**
```python
def shortest_path(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        dist, vertex = heapq.heappop(pq)
        for neighbor, weight in graph[vertex]:
            if dist + weight < distances[neighbor]:
                distances[neighbor] = dist + weight
                heapq.heappush(pq, (distances[neighbor], neighbor))
``` 