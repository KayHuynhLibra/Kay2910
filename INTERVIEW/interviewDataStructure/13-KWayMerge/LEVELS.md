# K-WAY MERGE - 10 LEVELS TỪ CƠ BẢN ĐẾN NÂNG CAO

## 🎯 Tổng quan
10 level này được thiết kế để bạn học K-Way Merge từ cơ bản đến nâng cao.

---

## 📚 **LEVEL 1: Hiểu cơ bản về K-Way Merge**
**Mục tiêu**: Hiểu khái niệm và cách hoạt động

### Bài toán: Merge Two Sorted Lists
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    """
    Hợp nhất hai danh sách đã sắp xếp
    """
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # Thêm phần còn lại
    current.next = l1 if l1 else l2
    
    return dummy.next
```

**Độ khó**: ⭐  
**Thời gian**: O(n + m)  
**Không gian**: O(1)

---

## 📚 **LEVEL 2: Merge K Sorted Lists**
**Mục tiêu**: Hợp nhất k danh sách đã sắp xếp

### Bài toán: Merge k Sorted Lists
```python
import heapq

def merge_k_lists(lists):
    """
    Hợp nhất k danh sách đã sắp xếp
    """
    if not lists:
        return None
    
    # Sử dụng min heap
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))
    
    dummy = ListNode(0)
    current = dummy
    
    while heap:
        val, list_idx, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, list_idx, node.next))
    
    return dummy.next
```

**Độ khó**: ⭐⭐  
**Thời gian**: O(n log k)  
**Không gian**: O(k)

---

## 📚 **LEVEL 3: Merge K Sorted Arrays**
**Mục tiêu**: Hợp nhất k mảng đã sắp xếp

### Bài toán: Merge K Sorted Arrays
```python
def merge_k_arrays(arrays):
    """
    Hợp nhất k mảng đã sắp xếp
    """
    if not arrays:
        return []
    
    # Sử dụng min heap với (value, array_index, element_index)
    heap = []
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))
    
    result = []
    
    while heap:
        val, arr_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        # Thêm phần tử tiếp theo từ mảng này
        if elem_idx + 1 < len(arrays[arr_idx]):
            heapq.heappush(heap, (arrays[arr_idx][elem_idx + 1], arr_idx, elem_idx + 1))
    
    return result
```

**Độ khó**: ⭐⭐⭐  
**Thời gian**: O(n log k)  
**Không gian**: O(k)

---

## 📚 **LEVEL 4: Kth Smallest Element in Sorted Matrix**
**Mục tiêu**: Tìm phần tử nhỏ thứ k trong ma trận đã sắp xếp

### Bài toán: Kth Smallest Element in a Sorted Matrix
```python
def kth_smallest_matrix(matrix, k):
    """
    Tìm phần tử nhỏ thứ k trong ma trận đã sắp xếp
    """
    rows, cols = len(matrix), len(matrix[0])
    
    # Sử dụng min heap với (value, row, col)
    heap = [(matrix[0][0], 0, 0)]
    visited = {(0, 0)}
    
    for _ in range(k - 1):
        val, row, col = heapq.heappop(heap)
        
        # Thêm phần tử bên phải
        if col + 1 < cols and (row, col + 1) not in visited:
            heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
            visited.add((row, col + 1))
        
        # Thêm phần tử bên dưới
        if row + 1 < rows and (row + 1, col) not in visited:
            heapq.heappush(heap, (matrix[row + 1][col], row + 1, col))
            visited.add((row + 1, col))
    
    return heap[0][0]
```

**Độ khó**: ⭐⭐⭐⭐  
**Thời gian**: O(k log k)  
**Không gian**: O(k)

---

## 📚 **LEVEL 5: Find K Pairs with Smallest Sums**
**Mục tiêu**: Tìm k cặp có tổng nhỏ nhất

### Bài toán: Find K Pairs with Smallest Sums
```python
def k_smallest_pairs(nums1, nums2, k):
    """
    Tìm k cặp có tổng nhỏ nhất
    """
    if not nums1 or not nums2:
        return []
    
    # Sử dụng min heap với (sum, i, j)
    heap = [(nums1[0] + nums2[0], 0, 0)]
    visited = {(0, 0)}
    result = []
    
    while heap and len(result) < k:
        sum_val, i, j = heapq.heappop(heap)
        result.append([nums1[i], nums2[j]])
        
        # Thêm cặp tiếp theo từ nums1
        if i + 1 < len(nums1) and (i + 1, j) not in visited:
            heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            visited.add((i + 1, j))
        
        # Thêm cặp tiếp theo từ nums2
        if j + 1 < len(nums2) and (i, j + 1) not in visited:
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            visited.add((i, j + 1))
    
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(k log k)  
**Không gian**: O(k)

---

## 📚 **LEVEL 6: Merge K Sorted Lists (Divide and Conquer)**
**Mục tiêu**: Sử dụng divide and conquer để merge k lists

### Bài toán: Merge K Lists with Divide and Conquer
```python
def merge_k_lists_divide_conquer(lists):
    """
    Hợp nhất k danh sách sử dụng divide and conquer
    """
    if not lists:
        return None
    
    def merge_lists(lists, start, end):
        if start == end:
            return lists[start]
        
        if start + 1 == end:
            return merge_two_lists(lists[start], lists[end])
        
        mid = (start + end) // 2
        left = merge_lists(lists, start, mid)
        right = merge_lists(lists, mid + 1, end)
        
        return merge_two_lists(left, right)
    
    return merge_lists(lists, 0, len(lists) - 1)
```

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(n log k)  
**Không gian**: O(log k)

---

## 📚 **LEVEL 7: Smallest Range Covering Elements from K Lists**
**Mục tiêu**: Tìm khoảng nhỏ nhất bao phủ phần tử từ k lists

### Bài toán: Smallest Range Covering Elements from K Lists
```python
def smallest_range(nums):
    """
    Tìm khoảng nhỏ nhất bao phủ phần tử từ k lists
    """
    # Tạo heap với phần tử đầu tiên của mỗi list
    heap = []
    max_val = float('-inf')
    
    for i, lst in enumerate(nums):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
            max_val = max(max_val, lst[0])
    
    min_range = float('inf')
    start, end = 0, 0
    
    while len(heap) == len(nums):
        min_val, list_idx, elem_idx = heapq.heappop(heap)
        
        # Cập nhật khoảng nhỏ nhất
        if max_val - min_val < min_range:
            min_range = max_val - min_val
            start, end = min_val, max_val
        
        # Thêm phần tử tiếp theo từ list này
        if elem_idx + 1 < len(nums[list_idx]):
            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
            max_val = max(max_val, next_val)
    
    return [start, end]
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n log k)  
**Không gian**: O(k)

---

## 📚 **LEVEL 8: Merge K Sorted Lists (Iterative)**
**Mục tiêu**: Sử dụng iterative approach để merge k lists

### Bài toán: Iterative K-Way Merge
```python
def merge_k_lists_iterative(lists):
    """
    Hợp nhất k danh sách sử dụng iterative approach
    """
    if not lists:
        return None
    
    # Merge từng cặp lists
    while len(lists) > 1:
        merged_lists = []
        
        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                merged = merge_two_lists(lists[i], lists[i + 1])
                merged_lists.append(merged)
            else:
                merged_lists.append(lists[i])
        
        lists = merged_lists
    
    return lists[0]
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n log k)  
**Không gian**: O(1)

---

## 📚 **LEVEL 9: K-Way Merge with Custom Comparator**
**Mục tiêu**: Sử dụng custom comparator trong k-way merge

### Bài toán: Merge K Lists with Custom Comparator
```python
def merge_k_lists_custom(lists, comparator):
    """
    Hợp nhất k danh sách với custom comparator
    """
    if not lists:
        return None
    
    # Sử dụng heap với custom comparator
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))
    
    dummy = ListNode(0)
    current = dummy
    
    while heap:
        val, list_idx, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        
        if node.next:
            # Sử dụng custom comparator
            next_val = node.next.val
            if comparator(next_val, val):
                heapq.heappush(heap, (next_val, list_idx, node.next))
    
    return dummy.next
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n log k)  
**Không gian**: O(k)

---

## 📚 **LEVEL 10: Advanced K-Way Merge Applications**
**Mục tiêu**: Ứng dụng k-way merge trong bài toán phức tạp

### Bài toán: Merge K Sorted Arrays with Duplicates
```python
def merge_k_arrays_with_duplicates(arrays):
    """
    Hợp nhất k mảng đã sắp xếp và loại bỏ trùng lặp
    """
    if not arrays:
        return []
    
    # Sử dụng min heap với (value, array_index, element_index)
    heap = []
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))
    
    result = []
    prev_val = None
    
    while heap:
        val, arr_idx, elem_idx = heapq.heappop(heap)
        
        # Loại bỏ trùng lặp
        if val != prev_val:
            result.append(val)
            prev_val = val
        
        # Thêm phần tử tiếp theo từ mảng này
        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, arr_idx, elem_idx + 1))
    
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n log k)  
**Không gian**: O(k)

---

## 🎯 **Lộ trình học tập**

### **Giai đoạn 1 (Level 1-3)**: Nền tảng
- Hiểu khái niệm k-way merge
- Thành thạo merge hai lists
- Làm quen với pattern cơ bản

### **Giai đoạn 2 (Level 4-6)**: Nâng cao
- Matrix problems
- Pair problems
- Divide and conquer

### **Giai đoạn 3 (Level 7-8)**: Chuyên sâu
- Range problems
- Iterative approaches
- Tối ưu hóa bộ nhớ

### **Giai đoạn 4 (Level 9-10)**: Master
- Custom comparators
- Advanced applications
- Edge cases phức tạp

## 💡 **Mẹo cho từng level**

- **Level 1-3**: Tập trung vào hiểu pattern cơ bản
- **Level 4-6**: Chú ý đến việc xử lý matrix và pairs
- **Level 7-8**: Hiểu sâu về range problems và iterative approaches
- **Level 9-10**: Thực hành nhiều và phân tích các trường hợp đặc biệt

## 🔥 **Common Patterns**

### **Basic K-Way Merge**
```python
heap = []
for i, lst in enumerate(lists):
    if lst:
        heapq.heappush(heap, (lst.val, i, lst))

while heap:
    val, list_idx, node = heapq.heappop(heap)
    # Process node
    if node.next:
        heapq.heappush(heap, (node.next.val, list_idx, node.next))
```

### **Matrix K-Way Merge**
```python
heap = [(matrix[0][0], 0, 0)]
visited = {(0, 0)}

while heap:
    val, row, col = heapq.heappop(heap)
    # Process value
    
    # Add neighbors
    for dr, dc in [(0, 1), (1, 0)]:
        new_row, new_col = row + dr, col + dc
        if (new_row, new_col) not in visited:
            heapq.heappush(heap, (matrix[new_row][new_col], new_row, new_col))
            visited.add((new_row, new_col))
```

### **Divide and Conquer**
```python
def merge_lists(lists, start, end):
    if start == end:
        return lists[start]
    
    mid = (start + end) // 2
    left = merge_lists(lists, start, mid)
    right = merge_lists(lists, mid + 1, end)
    
    return merge_two_lists(left, right)
``` 