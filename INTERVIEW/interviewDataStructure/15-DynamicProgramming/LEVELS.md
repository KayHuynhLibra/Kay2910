# DYNAMIC PROGRAMMING - 20 LEVELS TỪ CƠ BẢN ĐẾN NÂNG CAO

## 🎯 Tổng quan
20 level này được thiết kế để bạn học Dynamic Programming từ cơ bản đến nâng cao.

---

## 📚 **LEVEL 1: Hiểu cơ bản về Dynamic Programming**
**Mục tiêu**: Hiểu khái niệm và cách hoạt động

### Bài toán: Fibonacci Number
```python
def fib(n):
    """
    Tính số Fibonacci thứ n
    """
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]
```

**Độ khó**: ⭐  
**Thời gian**: O(n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 2: Climbing Stairs**
**Mục tiêu**: Đếm số cách leo cầu thang

### Bài toán: Climbing Stairs
```python
def climb_stairs(n):
    """
    Đếm số cách leo cầu thang n bậc
    """
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]
```

**Độ khó**: ⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 3: House Robber**
**Mục tiêu**: Cướp nhà để có tiền nhiều nhất

### Bài toán: House Robber
```python
def rob(nums):
    """
    Cướp nhà để có tiền nhiều nhất
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    
    return dp[-1]
```

**Độ khó**: ⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 4: Maximum Subarray**
**Mục tiêu**: Tìm subarray có tổng lớn nhất

### Bài toán: Maximum Subarray
```python
def max_sub_array(nums):
    """
    Tìm subarray có tổng lớn nhất
    """
    if not nums:
        return 0
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    max_sum = dp[0]
    
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])
        max_sum = max(max_sum, dp[i])
    
    return max_sum
```

**Độ khó**: ⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 5: Coin Change**
**Mục tiêu**: Tìm số đồng xu ít nhất để tạo ra amount

### Bài toán: Coin Change
```python
def coin_change(coins, amount):
    """
    Tìm số đồng xu ít nhất để tạo ra amount
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1
```

**Độ khó**: ⭐⭐⭐⭐  
**Thời gian**: O(amount * len(coins))  
**Không gian**: O(amount)

---

## 📚 **LEVEL 6: Longest Increasing Subsequence**
**Mục tiêu**: Tìm dãy con tăng dài nhất

### Bài toán: Longest Increasing Subsequence
```python
def length_of_lis(nums):
    """
    Tìm độ dài dãy con tăng dài nhất
    """
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)
```

**Độ khó**: ⭐⭐⭐⭐  
**Thời gian**: O(n²)  
**Không gian**: O(n)

---

## 📚 **LEVEL 7: Edit Distance**
**Mục tiêu**: Tìm số bước ít nhất để biến đổi word1 thành word2

### Bài toán: Edit Distance
```python
def min_distance(word1, word2):
    """
    Tìm số bước ít nhất để biến đổi word1 thành word2
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Khởi tạo
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    
    return dp[m][n]
```

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(m * n)  
**Không gian**: O(m * n)

---

## 📚 **LEVEL 8: Longest Common Subsequence**
**Mục tiêu**: Tìm dãy con chung dài nhất

### Bài toán: Longest Common Subsequence
```python
def longest_common_subsequence(text1, text2):
    """
    Tìm độ dài dãy con chung dài nhất
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]
```

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(m * n)  
**Không gian**: O(m * n)

---

## 📚 **LEVEL 9: Knapsack Problem**
**Mục tiêu**: Bài toán cái túi 0/1

### Bài toán: Knapsack Problem
```python
def knapsack(weights, values, capacity):
    """
    Bài toán cái túi 0/1
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n * capacity)  
**Không gian**: O(n * capacity)

---

## 📚 **LEVEL 10: Partition Equal Subset Sum**
**Mục tiêu**: Chia mảng thành hai phần có tổng bằng nhau

### Bài toán: Partition Equal Subset Sum
```python
def can_partition(nums):
    """
    Chia mảng thành hai phần có tổng bằng nhau
    """
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    
    return dp[target]
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n * target)  
**Không gian**: O(target)

---

## 📚 **LEVEL 11: Word Break**
**Mục tiêu**: Kiểm tra xem string có thể chia thành words không

### Bài toán: Word Break
```python
def word_break(s, word_dict):
    """
    Kiểm tra xem string có thể chia thành words không
    """
    word_set = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[len(s)]
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n³)  
**Không gian**: O(n)

---

## 📚 **LEVEL 12: Unique Paths**
**Mục tiêu**: Đếm số đường đi duy nhất từ góc trên trái đến góc dưới phải

### Bài toán: Unique Paths
```python
def unique_paths(m, n):
    """
    Đếm số đường đi duy nhất từ góc trên trái đến góc dưới phải
    """
    dp = [[1] * n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    return dp[m - 1][n - 1]
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(m * n)  
**Không gian**: O(m * n)

---

## 📚 **LEVEL 13: Minimum Path Sum**
**Mục tiêu**: Tìm đường đi có tổng nhỏ nhất

### Bài toán: Minimum Path Sum
```python
def min_path_sum(grid):
    """
    Tìm đường đi có tổng nhỏ nhất
    """
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    
    # Khởi tạo
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    
    # Fill DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    
    return dp[m - 1][n - 1]
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(m * n)  
**Không gian**: O(m * n)

---

## 📚 **LEVEL 14: Decode Ways**
**Mục tiêu**: Đếm số cách decode string thành số

### Bài toán: Decode Ways
```python
def num_decodings(s):
    """
    Đếm số cách decode string thành số
    """
    if not s or s[0] == '0':
        return 0
    
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n + 1):
        # Một chữ số
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        
        # Hai chữ số
        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]
    
    return dp[n]
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 15: Regular Expression Matching**
**Mục tiêu**: Kiểm tra string có match với pattern không

### Bài toán: Regular Expression Matching
```python
def is_match(s, p):
    """
    Kiểm tra string có match với pattern không
    """
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Empty pattern matches empty string
    dp[0][0] = True
    
    # Handle patterns like a*, a*b*, etc.
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]  # 0 occurrence
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
    
    return dp[m][n]
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(m * n)  
**Không gian**: O(m * n)

---

## 📚 **LEVEL 16: Wildcard Matching**
**Mục tiêu**: Kiểm tra string có match với wildcard pattern không

### Bài toán: Wildcard Matching
```python
def is_match_wildcard(s, p):
    """
    Kiểm tra string có match với wildcard pattern không
    """
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Empty pattern matches empty string
    dp[0][0] = True
    
    # Handle patterns like *, **, etc.
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    
    return dp[m][n]
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(m * n)  
**Không gian**: O(m * n)

---

## 📚 **LEVEL 17: Burst Balloons**
**Mục tiêu**: Tìm điểm số cao nhất khi nổ bóng bay

### Bài toán: Burst Balloons
```python
def max_coins(nums):
    """
    Tìm điểm số cao nhất khi nổ bóng bay
    """
    # Thêm 1 vào đầu và cuối
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    
    for length in range(2, n):
        for left in range(n - length):
            right = left + length
            for i in range(left + 1, right):
                dp[left][right] = max(dp[left][right], 
                                    nums[left] * nums[i] * nums[right] + 
                                    dp[left][i] + dp[i][right])
    
    return dp[0][n - 1]
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n³)  
**Không gian**: O(n²)

---

## 📚 **LEVEL 18: Super Egg Drop**
**Mục tiêu**: Tìm số lần thả trứng ít nhất

### Bài toán: Super Egg Drop
```python
def super_egg_drop(k, n):
    """
    Tìm số lần thả trứng ít nhất
    """
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            if i == 1:
                dp[i][j] = j
            elif j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = float('inf')
                for x in range(1, j + 1):
                    dp[i][j] = min(dp[i][j], 
                                  1 + max(dp[i - 1][x - 1], dp[i][j - x]))
    
    return dp[k][n]
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(k * n²)  
**Không gian**: O(k * n)

---

## 📚 **LEVEL 19: Advanced DP with State Compression**
**Mục tiêu**: DP với state compression

### Bài toán: Advanced DP
```python
def advanced_dp_with_state_compression(nums, target):
    """
    DP với state compression
    """
    n = len(nums)
    total = sum(nums)
    
    if total < target or (total + target) % 2 != 0:
        return 0
    
    subset_sum = (total + target) // 2
    dp = [0] * (subset_sum + 1)
    dp[0] = 1
    
    for num in nums:
        for i in range(subset_sum, num - 1, -1):
            dp[i] += dp[i - num]
    
    return dp[subset_sum]
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n * target)  
**Không gian**: O(target)

---

## 📚 **LEVEL 20: Master Level - Complex DP Applications**
**Mục tiêu**: Ứng dụng DP trong bài toán phức tạp nhất

### Bài toán: Master DP
```python
def master_dp_problem(grid, k):
    """
    DP với nhiều điều kiện phức tạp
    """
    m, n = len(grid), len(grid[0])
    
    # dp[i][j][k] = số đường đi đến (i,j) với k obstacles
    dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(m)]
    
    # Khởi tạo
    if grid[0][0] == 1:
        dp[0][0][1] = 1
    else:
        dp[0][0][0] = 1
    
    # Fill DP table
    for i in range(m):
        for j in range(n):
            for obstacle in range(k + 1):
                if i == 0 and j == 0:
                    continue
                
                current_obstacles = obstacle
                if grid[i][j] == 1:
                    current_obstacles -= 1
                
                if current_obstacles < 0:
                    continue
                
                # Từ trên xuống
                if i > 0:
                    dp[i][j][obstacle] += dp[i - 1][j][current_obstacles]
                
                # Từ trái sang
                if j > 0:
                    dp[i][j][obstacle] += dp[i][j - 1][current_obstacles]
    
    return sum(dp[m - 1][n - 1])
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(m * n * k)  
**Không gian**: O(m * n * k)

---

## 🎯 **Lộ trình học tập**

### **Giai đoạn 1 (Level 1-5)**: Nền tảng
- Hiểu khái niệm DP
- Thành thạo basic DP problems
- Làm quen với pattern cơ bản

### **Giai đoạn 2 (Level 6-10)**: Nâng cao
- String DP problems
- Optimization problems
- Tối ưu hóa thuật toán

### **Giai đoạn 3 (Level 11-15)**: Chuyên sâu
- Advanced DP problems
- State compression
- Tối ưu hóa bộ nhớ

### **Giai đoạn 4 (Level 16-20)**: Master
- Complex applications
- Multiple constraints
- Edge cases phức tạp

## 💡 **Mẹo cho từng level**

- **Level 1-5**: Tập trung vào hiểu pattern cơ bản
- **Level 6-10**: Chú ý đến việc xác định state và transition
- **Level 11-15**: Hiểu sâu về optimization techniques
- **Level 16-20**: Thực hành nhiều và phân tích các trường hợp đặc biệt

## 🔥 **Common Patterns**

### **1D DP**
```python
dp = [0] * (n + 1)
dp[0] = base_case
for i in range(1, n + 1):
    dp[i] = transition_function(dp, i)
```

### **2D DP**
```python
dp = [[0] * n for _ in range(m)]
# Initialize first row/column
for i in range(m):
    for j in range(n):
        dp[i][j] = transition_function(dp, i, j)
```

### **State Compression**
```python
dp = [0] * (1 << n)
for state in range(1 << n):
    for i in range(n):
        if state & (1 << i):
            # Process state
``` 