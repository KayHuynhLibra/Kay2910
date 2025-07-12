# SUBSETS - 10 LEVELS TỪ CƠ BẢN ĐẾN NÂNG CAO

## 🎯 Tổng quan
10 level này được thiết kế để bạn học Subsets từ cơ bản đến nâng cao.

---

## 📚 **LEVEL 1: Hiểu cơ bản về Subsets**
**Mục tiêu**: Hiểu khái niệm và cách hoạt động của subsets

### Bài toán: Subsets
```python
def subsets(nums):
    """
    Tìm tất cả subsets của mảng
    """
    result = []
    
    def backtrack(start, current):
        result.append(current[:])
        
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result
```

**Độ khó**: ⭐  
**Thời gian**: O(2^n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 2: Subsets II (With Duplicates)**
**Mục tiêu**: Xử lý subsets với phần tử trùng lặp

### Bài toán: Subsets II
```python
def subsets_with_dup(nums):
    """
    Tìm tất cả subsets với phần tử trùng lặp
    """
    nums.sort()  # Sắp xếp để xử lý trùng lặp
    result = []
    
    def backtrack(start, current):
        result.append(current[:])
        
        for i in range(start, len(nums)):
            # Bỏ qua phần tử trùng lặp
            if i > start and nums[i] == nums[i - 1]:
                continue
            
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result
```

**Độ khó**: ⭐⭐  
**Thời gian**: O(2^n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 3: Permutations**
**Mục tiêu**: Tìm tất cả hoán vị

### Bài toán: Permutations
```python
def permutations(nums):
    """
    Tìm tất cả hoán vị của mảng
    """
    result = []
    
    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return
        
        for num in nums:
            if num not in current:
                current.append(num)
                backtrack(current)
                current.pop()
    
    backtrack([])
    return result
```

**Độ khó**: ⭐⭐⭐  
**Thời gian**: O(n!)  
**Không gian**: O(n)

---

## 📚 **LEVEL 4: Permutations II (With Duplicates)**
**Mục tiêu**: Xử lý hoán vị với phần tử trùng lặp

### Bài toán: Permutations II
```python
def permutations_ii(nums):
    """
    Tìm tất cả hoán vị với phần tử trùng lặp
    """
    nums.sort()
    result = []
    used = [False] * len(nums)
    
    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return
        
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            
            used[i] = True
            current.append(nums[i])
            backtrack(current)
            current.pop()
            used[i] = False
    
    backtrack([])
    return result
```

**Độ khó**: ⭐⭐⭐⭐  
**Thời gian**: O(n!)  
**Không gian**: O(n)

---

## 📚 **LEVEL 5: Combination Sum**
**Mục tiêu**: Tìm tổ hợp có tổng bằng target

### Bài toán: Combination Sum
```python
def combination_sum(candidates, target):
    """
    Tìm tổ hợp có tổng bằng target
    """
    result = []
    
    def backtrack(start, current, current_sum):
        if current_sum == target:
            result.append(current[:])
            return
        
        if current_sum > target:
            return
        
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, current_sum + candidates[i])
            current.pop()
    
    backtrack(0, [], 0)
    return result
```

**Độ khó**: ⭐⭐⭐⭐  
**Thời gian**: O(2^n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 6: Combination Sum II**
**Mục tiêu**: Tổ hợp với điều kiện không trùng lặp

### Bài toán: Combination Sum II
```python
def combination_sum_ii(candidates, target):
    """
    Tìm tổ hợp có tổng bằng target (không trùng lặp)
    """
    candidates.sort()
    result = []
    
    def backtrack(start, current, current_sum):
        if current_sum == target:
            result.append(current[:])
            return
        
        if current_sum > target:
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            current.append(candidates[i])
            backtrack(i + 1, current, current_sum + candidates[i])
            current.pop()
    
    backtrack(0, [], 0)
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(2^n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 7: Palindrome Partitioning**
**Mục tiêu**: Phân hoạch chuỗi thành palindrome

### Bài toán: Palindrome Partitioning
```python
def partition(s):
    """
    Phân hoạch chuỗi thành palindrome
    """
    result = []
    
    def is_palindrome(s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    def backtrack(start, current):
        if start == len(s):
            result.append(current[:])
            return
        
        for end in range(start, len(s)):
            if is_palindrome(s, start, end):
                current.append(s[start:end + 1])
                backtrack(end + 1, current)
                current.pop()
    
    backtrack(0, [])
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n * 2^n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 8: Generate Parentheses**
**Mục tiêu**: Tạo tất cả cặp dấu ngoặc hợp lệ

### Bài toán: Generate Parentheses
```python
def generate_parentheses(n):
    """
    Tạo tất cả cặp dấu ngoặc hợp lệ
    """
    result = []
    
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)
        
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)
    
    backtrack("", 0, 0)
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(4^n / sqrt(n))  
**Không gian**: O(n)

---

## 📚 **LEVEL 9: Word Search**
**Mục tiêu**: Tìm từ trong ma trận 2D

### Bài toán: Word Search
```python
def word_search(board, word):
    """
    Tìm từ trong ma trận 2D
    """
    rows, cols = len(board), len(board[0])
    
    def backtrack(row, col, word_index):
        if word_index == len(word):
            return True
        
        if (row < 0 or row >= rows or col < 0 or col >= cols or 
            board[row][col] != word[word_index]):
            return False
        
        # Đánh dấu đã sử dụng
        temp = board[row][col]
        board[row][col] = '#'
        
        # Thử 4 hướng
        result = (backtrack(row + 1, col, word_index + 1) or
                 backtrack(row - 1, col, word_index + 1) or
                 backtrack(row, col + 1, word_index + 1) or
                 backtrack(row, col - 1, word_index + 1))
        
        # Khôi phục
        board[row][col] = temp
        return result
    
    for row in range(rows):
        for col in range(cols):
            if backtrack(row, col, 0):
                return True
    
    return False
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(m * n * 4^L)  
**Không gian**: O(L)

---

## 📚 **LEVEL 10: Advanced Subsets Applications**
**Mục tiêu**: Ứng dụng subsets trong bài toán phức tạp

### Bài toán: N-Queens
```python
def solve_n_queens(n):
    """
    Giải bài toán N-Queens
    """
    result = []
    
    def is_safe(board, row, col):
        # Kiểm tra cột
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Kiểm tra đường chéo trái trên
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        # Kiểm tra đường chéo phải trên
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == 'Q':
                return False
        
        return True
    
    def backtrack(row, board):
        if row == n:
            result.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(row + 1, board)
                board[row][col] = '.'
    
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(0, board)
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n!)  
**Không gian**: O(n²)

---

## 🎯 **Lộ trình học tập**

### **Giai đoạn 1 (Level 1-3)**: Nền tảng
- Hiểu khái niệm subsets và backtracking
- Thành thạo subsets cơ bản
- Làm quen với pattern cơ bản

### **Giai đoạn 2 (Level 4-6)**: Nâng cao
- Xử lý trùng lặp
- Combination problems
- Tối ưu hóa thuật toán

### **Giai đoạn 3 (Level 7-8)**: Chuyên sâu
- String problems
- Parentheses generation
- Tối ưu hóa bộ nhớ

### **Giai đoạn 4 (Level 9-10)**: Master
- Matrix problems
- Advanced applications
- Edge cases phức tạp

## 💡 **Mẹo cho từng level**

- **Level 1-3**: Tập trung vào hiểu pattern cơ bản
- **Level 4-6**: Chú ý đến việc xử lý trùng lặp
- **Level 7-8**: Hiểu sâu về ứng dụng trong chuỗi
- **Level 9-10**: Thực hành nhiều và phân tích các trường hợp đặc biệt

## 🔥 **Common Patterns**

### **Basic Backtracking**
```python
def backtrack(start, current):
    # Base case
    if condition:
        result.append(current[:])
        return
    
    for i in range(start, n):
        current.append(nums[i])
        backtrack(i + 1, current)
        current.pop()  # Backtrack
```

### **Handle Duplicates**
```python
nums.sort()
for i in range(start, len(nums)):
    if i > start and nums[i] == nums[i - 1]:
        continue
    # Process
```

### **String Backtracking**
```python
def backtrack(current, start):
    if start == len(s):
        result.append(current[:])
        return
    
    for end in range(start, len(s)):
        if is_valid(s[start:end + 1]):
            current.append(s[start:end + 1])
            backtrack(current, end + 1)
            current.pop()
``` 