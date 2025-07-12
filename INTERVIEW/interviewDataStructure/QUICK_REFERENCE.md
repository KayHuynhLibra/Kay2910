# QUICK REFERENCE - 14 PHƯƠNG PHÁP GIẢI THUẬT

## 🚀 Khi nào sử dụng từng phương pháp

### **Sliding Window** 📊
- **Khi nào**: Cần thao tác trên khoảng cố định của mảng/chuỗi
- **Ví dụ**: Tìm dãy con dài nhất, substring problems
- **Pattern**: `left = 0, right = 0; while(right < n) { ... }`

### **Two Pointers** 👆👆
- **Khi nào**: So sánh phần tử trong mảng đã sắp xếp
- **Ví dụ**: Two Sum, Remove Duplicates
- **Pattern**: `left = 0, right = n-1; while(left < right) { ... }`

### **Fast & Slow Pointers** 🐰🐢
- **Khi nào**: Phát hiện chu kỳ, tìm điểm giữa
- **Ví dụ**: Linked List Cycle, Find Middle
- **Pattern**: `slow = head, fast = head; while(fast && fast.next) { ... }`

### **Merge Intervals** 📅
- **Khi nào**: Xử lý khoảng thời gian chồng lấn
- **Ví dụ**: Meeting Rooms, Calendar
- **Pattern**: `sort(intervals); for interval in intervals: { ... }`

### **Cyclic Sort** 🔄
- **Khi nào**: Mảng chứa số trong phạm vi [1, n]
- **Ví dụ**: Find Missing Number, Find Duplicate
- **Pattern**: `for i in range(n): while(nums[i] != i+1): { ... }`

### **In-Place Reversal** ↩️
- **Khi nào**: Đảo ngược danh sách liên kết
- **Ví dụ**: Reverse Linked List, Palindrome
- **Pattern**: `prev = None, curr = head; while(curr): { ... }`

### **Tree BFS** 🌳➡️
- **Khi nào**: Duyệt cây theo từng tầng
- **Ví dụ**: Level Order Traversal, Shortest Path
- **Pattern**: `queue = [root]; while queue: { ... }`

### **Tree DFS** 🌳⬇️
- **Khi nào**: Duyệt cây theo chiều sâu
- **Ví dụ**: Path Sum, Tree Traversal
- **Pattern**: `def dfs(node): if not node: return; ...`

### **Two Heaps** ⚖️
- **Khi nào**: Cần median hoặc top-k elements
- **Ví dụ**: Find Median, Top K Frequent
- **Pattern**: `max_heap = [], min_heap = []`

### **Subsets** 📦
- **Khi nào**: Tạo tất cả tập con có thể
- **Ví dụ**: Subsets, Permutations
- **Pattern**: `def backtrack(start, path): { ... }`

### **Binary Search** 🔍
- **Khi nào**: Tìm kiếm trong dữ liệu đã sắp xếp
- **Ví dụ**: Search Insert Position, Find Peak
- **Pattern**: `left, right = 0, n-1; while(left <= right): { ... }`

### **Top K Elements** 🏆
- **Khi nào**: Tìm k phần tử lớn nhất/nhỏ nhất
- **Ví dụ**: Top K Frequent, Kth Largest
- **Pattern**: `heap = []; for num in nums: heapq.heappush(heap, num)`

### **K-Way Merge** 🔗
- **Khi nào**: Hợp nhất nhiều mảng đã sắp xếp
- **Ví dụ**: Merge K Sorted Lists
- **Pattern**: `heap = []; for list in lists: heapq.heappush(heap, (val, list))`

### **Topological Sort** 📋
- **Khi nào**: Sắp xếp theo thứ tự phụ thuộc
- **Ví dụ**: Course Schedule, Build Order
- **Pattern**: `indegree = [0]*n; queue = [i for i in range(n) if indegree[i] == 0]`

## 🎯 Decision Tree - Chọn phương pháp

```
Bài toán có dữ liệu gì?
├── Mảng/Chuỗi
│   ├── Cần thao tác trên khoảng? → Sliding Window
│   ├── Đã sắp xếp? → Two Pointers
│   ├── Cần tìm kiếm? → Binary Search
│   └── Cần tạo tổ hợp? → Subsets
├── Danh sách liên kết
│   ├── Phát hiện chu kỳ? → Fast/Slow Pointers
│   └── Đảo ngược? → In-Place Reversal
├── Cây
│   ├── Theo tầng? → BFS
│   └── Theo chiều sâu? → DFS
├── Khoảng thời gian
│   └── Chồng lấn? → Merge Intervals
├── Số trong phạm vi [1,n]
│   └── Thiếu/Trùng? → Cyclic Sort
├── Cần median/top-k
│   └── → Two Heaps
├── Nhiều mảng đã sắp xếp
│   └── → K-Way Merge
└── Có phụ thuộc
    └── → Topological Sort
```

## ⚡ Template Code

### Sliding Window
```python
def sliding_window_template(arr, k):
    left = 0
    result = []
    for right in range(len(arr)):
        # Mở rộng cửa sổ
        while condition:  # Thu nhỏ cửa sổ
            left += 1
        # Cập nhật kết quả
    return result
```

### Two Pointers
```python
def two_pointers_template(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if condition:
            left += 1
        else:
            right -= 1
    return result
```

### Binary Search
```python
def binary_search_template(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### DFS Template
```python
def dfs_template(node):
    if not node:
        return
    
    # Process current node
    dfs_template(node.left)
    dfs_template(node.right)
```

### BFS Template
```python
def bfs_template(root):
    if not root:
        return []
    
    queue = [root]
    result = []
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.pop(0)
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

## 🔥 Common Patterns

### **Array/String Problems**
1. **Subarray/Substring**: Sliding Window
2. **Two Sum**: Two Pointers (if sorted) or HashMap
3. **Search**: Binary Search
4. **Combination**: Subsets/Backtracking

### **Linked List Problems**
1. **Cycle Detection**: Fast/Slow Pointers
2. **Reverse**: In-Place Reversal
3. **Middle Node**: Fast/Slow Pointers
4. **Merge**: Two Pointers

### **Tree Problems**
1. **Level Order**: BFS
2. **Path Problems**: DFS
3. **BST Operations**: DFS with BST properties

### **Graph Problems**
1. **Shortest Path**: BFS
2. **Connected Components**: DFS
3. **Dependencies**: Topological Sort

## 💡 Pro Tips

1. **Always consider edge cases**: Empty input, single element, duplicates
2. **Think about space complexity**: Can you do it in-place?
3. **Consider multiple approaches**: Brute force first, then optimize
4. **Use the right data structure**: HashMap, Heap, Stack, Queue
5. **Practice pattern recognition**: Similar problems often use similar approaches

## 📚 Study Order

1. **Beginner**: Two Pointers → Sliding Window → Binary Search
2. **Intermediate**: Fast/Slow → BFS/DFS → Merge Intervals
3. **Advanced**: Two Heaps → Topological Sort → K-Way Merge
4. **Expert**: Cyclic Sort → In-Place Reversal → Subsets 