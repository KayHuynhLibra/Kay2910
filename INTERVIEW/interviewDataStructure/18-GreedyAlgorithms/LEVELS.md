# GREEDY ALGORITHMS - 20 LEVELS TỪ CƠ BẢN ĐẾN NÂNG CAO

## 🎯 Tổng quan
20 level này được thiết kế để bạn học Greedy Algorithms từ cơ bản đến nâng cao.

---

## 📚 **LEVEL 1: Hiểu cơ bản về Greedy**
**Mục tiêu**: Hiểu khái niệm và nguyên lý greedy

### Bài toán: Activity Selection
```python
def activity_selection(start, finish):
    """
    Chọn số hoạt động tối đa có thể thực hiện
    """
    n = len(start)
    activities = []
    
    # Sort activities by finish time
    sorted_activities = sorted(zip(start, finish), key=lambda x: x[1])
    
    # Select first activity
    activities.append(0)
    last_finish = sorted_activities[0][1]
    
    # Select remaining activities
    for i in range(1, n):
        if sorted_activities[i][0] >= last_finish:
            activities.append(i)
            last_finish = sorted_activities[i][1]
    
    return activities
```

**Độ khó**: ⭐  
**Thời gian**: O(n log n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 2: Fractional Knapsack**
**Mục tiêu**: Bài toán cái túi phân số

### Bài toán: Fractional Knapsack
```python
def fractional_knapsack(weights, values, capacity):
    """
    Bài toán cái túi phân số
    """
    n = len(weights)
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    items.sort(reverse=True)  # Sort by value per weight
    
    total_value = 0
    remaining_capacity = capacity
    
    for value_per_weight, weight, value in items:
        if remaining_capacity >= weight:
            total_value += value
            remaining_capacity -= weight
        else:
            total_value += value_per_weight * remaining_capacity
            break
    
    return total_value
```

**Độ khó**: ⭐⭐  
**Thời gian**: O(n log n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 3: Job Scheduling**
**Mục tiêu**: Lập lịch công việc với deadline

### Bài toán: Job Scheduling
```python
def job_scheduling(jobs):
    """
    Lập lịch công việc với deadline
    """
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    n = len(jobs)
    result = [False] * n
    slot = [-1] * n
    
    for i in range(n):
        # Find a free slot for this job
        for j in range(min(jobs[i][1] - 1, n - 1), -1, -1):
            if slot[j] == -1:
                slot[j] = i
                result[i] = True
                break
    
    return [jobs[i] for i in range(n) if result[i]]
```

**Độ khó**: ⭐⭐⭐  
**Thời gian**: O(n²)  
**Không gian**: O(n)

---

## 📚 **LEVEL 4: Huffman Coding**
**Mục tiêu**: Thuật toán Huffman coding

### Bài toán: Huffman Coding
```python
import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(characters, frequencies):
    """
    Thuật toán Huffman coding
    """
    # Create leaf nodes
    heap = [HuffmanNode(char, freq) for char, freq in zip(characters, frequencies)]
    heapq.heapify(heap)
    
    # Build Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        internal = HuffmanNode(None, left.freq + right.freq)
        internal.left = left
        internal.right = right
        
        heapq.heappush(heap, internal)
    
    # Generate codes
    codes = {}
    
    def generate_codes(node, code=""):
        if node.char is not None:
            codes[node.char] = code
        else:
            generate_codes(node.left, code + "0")
            generate_codes(node.right, code + "1")
    
    if heap:
        generate_codes(heap[0])
    
    return codes
```

**Độ khó**: ⭐⭐⭐⭐  
**Thời gian**: O(n log n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 5: Minimum Spanning Tree - Kruskal**
**Mục tiêu**: Thuật toán Kruskal cho MST

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

def kruskal_mst(edges, n):
    """
    Thuật toán Kruskal cho MST
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

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(E log E)  
**Không gian**: O(V)

---

## 📚 **LEVEL 6: Minimum Spanning Tree - Prim**
**Mục tiêu**: Thuật toán Prim cho MST

### Bài toán: Prim's Algorithm
```python
import heapq

def prim_mst(graph, start):
    """
    Thuật toán Prim cho MST
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

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O((V + E) log V)  
**Không gian**: O(V)

---

## 📚 **LEVEL 7: Dijkstra's Algorithm**
**Mục tiêu**: Thuật toán Dijkstra cho shortest path

### Bài toán: Dijkstra's Algorithm
```python
import heapq

def dijkstra(graph, start):
    """
    Thuật toán Dijkstra cho shortest path
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

## 📚 **LEVEL 8: Coin Change (Greedy)**
**Mục tiêu**: Bài toán đổi tiền với greedy

### Bài toán: Coin Change Greedy
```python
def coin_change_greedy(coins, amount):
    """
    Bài toán đổi tiền với greedy (chỉ khi coins có tính chất greedy)
    """
    coins.sort(reverse=True)  # Sort in descending order
    result = []
    remaining = amount
    
    for coin in coins:
        while remaining >= coin:
            result.append(coin)
            remaining -= coin
    
    return result if remaining == 0 else None
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 9: Gas Station Problem**
**Mục tiêu**: Bài toán trạm xăng

### Bài toán: Gas Station Problem
```python
def can_complete_circuit(gas, cost):
    """
    Kiểm tra có thể hoàn thành vòng tròn không
    """
    n = len(gas)
    total_gas = 0
    current_gas = 0
    start_station = 0
    
    for i in range(n):
        total_gas += gas[i] - cost[i]
        current_gas += gas[i] - cost[i]
        
        if current_gas < 0:
            current_gas = 0
            start_station = i + 1
    
    return start_station if total_gas >= 0 else -1
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 10: Jump Game**
**Mục tiêu**: Bài toán nhảy game

### Bài toán: Jump Game
```python
def can_jump(nums):
    """
    Kiểm tra có thể nhảy đến cuối không
    """
    max_reach = 0
    
    for i in range(len(nums)):
        if i > max_reach:
            return False
        
        max_reach = max(max_reach, i + nums[i])
        
        if max_reach >= len(nums) - 1:
            return True
    
    return True

def min_jumps(nums):
    """
    Tìm số bước nhảy ít nhất
    """
    if len(nums) <= 1:
        return 0
    
    jumps = 1
    current_max = nums[0]
    next_max = nums[0]
    
    for i in range(1, len(nums)):
        if i > current_max:
            jumps += 1
            current_max = next_max
        
        next_max = max(next_max, i + nums[i])
    
    return jumps
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 11: Candy Distribution**
**Mục tiêu**: Phân phối kẹo

### Bài toán: Candy Distribution
```python
def candy(ratings):
    """
    Phân phối kẹo dựa trên rating
    """
    n = len(ratings)
    candies = [1] * n
    
    # Left to right pass
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    
    # Right to left pass
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    
    return sum(candies)
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 12: Task Scheduler**
**Mục tiêu**: Lập lịch tác vụ

### Bài toán: Task Scheduler
```python
def least_interval(tasks, n):
    """
    Tìm thời gian ít nhất để hoàn thành tất cả tasks
    """
    from collections import Counter
    
    # Count frequency of each task
    task_counts = Counter(tasks)
    max_freq = max(task_counts.values())
    
    # Count tasks with max frequency
    max_freq_count = sum(1 for count in task_counts.values() if count == max_freq)
    
    # Calculate minimum intervals needed
    min_intervals = (max_freq - 1) * (n + 1) + max_freq_count
    
    return max(min_intervals, len(tasks))
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 13: Partition Labels**
**Mục tiêu**: Phân vùng nhãn

### Bài toán: Partition Labels
```python
def partition_labels(s):
    """
    Phân vùng string thành các phần có ký tự không lặp lại
    """
    # Find last occurrence of each character
    last_occurrence = {}
    for i, char in enumerate(s):
        last_occurrence[char] = i
    
    result = []
    start = end = 0
    
    for i, char in enumerate(s):
        end = max(end, last_occurrence[char])
        
        if i == end:
            result.append(end - start + 1)
            start = i + 1
    
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 14: Lemonade Change**
**Mục tiêu**: Bài toán đổi tiền bán chanh

### Bài toán: Lemonade Change
```python
def lemonade_change(bills):
    """
    Kiểm tra có thể đổi tiền cho tất cả khách hàng không
    """
    five = ten = 0
    
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1
        else:  # bill == 20
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    
    return True
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 15: Reorganize String**
**Mục tiêu**: Tái tổ chức string

### Bài toán: Reorganize String
```python
def reorganize_string(s):
    """
    Tái tổ chức string sao cho không có ký tự liền kề giống nhau
    """
    from collections import Counter
    import heapq
    
    # Count character frequencies
    char_count = Counter(s)
    
    # Create max heap
    heap = [(-count, char) for char, count in char_count.items()]
    heapq.heapify(heap)
    
    result = []
    prev_char = None
    
    while heap:
        count, char = heapq.heappop(heap)
        
        if prev_char == char:
            if not heap:
                return ""
            count2, char2 = heapq.heappop(heap)
            result.append(char2)
            prev_char = char2
            
            if count2 + 1 < 0:
                heapq.heappush(heap, (count2 + 1, char2))
            heapq.heappush(heap, (count, char))
        else:
            result.append(char)
            prev_char = char
            
            if count + 1 < 0:
                heapq.heappush(heap, (count + 1, char))
    
    return ''.join(result)
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n log n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 16: Minimum Cost to Connect Sticks**
**Mục tiêu**: Chi phí tối thiểu để nối que

### Bài toán: Minimum Cost to Connect Sticks
```python
def connect_sticks(sticks):
    """
    Tìm chi phí tối thiểu để nối tất cả que
    """
    import heapq
    
    if len(sticks) <= 1:
        return 0
    
    heapq.heapify(sticks)
    total_cost = 0
    
    while len(sticks) > 1:
        # Connect two shortest sticks
        stick1 = heapq.heappop(sticks)
        stick2 = heapq.heappop(sticks)
        
        cost = stick1 + stick2
        total_cost += cost
        
        heapq.heappush(sticks, cost)
    
    return total_cost
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n log n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 17: Meeting Rooms II**
**Mục tiêu**: Số phòng họp tối thiểu

### Bài toán: Meeting Rooms II
```python
def min_meeting_rooms(intervals):
    """
    Tìm số phòng họp tối thiểu
    """
    if not intervals:
        return 0
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    import heapq
    heap = []  # Store end times
    
    for start, end in intervals:
        if heap and start >= heap[0]:
            # Reuse room
            heapq.heappop(heap)
        heapq.heappush(heap, end)
    
    return len(heap)
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n log n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 18: Car Pooling**
**Mục tiêu**: Bài toán xe chở khách

### Bài toán: Car Pooling
```python
def car_pooling(trips, capacity):
    """
    Kiểm tra có thể chở tất cả khách không
    """
    # Create timeline of passenger changes
    timeline = []
    for passengers, start, end in trips:
        timeline.append((start, passengers))
        timeline.append((end, -passengers))
    
    # Sort by time
    timeline.sort()
    
    current_passengers = 0
    for time, change in timeline:
        current_passengers += change
        if current_passengers > capacity:
            return False
    
    return True
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n log n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 19: Advanced Greedy with Constraints**
**Mục tiêu**: Greedy với nhiều ràng buộc

### Bài toán: Advanced Greedy
```python
def advanced_greedy_with_constraints(items, capacity, constraints):
    """
    Greedy algorithm với nhiều ràng buộc
    """
    def calculate_priority(item):
        # Calculate priority based on multiple factors
        value, weight, category = item
        base_priority = value / weight
        
        # Apply constraints
        if category in constraints.get('forbidden_categories', []):
            return 0
        
        if weight > constraints.get('max_weight', float('inf')):
            return 0
        
        # Bonus for preferred categories
        if category in constraints.get('preferred_categories', []):
            base_priority *= 1.5
        
        return base_priority
    
    # Sort items by priority
    sorted_items = sorted(items, key=calculate_priority, reverse=True)
    
    selected_items = []
    remaining_capacity = capacity
    category_count = {}
    
    for item in sorted_items:
        value, weight, category = item
        
        # Check capacity constraint
        if weight > remaining_capacity:
            continue
        
        # Check category limit constraint
        max_per_category = constraints.get('max_per_category', float('inf'))
        if category_count.get(category, 0) >= max_per_category:
            continue
        
        # Check total items constraint
        max_total_items = constraints.get('max_total_items', float('inf'))
        if len(selected_items) >= max_total_items:
            break
        
        selected_items.append(item)
        remaining_capacity -= weight
        category_count[category] = category_count.get(category, 0) + 1
    
    return selected_items
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n log n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 20: Master Level - Complex Greedy Applications**
**Mục tiêu**: Ứng dụng greedy trong bài toán phức tạp nhất

### Bài toán: Master Greedy Algorithm
```python
def master_greedy_algorithm(problem_data, constraints, objectives):
    """
    Thuật toán greedy master với nhiều mục tiêu và ràng buộc phức tạp
    """
    def evaluate_solution(solution):
        # Evaluate solution based on multiple objectives
        total_score = 0
        
        for objective_name, objective_func in objectives.items():
            weight = objectives.get(f"{objective_name}_weight", 1.0)
            score = objective_func(solution)
            total_score += weight * score
        
        return total_score
    
    def is_feasible(solution, new_item):
        # Check if adding new_item maintains feasibility
        for constraint_name, constraint_func in constraints.items():
            if not constraint_func(solution + [new_item]):
                return False
        return True
    
    def greedy_construct():
        # Greedy construction with multiple criteria
        solution = []
        available_items = problem_data.copy()
        
        while available_items:
            best_item = None
            best_score = float('-inf')
            
            for item in available_items:
                if is_feasible(solution, item):
                    # Calculate marginal contribution
                    current_score = evaluate_solution(solution)
                    new_score = evaluate_solution(solution + [item])
                    marginal_score = new_score - current_score
                    
                    if marginal_score > best_score:
                        best_score = marginal_score
                        best_item = item
            
            if best_item is None:
                break
            
            solution.append(best_item)
            available_items.remove(best_item)
        
        return solution
    
    def local_search(solution):
        # Local search improvement
        improved = True
        while improved:
            improved = False
            
            for i in range(len(solution)):
                for j in range(i + 1, len(solution)):
                    # Try swapping items
                    new_solution = solution.copy()
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    
                    if (is_feasible(new_solution, []) and 
                        evaluate_solution(new_solution) > evaluate_solution(solution)):
                        solution = new_solution
                        improved = True
                        break
                if improved:
                    break
        
        return solution
    
    # Main algorithm
    initial_solution = greedy_construct()
    final_solution = local_search(initial_solution)
    
    return {
        'solution': final_solution,
        'score': evaluate_solution(final_solution),
        'feasible': is_feasible(final_solution, [])
    }
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n² * m) với m là số constraints  
**Không gian**: O(n)

---

## 🎯 **Lộ trình học tập**

### **Giai đoạn 1 (Level 1-5)**: Nền tảng
- Hiểu khái niệm greedy algorithms
- Thành thạo basic greedy problems
- Làm quen với pattern cơ bản

### **Giai đoạn 2 (Level 6-10)**: Nâng cao
- Advanced greedy algorithms
- Optimization problems
- Tối ưu hóa thuật toán

### **Giai đoạn 3 (Level 11-15)**: Chuyên sâu
- Complex greedy problems
- Multiple constraints
- Tối ưu hóa bộ nhớ

### **Giai đoạn 4 (Level 16-20)**: Master
- Advanced applications
- Multiple objectives
- Edge cases phức tạp

## 💡 **Mẹo cho từng level**

- **Level 1-5**: Tập trung vào hiểu pattern cơ bản
- **Level 6-10**: Chú ý đến việc chứng minh tính đúng đắn
- **Level 11-15**: Hiểu sâu về greedy theory
- **Level 16-20**: Thực hành nhiều và phân tích các trường hợp đặc biệt

## 🔥 **Common Patterns**

### **Sort and Select Pattern**
```python
def greedy_sort_select(items):
    items.sort(key=lambda x: x.priority, reverse=True)
    result = []
    for item in items:
        if is_feasible(result + [item]):
            result.append(item)
    return result
```

### **Heap-based Greedy Pattern**
```python
def greedy_heap(items):
    import heapq
    heap = []
    for item in items:
        heapq.heappush(heap, (item.priority, item))
    
    result = []
    while heap:
        priority, item = heapq.heappop(heap)
        if is_feasible(result + [item]):
            result.append(item)
    return result
```

### **Two-pointer Greedy Pattern**
```python
def greedy_two_pointers(array):
    left, right = 0, len(array) - 1
    result = 0
    
    while left < right:
        # Make greedy choice
        if array[left] < array[right]:
            result += array[left]
            left += 1
        else:
            result += array[right]
            right -= 1
    
    return result
``` 