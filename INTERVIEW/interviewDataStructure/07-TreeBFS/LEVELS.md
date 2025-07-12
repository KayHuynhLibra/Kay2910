# TREE BFS - 10 LEVELS TỪ CƠ BẢN ĐẾN NÂNG CAO

## 🎯 Tổng quan
10 level này được thiết kế để bạn học Tree BFS từ cơ bản đến nâng cao.

---

## 📚 **LEVEL 1: Hiểu cơ bản về Tree BFS**
**Mục tiêu**: Hiểu khái niệm và cách hoạt động của BFS

### Bài toán: Binary Tree Level Order Traversal
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    """
    Duyệt cây theo từng tầng
    """
    if not root:
        return []
    
    result = []
    queue = [root]
    
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

**Độ khó**: ⭐  
**Thời gian**: O(n)  
**Không gian**: O(w) - w là chiều rộng cây

---

## 📚 **LEVEL 2: Level Order Traversal II**
**Mục tiêu**: Duyệt từ dưới lên trên

### Bài toán: Binary Tree Level Order Traversal II
```python
def level_order_bottom(root):
    """
    Duyệt cây từ dưới lên trên
    """
    if not root:
        return []
    
    result = []
    queue = [root]
    
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
        
        result.insert(0, level)  # Chèn vào đầu
    
    return result
```

**Độ khó**: ⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(w)

---

## 📚 **LEVEL 3: Zigzag Level Order Traversal**
**Mục tiêu**: Duyệt theo pattern zigzag

### Bài toán: Binary Tree Zigzag Level Order Traversal
```python
def zigzag_level_order(root):
    """
    Duyệt cây theo pattern zigzag
    """
    if not root:
        return []
    
    result = []
    queue = [root]
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.pop(0)
            
            if left_to_right:
                level.append(node.val)
            else:
                level.insert(0, node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
        left_to_right = not left_to_right
    
    return result
```

**Độ khó**: ⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(w)

---

## 📚 **LEVEL 4: Average of Levels in Binary Tree**
**Mục tiêu**: Tính trung bình của mỗi tầng

### Bài toán: Average of Levels in Binary Tree
```python
def average_of_levels(root):
    """
    Tính trung bình của mỗi tầng
    """
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        level_sum = 0
        
        for _ in range(level_size):
            node = queue.pop(0)
            level_sum += node.val
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level_sum / level_size)
    
    return result
```

**Độ khó**: ⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(w)

---

## 📚 **LEVEL 5: Find Largest Value in Each Tree Row**
**Mục tiêu**: Tìm giá trị lớn nhất của mỗi tầng

### Bài toán: Find Largest Value in Each Tree Row
```python
def largest_values(root):
    """
    Tìm giá trị lớn nhất của mỗi tầng
    """
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        max_val = float('-inf')
        
        for _ in range(level_size):
            node = queue.pop(0)
            max_val = max(max_val, node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(max_val)
    
    return result
```

**Độ khó**: ⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(w)

---

## 📚 **LEVEL 6: Populating Next Right Pointers**
**Mục tiêu**: Kết nối các node cùng tầng

### Bài toán: Populating Next Right Pointers in Each Node
```python
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    """
    Kết nối các node cùng tầng
    """
    if not root:
        return root
    
    queue = [root]
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.pop(0)
            
            # Kết nối với node tiếp theo trong cùng tầng
            if i < level_size - 1:
                node.next = queue[0]
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return root
```

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(w)

---

## 📚 **LEVEL 7: Binary Tree Right Side View**
**Mục tiêu**: Tìm view từ bên phải

### Bài toán: Binary Tree Right Side View
```python
def right_side_view(root):
    """
    Tìm view từ bên phải của cây
    """
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.pop(0)
            
            # Node cuối cùng của mỗi tầng
            if i == level_size - 1:
                result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(w)

---

## 📚 **LEVEL 8: Minimum Depth of Binary Tree**
**Mục tiêu**: Tìm độ sâu tối thiểu

### Bài toán: Minimum Depth of Binary Tree
```python
def min_depth(root):
    """
    Tìm độ sâu tối thiểu của cây
    """
    if not root:
        return 0
    
    queue = [(root, 1)]
    
    while queue:
        node, depth = queue.pop(0)
        
        # Nếu là lá
        if not node.left and not node.right:
            return depth
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return 0
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(w)

---

## 📚 **LEVEL 9: Maximum Width of Binary Tree**
**Mục tiêu**: Tìm chiều rộng tối đa

### Bài toán: Maximum Width of Binary Tree
```python
def width_of_binary_tree(root):
    """
    Tìm chiều rộng tối đa của cây
    """
    if not root:
        return 0
    
    queue = [(root, 0, 0)]  # (node, depth, position)
    current_depth = 0
    left = 0
    max_width = 0
    
    while queue:
        node, depth, position = queue.pop(0)
        
        if depth != current_depth:
            current_depth = depth
            left = position
        
        max_width = max(max_width, position - left + 1)
        
        if node.left:
            queue.append((node.left, depth + 1, 2 * position))
        if node.right:
            queue.append((node.right, depth + 1, 2 * position + 1))
    
    return max_width
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(w)

---

## 📚 **LEVEL 10: Advanced BFS Applications**
**Mục tiêu**: Ứng dụng BFS trong bài toán phức tạp

### Bài toán: All Nodes Distance K in Binary Tree
```python
def distance_k(root, target, k):
    """
    Tìm tất cả node cách target k bước
    """
    def build_parent_map(node, parent):
        if not node:
            return
        parent_map[node] = parent
        build_parent_map(node.left, node)
        build_parent_map(node.right, node)
    
    def bfs_from_target(target, k):
        queue = [(target, 0)]
        visited = {target}
        result = []
        
        while queue:
            node, distance = queue.pop(0)
            
            if distance == k:
                result.append(node.val)
            elif distance < k:
                # Thêm các node lân cận
                for neighbor in [node.left, node.right, parent_map.get(node)]:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, distance + 1))
        
        return result
    
    parent_map = {}
    build_parent_map(root, None)
    return bfs_from_target(target, k)
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(n)

---

## 🎯 **Lộ trình học tập**

### **Giai đoạn 1 (Level 1-3)**: Nền tảng
- Hiểu khái niệm BFS
- Thành thạo level order traversal
- Làm quen với pattern cơ bản

### **Giai đoạn 2 (Level 4-6)**: Nâng cao
- Tính toán trên từng tầng
- Kết nối các node
- Tối ưu hóa thuật toán

### **Giai đoạn 3 (Level 7-8)**: Chuyên sâu
- Tìm view và độ sâu
- Xử lý bài toán phức tạp
- Tối ưu hóa bộ nhớ

### **Giai đoạn 4 (Level 9-10)**: Master
- Ứng dụng cao cấp
- Kết hợp nhiều kỹ thuật
- Edge cases phức tạp

## 💡 **Mẹo cho từng level**

- **Level 1-3**: Tập trung vào hiểu pattern cơ bản
- **Level 4-6**: Chú ý đến việc xử lý từng tầng
- **Level 7-8**: Hiểu sâu về ứng dụng trong cây
- **Level 9-10**: Thực hành nhiều và phân tích các trường hợp đặc biệt

## 🔥 **Common Patterns**

### **Basic BFS**
```python
queue = [root]
while queue:
    level_size = len(queue)
    for _ in range(level_size):
        node = queue.pop(0)
        # Process node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

### **Level Processing**
```python
level = []
for _ in range(level_size):
    node = queue.pop(0)
    level.append(node.val)
    # Add children
result.append(level)
```

### **BFS with Distance**
```python
queue = [(root, 0)]
while queue:
    node, distance = queue.pop(0)
    if distance == target:
        # Process
    # Add children with distance + 1
``` 