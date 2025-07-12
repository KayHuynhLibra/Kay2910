# TREE DFS - 10 LEVELS TỪ CƠ BẢN ĐẾN NÂNG CAO

## 🎯 Tổng quan
10 level này được thiết kế để bạn học Tree DFS từ cơ bản đến nâng cao.

---

## 📚 **LEVEL 1: Hiểu cơ bản về Tree DFS**
**Mục tiêu**: Hiểu khái niệm và cách hoạt động của DFS

### Bài toán: Binary Tree Inorder Traversal
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    """
    Duyệt cây theo thứ tự trung tố (Inorder)
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    
    dfs(root)
    return result
```

**Độ khó**: ⭐  
**Thời gian**: O(n)  
**Không gian**: O(h) - h là chiều cao cây

---

## 📚 **LEVEL 2: Preorder và Postorder Traversal**
**Mục tiêu**: Thành thạo các thứ tự duyệt khác nhau

### Bài toán: Preorder và Postorder Traversal
```python
def preorder_traversal(root):
    """
    Duyệt cây theo thứ tự tiền tố (Preorder)
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return result

def postorder_traversal(root):
    """
    Duyệt cây theo thứ tự hậu tố (Postorder)
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)
    
    dfs(root)
    return result
```

**Độ khó**: ⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(h)

---

## 📚 **LEVEL 3: Maximum Depth of Binary Tree**
**Mục tiêu**: Tìm độ sâu tối đa của cây

### Bài toán: Maximum Depth of Binary Tree
```python
def max_depth(root):
    """
    Tìm độ sâu tối đa của cây
    """
    if not root:
        return 0
    
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    return max(left_depth, right_depth) + 1
```

**Độ khó**: ⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(h)

---

## 📚 **LEVEL 4: Path Sum**
**Mục tiêu**: Kiểm tra tổng đường đi

### Bài toán: Path Sum
```python
def has_path_sum(root, target_sum):
    """
    Kiểm tra xem có đường đi nào có tổng bằng target_sum không
    """
    if not root:
        return False
    
    if not root.left and not root.right:
        return target_sum == root.val
    
    remaining_sum = target_sum - root.val
    return has_path_sum(root.left, remaining_sum) or has_path_sum(root.right, remaining_sum)
```

**Độ khó**: ⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(h)

---

## 📚 **LEVEL 5: Path Sum II**
**Mục tiêu**: Tìm tất cả đường đi có tổng bằng target

### Bài toán: Path Sum II
```python
def path_sum(root, target_sum):
    """
    Tìm tất cả đường đi có tổng bằng target_sum
    """
    result = []
    
    def dfs(node, current_sum, path):
        if not node:
            return
        
        current_sum += node.val
        path.append(node.val)
        
        if not node.left and not node.right and current_sum == target_sum:
            result.append(path[:])
        
        dfs(node.left, current_sum, path)
        dfs(node.right, current_sum, path)
        
        path.pop()  # Backtrack
    
    dfs(root, 0, [])
    return result
```

**Độ khó**: ⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(h)

---

## 📚 **LEVEL 6: Binary Tree Paths**
**Mục tiêu**: Tìm tất cả đường đi từ gốc đến lá

### Bài toán: Binary Tree Paths
```python
def binary_tree_paths(root):
    """
    Tìm tất cả đường đi từ gốc đến lá
    """
    result = []
    
    def dfs(node, path):
        if not node:
            return
        
        path.append(str(node.val))
        
        if not node.left and not node.right:
            result.append("->".join(path))
        else:
            dfs(node.left, path)
            dfs(node.right, path)
        
        path.pop()  # Backtrack
    
    dfs(root, [])
    return result
```

**Độ khó**: ⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(h)

---

## 📚 **LEVEL 7: Sum Root to Leaf Numbers**
**Mục tiêu**: Tính tổng tất cả số từ gốc đến lá

### Bài toán: Sum Root to Leaf Numbers
```python
def sum_numbers(root):
    """
    Tính tổng tất cả số từ gốc đến lá
    """
    total_sum = 0
    
    def dfs(node, current_sum):
        nonlocal total_sum
        
        if not node:
            return
        
        current_sum = current_sum * 10 + node.val
        
        if not node.left and not node.right:
            total_sum += current_sum
        else:
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
    
    dfs(root, 0)
    return total_sum
```

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(h)

---

## 📚 **LEVEL 8: Validate Binary Search Tree**
**Mục tiêu**: Kiểm tra xem cây có phải BST không

### Bài toán: Validate Binary Search Tree
```python
def is_valid_bst(root):
    """
    Kiểm tra xem cây có phải BST không
    """
    def dfs(node, lower, upper):
        if not node:
            return True
        
        if node.val <= lower or node.val >= upper:
            return False
        
        return (dfs(node.left, lower, node.val) and 
                dfs(node.right, node.val, upper))
    
    return dfs(root, float('-inf'), float('inf'))
```

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(h)

---

## 📚 **LEVEL 9: Flatten Binary Tree to Linked List**
**Mục tiêu**: Biến đổi cây thành linked list

### Bài toán: Flatten Binary Tree to Linked List
```python
def flatten(root):
    """
    Biến đổi cây thành linked list
    """
    def dfs(node):
        if not node:
            return None
        
        if not node.left and not node.right:
            return node
        
        left_tail = dfs(node.left)
        right_tail = dfs(node.right)
        
        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None
        
        return right_tail if right_tail else left_tail
    
    dfs(root)
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(h)

---

## 📚 **LEVEL 10: Advanced DFS Applications**
**Mục tiêu**: Ứng dụng DFS trong bài toán phức tạp

### Bài toán: Serialize and Deserialize Binary Tree
```python
def serialize(root):
    """
    Chuyển cây thành chuỗi
    """
    if not root:
        return "null"
    
    return str(root.val) + "," + serialize(root.left) + "," + serialize(root.right)

def deserialize(data):
    """
    Chuyển chuỗi thành cây
    """
    def dfs(values):
        if not values or values[0] == "null":
            values.pop(0)
            return None
        
        root = TreeNode(int(values[0]))
        values.pop(0)
        root.left = dfs(values)
        root.right = dfs(values)
        return root
    
    values = data.split(",")
    return dfs(values)
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(n)

---

## 🎯 **Lộ trình học tập**

### **Giai đoạn 1 (Level 1-3)**: Nền tảng
- Hiểu khái niệm DFS
- Thành thạo các thứ tự duyệt
- Làm quen với pattern cơ bản

### **Giai đoạn 2 (Level 4-6)**: Nâng cao
- Xử lý đường đi và tổng
- Backtracking
- Tối ưu hóa thuật toán

### **Giai đoạn 3 (Level 7-8)**: Chuyên sâu
- BST validation
- Tree transformation
- Tối ưu hóa bộ nhớ

### **Giai đoạn 4 (Level 9-10)**: Master
- Ứng dụng cao cấp
- Serialization
- Edge cases phức tạp

## 💡 **Mẹo cho từng level**

- **Level 1-3**: Tập trung vào hiểu pattern cơ bản
- **Level 4-6**: Chú ý đến backtracking và path processing
- **Level 7-8**: Hiểu sâu về BST và tree transformation
- **Level 9-10**: Thực hành nhiều và phân tích các trường hợp đặc biệt

## 🔥 **Common Patterns**

### **Basic DFS**
```python
def dfs(node):
    if not node:
        return
    # Process current node
    dfs(node.left)
    dfs(node.right)
```

### **DFS with Backtracking**
```python
def dfs(node, path):
    if not node:
        return
    
    path.append(node.val)
    # Process
    dfs(node.left, path)
    dfs(node.right, path)
    path.pop()  # Backtrack
```

### **DFS with State**
```python
def dfs(node, state):
    if not node:
        return state
    
    # Update state
    new_state = process(node, state)
    
    left_state = dfs(node.left, new_state)
    right_state = dfs(node.right, new_state)
    
    return combine(left_state, right_state)
``` 