# TOPOLOGICAL SORT - 10 LEVELS TỪ CƠ BẢN ĐẾN NÂNG CAO

## 🎯 Tổng quan
10 level này được thiết kế để bạn học Topological Sort từ cơ bản đến nâng cao.

---

## 📚 **LEVEL 1: Hiểu cơ bản về Topological Sort**
**Mục tiêu**: Hiểu khái niệm và cách hoạt động

### Bài toán: Course Schedule
```python
from collections import defaultdict, deque

def can_finish(num_courses, prerequisites):
    """
    Kiểm tra xem có thể hoàn thành tất cả khóa học không
    """
    # Tạo adjacency list
    graph = defaultdict(list)
    in_degree = [0] * num_courses
    
    # Xây dựng graph và tính in-degree
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # BFS với queue
    queue = deque()
    for i in range(num_courses):
        if in_degree[i] == 0:
            queue.append(i)
    
    completed = 0
    while queue:
        course = queue.popleft()
        completed += 1
        
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
    
    return completed == num_courses
```

**Độ khó**: ⭐  
**Thời gian**: O(V + E)  
**Không gian**: O(V + E)

---

## 📚 **LEVEL 2: Course Schedule II**
**Mục tiêu**: Tìm thứ tự hoàn thành khóa học

### Bài toán: Course Schedule II
```python
def find_order(num_courses, prerequisites):
    """
    Tìm thứ tự hoàn thành khóa học
    """
    # Tạo adjacency list
    graph = defaultdict(list)
    in_degree = [0] * num_courses
    
    # Xây dựng graph và tính in-degree
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # BFS với queue
    queue = deque()
    for i in range(num_courses):
        if in_degree[i] == 0:
            queue.append(i)
    
    result = []
    while queue:
        course = queue.popleft()
        result.append(course)
        
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
    
    return result if len(result) == num_courses else []
```

**Độ khó**: ⭐⭐  
**Thời gian**: O(V + E)  
**Không gian**: O(V + E)

---

## 📚 **LEVEL 3: Alien Dictionary**
**Mục tiêu**: Tìm thứ tự bảng chữ cái từ từ điển ngoài hành tinh

### Bài toán: Alien Dictionary
```python
def alien_order(words):
    """
    Tìm thứ tự bảng chữ cái từ từ điển ngoài hành tinh
    """
    # Tạo adjacency list
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    
    # Khởi tạo in-degree cho tất cả ký tự
    for word in words:
        for char in word:
            in_degree[char] = 0
    
    # Xây dựng graph
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        
        # Tìm ký tự khác nhau đầu tiên
        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                break
        else:
            # Kiểm tra prefix
            if len(word1) > len(word2):
                return ""
    
    # BFS với queue
    queue = deque()
    for char in in_degree:
        if in_degree[char] == 0:
            queue.append(char)
    
    result = []
    while queue:
        char = queue.popleft()
        result.append(char)
        
        for next_char in graph[char]:
            in_degree[next_char] -= 1
            if in_degree[next_char] == 0:
                queue.append(next_char)
    
    return ''.join(result) if len(result) == len(in_degree) else ""
```

**Độ khó**: ⭐⭐⭐  
**Thời gian**: O(V + E)  
**Không gian**: O(V + E)

---

## 📚 **LEVEL 4: Minimum Height Trees**
**Mục tiêu**: Tìm gốc cây có chiều cao tối thiểu

### Bài toán: Minimum Height Trees
```python
def find_min_height_trees(n, edges):
    """
    Tìm gốc cây có chiều cao tối thiểu
    """
    if n == 1:
        return [0]
    
    # Tạo adjacency list
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    
    # Tìm leaves (nodes có degree = 1)
    leaves = []
    for i in range(n):
        if len(graph[i]) == 1:
            leaves.append(i)
    
    # Loại bỏ leaves từng lớp
    remaining_nodes = n
    while remaining_nodes > 2:
        remaining_nodes -= len(leaves)
        new_leaves = []
        
        for leaf in leaves:
            neighbor = list(graph[leaf])[0]
            graph[neighbor].remove(leaf)
            
            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)
        
        leaves = new_leaves
    
    return leaves
```

**Độ khó**: ⭐⭐⭐⭐  
**Thời gian**: O(V + E)  
**Không gian**: O(V + E)

---

## 📚 **LEVEL 5: Sequence Reconstruction**
**Mục tiêu**: Kiểm tra xem sequence có thể tái tạo từ subsequences không

### Bài toán: Sequence Reconstruction
```python
def sequence_reconstruction(org, seqs):
    """
    Kiểm tra xem sequence có thể tái tạo từ subsequences không
    """
    if not seqs:
        return False
    
    # Tạo graph
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    
    # Khởi tạo in-degree
    for seq in seqs:
        for num in seq:
            in_degree[num] = 0
    
    # Xây dựng graph
    for seq in seqs:
        for i in range(len(seq) - 1):
            if seq[i + 1] not in graph[seq[i]]:
                graph[seq[i]].add(seq[i + 1])
                in_degree[seq[i + 1]] += 1
    
    # BFS với queue
    queue = deque()
    for num in in_degree:
        if in_degree[num] == 0:
            queue.append(num)
    
    result = []
    while queue:
        if len(queue) > 1:
            return False  # Không unique
        
        num = queue.popleft()
        result.append(num)
        
        for next_num in graph[num]:
            in_degree[next_num] -= 1
            if in_degree[next_num] == 0:
                queue.append(next_num)
    
    return result == org
```

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(V + E)  
**Không gian**: O(V + E)

---

## 📚 **LEVEL 6: Course Schedule III**
**Mục tiêu**: Lập lịch khóa học với thời gian

### Bài toán: Course Schedule III
```python
import heapq

def schedule_course(courses):
    """
    Lập lịch khóa học với thời gian
    """
    # Sắp xếp theo deadline
    courses.sort(key=lambda x: x[1])
    
    # Sử dụng max heap để lưu duration
    heap = []
    current_time = 0
    
    for duration, deadline in courses:
        current_time += duration
        heapq.heappush(heap, -duration)
        
        # Nếu vượt deadline, loại bỏ khóa học dài nhất
        if current_time > deadline:
            current_time += heapq.heappop(heap)
    
    return len(heap)
```

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(n log n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 7: Parallel Courses**
**Mục tiêu**: Tìm số semester tối thiểu để hoàn thành khóa học

### Bài toán: Parallel Courses
```python
def minimum_semesters(n, relations):
    """
    Tìm số semester tối thiểu để hoàn thành khóa học
    """
    # Tạo graph
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    # Xây dựng graph
    for prev, next_course in relations:
        graph[prev].append(next_course)
        in_degree[next_course] += 1
    
    # BFS với queue
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    semesters = 0
    completed = 0
    
    while queue:
        semesters += 1
        level_size = len(queue)
        
        for _ in range(level_size):
            course = queue.popleft()
            completed += 1
            
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
    
    return semesters if completed == n else -1
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(V + E)  
**Không gian**: O(V + E)

---

## 📚 **LEVEL 8: Build a Matrix With Conditions**
**Mục tiêu**: Xây dựng ma trận với điều kiện

### Bài toán: Build a Matrix With Conditions
```python
def build_matrix(k, row_conditions, col_conditions):
    """
    Xây dựng ma trận với điều kiện
    """
    def topological_sort(conditions, n):
        # Tạo graph
        graph = defaultdict(list)
        in_degree = [0] * n
        
        for a, b in conditions:
            graph[a - 1].append(b - 1)
            in_degree[b - 1] += 1
        
        # BFS
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for next_node in graph[node]:
                in_degree[next_node] -= 1
                if in_degree[next_node] == 0:
                    queue.append(next_node)
        
        return result if len(result) == n else None
    
    # Topological sort cho rows và columns
    row_order = topological_sort(row_conditions, k)
    col_order = topological_sort(col_conditions, k)
    
    if not row_order or not col_order:
        return []
    
    # Xây dựng ma trận
    matrix = [[0] * k for _ in range(k)]
    for i, num in enumerate(row_order):
        for j, col_num in enumerate(col_order):
            if num == col_num:
                matrix[i][j] = num + 1
    
    return matrix
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(k²)  
**Không gian**: O(k²)

---

## 📚 **LEVEL 9: Topological Sort with DFS**
**Mục tiêu**: Sử dụng DFS để thực hiện topological sort

### Bài toán: Topological Sort with DFS
```python
def topological_sort_dfs(graph):
    """
    Topological sort sử dụng DFS
    """
    def dfs(node):
        if node in visiting:
            return False  # Cycle detected
        if node in visited:
            return True
        
        visiting.add(node)
        
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        
        visiting.remove(node)
        visited.add(node)
        result.append(node)
        return True
    
    visiting = set()
    visited = set()
    result = []
    
    for node in graph:
        if node not in visited:
            if not dfs(node):
                return []  # Cycle detected
    
    return result[::-1]
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(V + E)  
**Không gian**: O(V + E)

---

## 📚 **LEVEL 10: Advanced Topological Sort Applications**
**Mục tiêu**: Ứng dụng topological sort trong bài toán phức tạp

### Bài toán: Longest Increasing Path in a Matrix
```python
def longest_increasing_path(matrix):
    """
    Tìm đường đi tăng dài nhất trong ma trận
    """
    if not matrix or not matrix[0]:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    memo = {}
    
    def dfs(row, col, prev_val):
        if (row < 0 or row >= rows or col < 0 or col >= cols or 
            matrix[row][col] <= prev_val):
            return 0
        
        if (row, col) in memo:
            return memo[(row, col)]
        
        # Thử 4 hướng
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_path = 0
        
        for dr, dc in directions:
            max_path = max(max_path, dfs(row + dr, col + dc, matrix[row][col]))
        
        memo[(row, col)] = max_path + 1
        return memo[(row, col)]
    
    max_length = 0
    for row in range(rows):
        for col in range(cols):
            max_length = max(max_length, dfs(row, col, float('-inf')))
    
    return max_length
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(V + E)  
**Không gian**: O(V + E)

---

## 🎯 **Lộ trình học tập**

### **Giai đoạn 1 (Level 1-3)**: Nền tảng
- Hiểu khái niệm topological sort
- Thành thạo BFS approach
- Làm quen với pattern cơ bản

### **Giai đoạn 2 (Level 4-6)**: Nâng cao
- Alien dictionary
- Minimum height trees
- Sequence reconstruction

### **Giai đoạn 3 (Level 7-8)**: Chuyên sâu
- Course scheduling
- Matrix problems
- DFS approach

### **Giai đoạn 4 (Level 9-10)**: Master
- Advanced applications
- Complex constraints
- Edge cases phức tạp

## 💡 **Mẹo cho từng level**

- **Level 1-3**: Tập trung vào hiểu pattern cơ bản
- **Level 4-6**: Chú ý đến việc xử lý cycles
- **Level 7-8**: Hiểu sâu về ứng dụng trong scheduling
- **Level 9-10**: Thực hành nhiều và phân tích các trường hợp đặc biệt

## 🔥 **Common Patterns**

### **Basic Topological Sort**
```python
# Tạo graph và in-degree
graph = defaultdict(list)
in_degree = [0] * n

# BFS với queue
queue = deque()
for i in range(n):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()
    # Process node
    for neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)
```

### **DFS Topological Sort**
```python
def dfs(node):
    if node in visiting:
        return False  # Cycle
    if node in visited:
        return True
    
    visiting.add(node)
    for neighbor in graph[node]:
        if not dfs(neighbor):
            return False
    
    visiting.remove(node)
    visited.add(node)
    result.append(node)
    return True
```

### **Cycle Detection**
```python
def has_cycle(graph):
    visiting = set()
    visited = set()
    
    def dfs(node):
        if node in visiting:
            return True
        if node in visited:
            return False
        
        visiting.add(node)
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        
        visiting.remove(node)
        visited.add(node)
        return False
    
    for node in graph:
        if dfs(node):
            return True
    return False
``` 