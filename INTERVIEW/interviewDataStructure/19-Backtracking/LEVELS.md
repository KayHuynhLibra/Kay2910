# BACKTRACKING ALGORITHMS - 20 LEVELS TỪ CƠ BẢN ĐẾN NÂNG CAO

## 🎯 Tổng quan
20 level này được thiết kế để bạn học Backtracking Algorithms từ cơ bản đến nâng cao.

---

## 📚 **LEVEL 1: Hiểu cơ bản về Backtracking**
**Mục tiêu**: Hiểu khái niệm và nguyên lý backtracking

### Bài toán: Generate Parentheses
```python
def generate_parentheses(n):
    """
    Tạo tất cả các cặp ngoặc hợp lệ
    """
    def backtrack(open_count, close_count, current, result):
        if len(current) == 2 * n:
            result.append(current)
            return
        
        if open_count < n:
            backtrack(open_count + 1, close_count, current + '(', result)
        
        if close_count < open_count:
            backtrack(open_count, close_count + 1, current + ')', result)
    
    result = []
    backtrack(0, 0, '', result)
    return result
```

**Độ khó**: ⭐  
**Thời gian**: O(4^n / sqrt(n))  
**Không gian**: O(n)

---

## 📚 **LEVEL 2: Subsets**
**Mục tiêu**: Tạo tất cả các subset

### Bài toán: Subsets
```python
def subsets(nums):
    """
    Tạo tất cả các subset của array
    """
    def backtrack(start, current, result):
        result.append(current[:])
        
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current, result)
            current.pop()
    
    result = []
    backtrack(0, [], result)
    return result
```

**Độ khó**: ⭐⭐  
**Thời gian**: O(2^n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 3: Permutations**
**Mục tiêu**: Tạo tất cả các hoán vị

### Bài toán: Permutations
```python
def permutations(nums):
    """
    Tạo tất cả các hoán vị của array
    """
    def backtrack(current, used, result):
        if len(current) == len(nums):
            result.append(current[:])
            return
        
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                current.append(nums[i])
                backtrack(current, used, result)
                current.pop()
                used[i] = False
    
    result = []
    used = [False] * len(nums)
    backtrack([], used, result)
    return result
```

**Độ khó**: ⭐⭐⭐  
**Thời gian**: O(n!)  
**Không gian**: O(n)

---

## 📚 **LEVEL 4: Combination Sum**
**Mục tiêu**: Tìm tổng các combination

### Bài toán: Combination Sum
```python
def combination_sum(candidates, target):
    """
    Tìm tất cả combinations có tổng bằng target
    """
    def backtrack(start, current, current_sum, result):
        if current_sum == target:
            result.append(current[:])
            return
        
        if current_sum > target:
            return
        
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, current_sum + candidates[i], result)
            current.pop()
    
    result = []
    candidates.sort()
    backtrack(0, [], 0, result)
    return result
```

**Độ khó**: ⭐⭐⭐⭐  
**Thời gian**: O(2^n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 5: N-Queens**
**Mục tiêu**: Bài toán N-Queens

### Bài toán: N-Queens
```python
def solve_n_queens(n):
    """
    Giải bài toán N-Queens
    """
    def is_safe(board, row, col):
        # Check row
        for j in range(col):
            if board[row][j] == 'Q':
                return False
        
        # Check upper diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        # Check lower diagonal
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        return True
    
    def backtrack(col, board, result):
        if col >= n:
            result.append([''.join(row) for row in board])
            return
        
        for row in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(col + 1, board, result)
                board[row][col] = '.'
    
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(0, board, result)
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(n!)  
**Không gian**: O(n²)

---

## 📚 **LEVEL 6: Sudoku Solver**
**Mục tiêu**: Giải Sudoku

### Bài toán: Sudoku Solver
```python
def solve_sudoku(board):
    """
    Giải Sudoku
    """
    def is_valid(board, row, col, num):
        # Check row
        for j in range(9):
            if board[row][j] == str(num):
                return False
        
        # Check column
        for i in range(9):
            if board[i][col] == str(num):
                return False
        
        # Check 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == str(num):
                    return False
        
        return True
    
    def find_empty(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return i, j
        return None
    
    def backtrack(board):
        empty = find_empty(board)
        if not empty:
            return True
        
        row, col = empty
        for num in range(1, 10):
            if is_valid(board, row, col, num):
                board[row][col] = str(num)
                if backtrack(board):
                    return True
                board[row][col] = '.'
        
        return False
    
    backtrack(board)
    return board
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(9^(n²))  
**Không gian**: O(n²)

---

## 📚 **LEVEL 7: Word Search**
**Mục tiêu**: Tìm từ trong ma trận

### Bài toán: Word Search
```python
def word_search(board, word):
    """
    Tìm từ trong ma trận
    """
    def backtrack(i, j, index):
        if index == len(word):
            return True
        
        if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or 
            board[i][j] != word[index]):
            return False
        
        # Mark as visited
        temp = board[i][j]
        board[i][j] = '#'
        
        # Try all directions
        result = (backtrack(i + 1, j, index + 1) or
                 backtrack(i - 1, j, index + 1) or
                 backtrack(i, j + 1, index + 1) or
                 backtrack(i, j - 1, index + 1))
        
        # Restore
        board[i][j] = temp
        return result
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if backtrack(i, j, 0):
                return True
    
    return False
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(m * n * 4^L) với L là độ dài word  
**Không gian**: O(L)

---

## 📚 **LEVEL 8: Palindrome Partitioning**
**Mục tiêu**: Phân vùng palindrome

### Bài toán: Palindrome Partitioning
```python
def palindrome_partitioning(s):
    """
    Phân vùng string thành các palindrome
    """
    def is_palindrome(s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    def backtrack(start, current, result):
        if start >= len(s):
            result.append(current[:])
            return
        
        for end in range(start, len(s)):
            if is_palindrome(s, start, end):
                current.append(s[start:end + 1])
                backtrack(end + 1, current, result)
                current.pop()
    
    result = []
    backtrack(0, [], result)
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n * 2^n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 9: Restore IP Addresses**
**Mục tiêu**: Khôi phục địa chỉ IP

### Bài toán: Restore IP Addresses
```python
def restore_ip_addresses(s):
    """
    Khôi phục địa chỉ IP từ string
    """
    def is_valid(segment):
        if len(segment) > 3 or len(segment) == 0:
            return False
        if len(segment) > 1 and segment[0] == '0':
            return False
        return 0 <= int(segment) <= 255
    
    def backtrack(start, current, result):
        if len(current) == 4:
            if start == len(s):
                result.append('.'.join(current))
            return
        
        for i in range(start, min(start + 3, len(s))):
            segment = s[start:i + 1]
            if is_valid(segment):
                current.append(segment)
                backtrack(i + 1, current, result)
                current.pop()
    
    result = []
    backtrack(0, [], result)
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(3^4)  
**Không gian**: O(1)

---

## 📚 **LEVEL 10: Letter Combinations**
**Mục tiêu**: Tổ hợp chữ cái

### Bài toán: Letter Combinations
```python
def letter_combinations(digits):
    """
    Tạo tổ hợp chữ cái từ digits
    """
    if not digits:
        return []
    
    digit_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index, current, result):
        if index == len(digits):
            result.append(''.join(current))
            return
        
        for char in digit_map[digits[index]]:
            current.append(char)
            backtrack(index + 1, current, result)
            current.pop()
    
    result = []
    backtrack(0, [], result)
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(4^n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 11: Combination Sum II**
**Mục tiêu**: Combination sum với duplicates

### Bài toán: Combination Sum II
```python
def combination_sum_ii(candidates, target):
    """
    Combination sum với duplicates
    """
    def backtrack(start, current, current_sum, result):
        if current_sum == target:
            result.append(current[:])
            return
        
        if current_sum > target:
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            current.append(candidates[i])
            backtrack(i + 1, current, current_sum + candidates[i], result)
            current.pop()
    
    result = []
    candidates.sort()
    backtrack(0, [], 0, result)
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(2^n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 12: Permutations II**
**Mục tiêu**: Permutations với duplicates

### Bài toán: Permutations II
```python
def permutations_ii(nums):
    """
    Permutations với duplicates
    """
    def backtrack(current, used, result):
        if len(current) == len(nums):
            result.append(current[:])
            return
        
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            
            used[i] = True
            current.append(nums[i])
            backtrack(current, used, result)
            current.pop()
            used[i] = False
    
    result = []
    nums.sort()
    used = [False] * len(nums)
    backtrack([], used, result)
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n!)  
**Không gian**: O(n)

---

## 📚 **LEVEL 13: Binary Watch**
**Mục tiêu**: Đồng hồ nhị phân

### Bài toán: Binary Watch
```python
def read_binary_watch(turned_on):
    """
    Đọc đồng hồ nhị phân
    """
    def count_bits(n):
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
    
    result = []
    for hour in range(12):
        for minute in range(60):
            if count_bits(hour) + count_bits(minute) == turned_on:
                result.append(f"{hour}:{minute:02d}")
    
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(1)  
**Không gian**: O(1)

---

## 📚 **LEVEL 14: Beautiful Arrangement**
**Mục tiêu**: Sắp xếp đẹp

### Bài toán: Beautiful Arrangement
```python
def count_arrangement(n):
    """
    Đếm số cách sắp xếp đẹp
    """
    def backtrack(pos, used):
        if pos > n:
            return 1
        
        count = 0
        for i in range(1, n + 1):
            if not used[i] and (pos % i == 0 or i % pos == 0):
                used[i] = True
                count += backtrack(pos + 1, used)
                used[i] = False
        
        return count
    
    used = [False] * (n + 1)
    return backtrack(1, used)
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n!)  
**Không gian**: O(n)

---

## 📚 **LEVEL 15: Word Squares**
**Mục tiêu**: Tạo word squares

### Bài toán: Word Squares
```python
def word_squares(words):
    """
    Tạo word squares
    """
    def build_prefix_map(words):
        prefix_map = {}
        for word in words:
            for i in range(len(word)):
                prefix = word[:i + 1]
                if prefix not in prefix_map:
                    prefix_map[prefix] = []
                prefix_map[prefix].append(word)
        return prefix_map
    
    def get_words_with_prefix(prefix):
        return prefix_map.get(prefix, [])
    
    def backtrack(square, result):
        if len(square) == len(words[0]):
            result.append(square[:])
            return
        
        # Build prefix for next word
        prefix = ''
        for i in range(len(square)):
            prefix += square[i][len(square)]
        
        # Try all words with this prefix
        for word in get_words_with_prefix(prefix):
            square.append(word)
            backtrack(square, result)
            square.pop()
    
    if not words:
        return []
    
    prefix_map = build_prefix_map(words)
    result = []
    
    for word in words:
        backtrack([word], result)
    
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n * 26^L) với L là độ dài word  
**Không gian**: O(n * L)

---

## 📚 **LEVEL 16: Generalized Abbreviation**
**Mục tiêu**: Viết tắt tổng quát

### Bài toán: Generalized Abbreviation
```python
def generate_abbreviations(word):
    """
    Tạo tất cả các cách viết tắt
    """
    def backtrack(pos, current, count, result):
        if pos == len(word):
            if count > 0:
                current += str(count)
            result.append(current)
            return
        
        # Abbreviate current character
        backtrack(pos + 1, current, count + 1, result)
        
        # Keep current character
        if count > 0:
            current += str(count)
        backtrack(pos + 1, current + word[pos], 0, result)
    
    result = []
    backtrack(0, '', 0, result)
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(2^n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 17: Flip Game II**
**Mục tiêu**: Game lật coin

### Bài toán: Flip Game II
```python
def can_win(s):
    """
    Kiểm tra có thể thắng game không
    """
    def backtrack(s):
        for i in range(len(s) - 1):
            if s[i:i + 2] == '++':
                new_s = s[:i] + '--' + s[i + 2:]
                if not backtrack(new_s):
                    return True
        return False
    
    return backtrack(s)
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n!)  
**Không gian**: O(n)

---

## 📚 **LEVEL 18: Android Unlock Patterns**
**Mục tiêu**: Mẫu mở khóa Android

### Bài toán: Android Unlock Patterns
```python
def number_of_patterns(m, n):
    """
    Đếm số mẫu mở khóa Android
    """
    def is_valid_move(used, from_pos, to_pos):
        if used[to_pos]:
            return False
        
        # Check if there's a number between from_pos and to_pos
        if from_pos == 1 and to_pos == 3 and not used[2]:
            return False
        if from_pos == 1 and to_pos == 7 and not used[4]:
            return False
        if from_pos == 1 and to_pos == 9 and not used[5]:
            return False
        if from_pos == 2 and to_pos == 8 and not used[5]:
            return False
        if from_pos == 3 and to_pos == 1 and not used[2]:
            return False
        if from_pos == 3 and to_pos == 7 and not used[5]:
            return False
        if from_pos == 3 and to_pos == 9 and not used[6]:
            return False
        if from_pos == 4 and to_pos == 6 and not used[5]:
            return False
        if from_pos == 6 and to_pos == 4 and not used[5]:
            return False
        if from_pos == 7 and to_pos == 1 and not used[4]:
            return False
        if from_pos == 7 and to_pos == 3 and not used[5]:
            return False
        if from_pos == 7 and to_pos == 9 and not used[8]:
            return False
        if from_pos == 8 and to_pos == 2 and not used[5]:
            return False
        if from_pos == 9 and to_pos == 1 and not used[5]:
            return False
        if from_pos == 9 and to_pos == 3 and not used[6]:
            return False
        if from_pos == 9 and to_pos == 7 and not used[8]:
            return False
        
        return True
    
    def backtrack(pos, length, used):
        if length >= m:
            count[0] += 1
        
        if length == n:
            return
        
        for next_pos in range(1, 10):
            if is_valid_move(used, pos, next_pos):
                used[next_pos] = True
                backtrack(next_pos, length + 1, used)
                used[next_pos] = False
    
    count = [0]
    used = [False] * 10
    
    for start in range(1, 10):
        used[start] = True
        backtrack(start, 1, used)
        used[start] = False
    
    return count[0]
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n!)  
**Không gian**: O(n)

---

## 📚 **LEVEL 19: Advanced Backtracking with Pruning**
**Mục tiêu**: Backtracking với pruning nâng cao

### Bài toán: Advanced Backtracking
```python
def advanced_backtracking_with_pruning(problem_data, constraints):
    """
    Backtracking với pruning nâng cao
    """
    def is_promising(current_solution, remaining_items):
        # Check if current partial solution can lead to a valid solution
        for constraint in constraints:
            if not constraint.is_satisfiable(current_solution, remaining_items):
                return False
        return True
    
    def get_best_candidates(current_solution, remaining_items):
        # Get candidates sorted by some heuristic
        candidates = []
        for item in remaining_items:
            score = evaluate_candidate(item, current_solution)
            candidates.append((score, item))
        candidates.sort(reverse=True)
        return [item for score, item in candidates]
    
    def backtrack(current_solution, remaining_items, best_solution):
        if not remaining_items:
            if evaluate_solution(current_solution) > evaluate_solution(best_solution):
                best_solution[:] = current_solution[:]
            return
        
        # Pruning: check if current path is promising
        if not is_promising(current_solution, remaining_items):
            return
        
        # Get candidates with heuristic ordering
        candidates = get_best_candidates(current_solution, remaining_items)
        
        for item in candidates:
            if is_valid_addition(current_solution, item):
                current_solution.append(item)
                remaining_items.remove(item)
                
                backtrack(current_solution, remaining_items, best_solution)
                
                remaining_items.add(item)
                current_solution.pop()
    
    best_solution = []
    backtrack([], set(problem_data), best_solution)
    return best_solution
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n! * f(n)) với f(n) là cost của pruning  
**Không gian**: O(n)

---

## 📚 **LEVEL 20: Master Level - Complex Backtracking Applications**
**Mục tiêu**: Ứng dụng backtracking trong bài toán phức tạp nhất

### Bài toán: Master Backtracking Algorithm
```python
def master_backtracking_algorithm(problem_data, constraints, objectives):
    """
    Thuật toán backtracking master với nhiều mục tiêu và ràng buộc phức tạp
    """
    class Solution:
        def __init__(self):
            self.items = []
            self.score = 0
            self.constraint_violations = 0
        
        def add_item(self, item):
            self.items.append(item)
            self.update_score()
        
        def remove_item(self):
            if self.items:
                self.items.pop()
                self.update_score()
        
        def update_score(self):
            # Calculate score based on multiple objectives
            self.score = 0
            for objective_name, objective_func in objectives.items():
                weight = objectives.get(f"{objective_name}_weight", 1.0)
                self.score += weight * objective_func(self.items)
            
            # Calculate constraint violations
            self.constraint_violations = 0
            for constraint in constraints:
                if not constraint.is_satisfied(self.items):
                    self.constraint_violations += 1
    
    def backtrack(current_solution, remaining_items, best_solutions):
        # Check if current solution is complete
        if not remaining_items:
            if current_solution.constraint_violations == 0:
                best_solutions.append(current_solution.items[:])
            return
        
        # Pruning: check if current path can lead to better solution
        if current_solution.constraint_violations > 0:
            return
        
        # Get promising candidates
        candidates = get_promising_candidates(current_solution, remaining_items)
        
        for item in candidates:
            # Try adding item
            current_solution.add_item(item)
            remaining_items.remove(item)
            
            # Recursive call
            backtrack(current_solution, remaining_items, best_solutions)
            
            # Backtrack
            remaining_items.add(item)
            current_solution.remove_item()
    
    def get_promising_candidates(current_solution, remaining_items):
        # Get candidates with advanced heuristics
        candidates = []
        for item in remaining_items:
            # Calculate potential score improvement
            potential_score = calculate_potential_score(current_solution, item)
            
            # Calculate constraint satisfaction
            constraint_satisfaction = calculate_constraint_satisfaction(current_solution, item)
            
            # Combined heuristic score
            heuristic_score = potential_score * constraint_satisfaction
            candidates.append((heuristic_score, item))
        
        # Sort by heuristic score
        candidates.sort(reverse=True)
        return [item for score, item in candidates]
    
    def calculate_potential_score(solution, item):
        # Calculate potential score improvement
        temp_solution = Solution()
        temp_solution.items = solution.items[:]
        temp_solution.add_item(item)
        return temp_solution.score - solution.score
    
    def calculate_constraint_satisfaction(solution, item):
        # Calculate how well the item satisfies constraints
        satisfaction = 1.0
        for constraint in constraints:
            if not constraint.is_satisfied(solution.items + [item]):
                satisfaction *= 0.5
        return satisfaction
    
    # Main algorithm
    current_solution = Solution()
    best_solutions = []
    
    backtrack(current_solution, set(problem_data), best_solutions)
    
    return {
        'solutions': best_solutions,
        'count': len(best_solutions),
        'best_score': max([evaluate_solution(sol) for sol in best_solutions]) if best_solutions else 0
    }
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n! * m) với m là số constraints  
**Không gian**: O(n * m)

---

## 🎯 **Lộ trình học tập**

### **Giai đoạn 1 (Level 1-5)**: Nền tảng
- Hiểu khái niệm backtracking
- Thành thạo basic backtracking problems
- Làm quen với pattern cơ bản

### **Giai đoạn 2 (Level 6-10)**: Nâng cao
- Advanced backtracking problems
- Optimization problems
- Tối ưu hóa thuật toán

### **Giai đoạn 3 (Level 11-15)**: Chuyên sâu
- Complex backtracking problems
- Multiple constraints
- Tối ưu hóa bộ nhớ

### **Giai đoạn 4 (Level 16-20)**: Master
- Advanced applications
- Multiple objectives
- Edge cases phức tạp

## 💡 **Mẹo cho từng level**

- **Level 1-5**: Tập trung vào hiểu pattern cơ bản
- **Level 6-10**: Chú ý đến việc tối ưu hóa state
- **Level 11-15**: Hiểu sâu về pruning techniques
- **Level 16-20**: Thực hành nhiều và phân tích các trường hợp đặc biệt

## 🔥 **Common Patterns**

### **Basic Backtracking Pattern**
```python
def backtrack(current, remaining, result):
    if is_complete(current):
        result.append(current[:])
        return
    
    for item in remaining:
        if is_valid(current, item):
            current.append(item)
            backtrack(current, remaining - {item}, result)
            current.pop()
```

### **State-based Backtracking Pattern**
```python
def backtrack_with_state(state, depth, result):
    if depth == target_depth:
        result.append(state.copy())
        return
    
    for choice in get_choices(state):
        if is_valid_choice(state, choice):
            apply_choice(state, choice)
            backtrack_with_state(state, depth + 1, result)
            undo_choice(state, choice)
```

### **Pruning Backtracking Pattern**
```python
def backtrack_with_pruning(current, remaining, result):
    if not is_promising(current, remaining):
        return  # Pruning
    
    if is_complete(current):
        result.append(current[:])
        return
    
    for item in get_promising_candidates(current, remaining):
        current.append(item)
        backtrack_with_pruning(current, remaining - {item}, result)
        current.pop()
``` 