# SLIDING WINDOW - 20 LEVELS TỪ CƠ BẢN ĐẾN NÂNG CAO

## 🎯 Tổng quan
20 level này được thiết kế để bạn học Sliding Window từ cơ bản đến nâng cao, mỗi level tăng dần độ khó và phức tạp.

---

## 📚 **LEVEL 1: Hiểu cơ bản về Sliding Window**
**Mục tiêu**: Hiểu khái niệm và cách hoạt động của sliding window

### Bài toán: Maximum Sum Subarray of Size K
```python
def max_sum_subarray_of_size_k(arr, k):
    """
    Tìm tổng lớn nhất của subarray có kích thước k
    """
    if len(arr) < k:
        return 0
    
    # Tính tổng của window đầu tiên
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Trượt window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

**Độ khó**: ⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 2: Minimum Size Subarray Sum**
**Mục tiêu**: Tìm subarray nhỏ nhất có tổng >= target

### Bài toán: Minimum Size Subarray Sum
```python
def min_sub_array_len(target, nums):
    """
    Tìm độ dài nhỏ nhất của subarray có tổng >= target
    """
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0
```

**Độ khó**: ⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 3: Longest Substring Without Repeating Characters**
**Mục tiêu**: Tìm chuỗi con dài nhất không có ký tự lặp lại

### Bài toán: Longest Substring Without Repeating Characters
```python
def length_of_longest_substring(s):
    """
    Tìm độ dài chuỗi con dài nhất không có ký tự lặp lại
    """
    char_map = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1
        
        char_map[s[right]] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

**Độ khó**: ⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(min(m, n))

---

## 📚 **LEVEL 4: Longest Repeating Character Replacement**
**Mục tiêu**: Thay thế k ký tự để tạo chuỗi con dài nhất

### Bài toán: Longest Repeating Character Replacement
```python
def character_replacement(s, k):
    """
    Thay thế tối đa k ký tự để tạo chuỗi con dài nhất
    """
    char_count = {}
    left = 0
    max_count = 0
    max_length = 0
    
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        max_count = max(max_count, char_count[s[right]])
        
        if (right - left + 1) - max_count > k:
            char_count[s[left]] -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

**Độ khó**: ⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 5: Permutation in String**
**Mục tiêu**: Kiểm tra xem s2 có chứa permutation của s1 không

### Bài toán: Permutation in String
```python
def check_inclusion(s1, s2):
    """
    Kiểm tra xem s2 có chứa permutation của s1 không
    """
    if len(s1) > len(s2):
        return False
    
    s1_count = [0] * 26
    s2_count = [0] * 26
    
    # Khởi tạo count cho s1
    for char in s1:
        s1_count[ord(char) - ord('a')] += 1
    
    # Sliding window trên s2
    for i in range(len(s2)):
        s2_count[ord(s2[i]) - ord('a')] += 1
        
        if i >= len(s1):
            s2_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
        
        if s1_count == s2_count:
            return True
    
    return False
```

**Độ khó**: ⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 6: Find All Anagrams in a String**
**Mục tiêu**: Tìm tất cả anagrams của p trong s

### Bài toán: Find All Anagrams in a String
```python
def find_anagrams(s, p):
    """
    Tìm tất cả anagrams của p trong s
    """
    if len(s) < len(p):
        return []
    
    p_count = [0] * 26
    s_count = [0] * 26
    result = []
    
    # Khởi tạo count cho p
    for char in p:
        p_count[ord(char) - ord('a')] += 1
    
    # Sliding window trên s
    for i in range(len(s)):
        s_count[ord(s[i]) - ord('a')] += 1
        
        if i >= len(p):
            s_count[ord(s[i - len(p)]) - ord('a')] -= 1
        
        if p_count == s_count:
            result.append(i - len(p) + 1)
    
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 7: Substring with Concatenation of All Words**
**Mục tiêu**: Tìm tất cả indices của substring chứa tất cả words

### Bài toán: Substring with Concatenation of All Words
```python
def find_substring(s, words):
    """
    Tìm tất cả indices của substring chứa tất cả words
    """
    if not s or not words:
        return []
    
    word_len = len(words[0])
    word_count = len(words)
    total_len = word_len * word_count
    result = []
    
    # Tạo word frequency map
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    # Kiểm tra từng vị trí bắt đầu
    for i in range(len(s) - total_len + 1):
        seen = {}
        valid = True
        
        for j in range(word_count):
            word = s[i + j * word_len:i + (j + 1) * word_len]
            
            if word not in word_freq:
                valid = False
                break
            
            seen[word] = seen.get(word, 0) + 1
            if seen[word] > word_freq[word]:
                valid = False
                break
        
        if valid:
            result.append(i)
    
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n * m * k)  
**Không gian**: O(m)

---

## 📚 **LEVEL 8: Minimum Window Substring**
**Mục tiêu**: Tìm window nhỏ nhất chứa tất cả ký tự của t

### Bài toán: Minimum Window Substring
```python
def min_window(s, t):
    """
    Tìm window nhỏ nhất chứa tất cả ký tự của t
    """
    if not s or not t:
        return ""
    
    # Tạo frequency map cho t
    t_freq = {}
    for char in t:
        t_freq[char] = t_freq.get(char, 0) + 1
    
    left = 0
    min_left = 0
    min_len = float('inf')
    required = len(t_freq)
    formed = 0
    window_freq = {}
    
    for right in range(len(s)):
        char = s[right]
        window_freq[char] = window_freq.get(char, 0) + 1
        
        if char in t_freq and window_freq[char] == t_freq[char]:
            formed += 1
        
        while left <= right and formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_left = left
            
            char = s[left]
            window_freq[char] -= 1
            
            if char in t_freq and window_freq[char] < t_freq[char]:
                formed -= 1
            
            left += 1
    
    return s[min_left:min_left + min_len] if min_len != float('inf') else ""
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(k)

---

## 📚 **LEVEL 9: Sliding Window Maximum**
**Mục tiêu**: Tìm maximum trong mỗi sliding window

### Bài toán: Sliding Window Maximum
```python
from collections import deque

def max_sliding_window(nums, k):
    """
    Tìm maximum trong mỗi sliding window
    """
    if not nums or k == 0:
        return []
    
    deq = deque()
    result = []
    
    for i in range(len(nums)):
        # Loại bỏ các phần tử nhỏ hơn nums[i] từ back
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
        
        deq.append(i)
        
        # Loại bỏ phần tử ngoài window từ front
        if deq[0] == i - k:
            deq.popleft()
        
        # Thêm maximum vào result
        if i >= k - 1:
            result.append(nums[deq[0]])
    
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(k)

---

## 📚 **LEVEL 10: Longest Substring with At Most K Distinct Characters**
**Mục tiêu**: Tìm chuỗi con dài nhất có tối đa k ký tự khác nhau

### Bài toán: Longest Substring with At Most K Distinct Characters
```python
def length_of_longest_substring_k_distinct(s, k):
    """
    Tìm độ dài chuỗi con dài nhất có tối đa k ký tự khác nhau
    """
    if k == 0:
        return 0
    
    char_count = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(k)

---

## 📚 **LEVEL 11: Longest Substring with At Most Two Distinct Characters**
**Mục tiêu**: Tìm chuỗi con dài nhất có tối đa 2 ký tự khác nhau

### Bài toán: Longest Substring with At Most Two Distinct Characters
```python
def length_of_longest_substring_two_distinct(s):
    """
    Tìm độ dài chuỗi con dài nhất có tối đa 2 ký tự khác nhau
    """
    return length_of_longest_substring_k_distinct(s, 2)
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 12: Subarrays with K Different Integers**
**Mục tiêu**: Đếm số subarray có đúng k số nguyên khác nhau

### Bài toán: Subarrays with K Different Integers
```python
def subarrays_with_k_distinct(nums, k):
    """
    Đếm số subarray có đúng k số nguyên khác nhau
    """
    def at_most_k_distinct(k):
        count = {}
        left = 0
        result = 0
        
        for right in range(len(nums)):
            count[nums[right]] = count.get(nums[right], 0) + 1
            
            while len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            
            result += right - left + 1
        
        return result
    
    return at_most_k_distinct(k) - at_most_k_distinct(k - 1)
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(k)

---

## 📚 **LEVEL 13: Fruit Into Baskets**
**Mục tiêu**: Thu thập tối đa 2 loại trái cây

### Bài toán: Fruit Into Baskets
```python
def total_fruit(fruits):
    """
    Thu thập tối đa 2 loại trái cây
    """
    return length_of_longest_substring_k_distinct(fruits, 2)
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 14: Longest Substring with At Least K Repeating Characters**
**Mục tiêu**: Tìm chuỗi con dài nhất có ít nhất k lần lặp lại mỗi ký tự

### Bài toán: Longest Substring with At Least K Repeating Characters
```python
def longest_substring(s, k):
    """
    Tìm chuỗi con dài nhất có ít nhất k lần lặp lại mỗi ký tự
    """
    def divide_and_conquer(s, k):
        if len(s) < k:
            return 0
        
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Tìm ký tự có frequency < k
        for char, count in char_count.items():
            if count < k:
                return max(divide_and_conquer(substring, k) 
                          for substring in s.split(char))
        
        return len(s)
    
    return divide_and_conquer(s, k)
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n²)  
**Không gian**: O(n)

---

## 📚 **LEVEL 15: Maximum Points You Can Obtain from Cards**
**Mục tiêu**: Lấy k thẻ từ đầu hoặc cuối để có điểm cao nhất

### Bài toán: Maximum Points You Can Obtain from Cards
```python
def max_score(card_points, k):
    """
    Lấy k thẻ từ đầu hoặc cuối để có điểm cao nhất
    """
    n = len(card_points)
    window_size = n - k
    
    # Tính tổng của window giữa
    window_sum = sum(card_points[:window_size])
    min_window_sum = window_sum
    
    # Trượt window
    for i in range(window_size, n):
        window_sum = window_sum - card_points[i - window_size] + card_points[i]
        min_window_sum = min(min_window_sum, window_sum)
    
    return sum(card_points) - min_window_sum
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 16: Number of Substrings Containing All Three Characters**
**Mục tiêu**: Đếm số substring chứa cả 3 ký tự a, b, c

### Bài toán: Number of Substrings Containing All Three Characters
```python
def number_of_substrings(s):
    """
    Đếm số substring chứa cả 3 ký tự a, b, c
    """
    count = [0] * 3  # count of a, b, c
    left = 0
    result = 0
    
    for right in range(len(s)):
        count[ord(s[right]) - ord('a')] += 1
        
        while all(count):
            result += len(s) - right
            count[ord(s[left]) - ord('a')] -= 1
            left += 1
    
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 17: Replace the Substring for Balanced String**
**Mục tiêu**: Thay thế substring để cân bằng Q, W, E, R

### Bài toán: Replace the Substring for Balanced String
```python
def balanced_string(s):
    """
    Thay thế substring để cân bằng Q, W, E, R
    """
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    target = len(s) // 4
    extra = {}
    
    for char in 'QWER':
        if count.get(char, 0) > target:
            extra[char] = count[char] - target
    
    if not extra:
        return 0
    
    left = 0
    min_len = float('inf')
    window_count = {}
    
    for right in range(len(s)):
        window_count[s[right]] = window_count.get(s[right], 0) + 1
        
        while all(window_count.get(char, 0) >= extra.get(char, 0) for char in extra):
            min_len = min(min_len, right - left + 1)
            window_count[s[left]] -= 1
            left += 1
    
    return min_len
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 18: Count Number of Nice Subarrays**
**Mục tiêu**: Đếm số subarray có đúng k số lẻ

### Bài toán: Count Number of Nice Subarrays
```python
def number_of_subarrays(nums, k):
    """
    Đếm số subarray có đúng k số lẻ
    """
    def at_most_k_odd(k):
        left = 0
        result = 0
        odd_count = 0
        
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd_count += 1
            
            while odd_count > k:
                if nums[left] % 2 == 1:
                    odd_count -= 1
                left += 1
            
            result += right - left + 1
        
        return result
    
    return at_most_k_odd(k) - at_most_k_odd(k - 1)
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 19: Advanced Sliding Window with Multiple Constraints**
**Mục tiêu**: Sliding window với nhiều điều kiện phức tạp

### Bài toán: Advanced Sliding Window
```python
def advanced_sliding_window(nums, k, target_sum, target_product):
    """
    Sliding window với nhiều điều kiện: kích thước k, tổng >= target_sum, tích <= target_product
    """
    if k > len(nums):
        return 0
    
    left = 0
    current_sum = 0
    current_product = 1
    count = 0
    
    for right in range(len(nums)):
        current_sum += nums[right]
        current_product *= nums[right]
        
        # Mở rộng window đến kích thước k
        if right - left + 1 == k:
            if current_sum >= target_sum and current_product <= target_product:
                count += 1
            
            current_sum -= nums[left]
            current_product //= nums[left]
            left += 1
    
    return count
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 20: Master Level - Complex Sliding Window Applications**
**Mục tiêu**: Ứng dụng sliding window trong bài toán phức tạp nhất

### Bài toán: Master Sliding Window
```python
def master_sliding_window(s, patterns):
    """
    Sliding window với nhiều pattern và điều kiện phức tạp
    """
    def is_valid_window(window, patterns):
        # Kiểm tra tất cả patterns
        for pattern in patterns:
            if pattern not in window:
                return False
        return True
    
    def get_window_score(window):
        # Tính điểm của window dựa trên nhiều tiêu chí
        score = 0
        char_freq = {}
        
        for char in window:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        # Điểm dựa trên độ đa dạng
        score += len(char_freq) * 10
        
        # Điểm dựa trên độ cân bằng
        min_freq = min(char_freq.values())
        max_freq = max(char_freq.values())
        score += (max_freq - min_freq) * -5
        
        return score
    
    if not s or not patterns:
        return ""
    
    left = 0
    best_window = ""
    best_score = float('-inf')
    
    for right in range(len(s)):
        window = s[left:right + 1]
        
        # Kiểm tra tính hợp lệ
        while left <= right and not is_valid_window(window, patterns):
            left += 1
            window = s[left:right + 1]
        
        if is_valid_window(window, patterns):
            score = get_window_score(window)
            if score > best_score:
                best_score = score
                best_window = window
    
    return best_window
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n * m * k)  
**Không gian**: O(n)

---

## 🎯 **Lộ trình học tập**

### **Giai đoạn 1 (Level 1-5)**: Nền tảng
- Hiểu khái niệm sliding window
- Thành thạo window cố định và thay đổi
- Làm quen với pattern cơ bản

### **Giai đoạn 2 (Level 6-10)**: Nâng cao
- Xử lý string problems
- Window với điều kiện phức tạp
- Tối ưu hóa thuật toán

### **Giai đoạn 3 (Level 11-15)**: Chuyên sâu
- K distinct characters
- Advanced string manipulation
- Tối ưu hóa bộ nhớ

### **Giai đoạn 4 (Level 16-20)**: Master
- Multiple constraints
- Complex applications
- Edge cases phức tạp

## 💡 **Mẹo cho từng level**

- **Level 1-5**: Tập trung vào hiểu pattern cơ bản
- **Level 6-10**: Chú ý đến việc xử lý string và anagrams
- **Level 11-15**: Hiểu sâu về k distinct characters
- **Level 16-20**: Thực hành nhiều và phân tích các trường hợp đặc biệt

## 🔥 **Common Patterns**

### **Fixed Size Window**
```python
window_sum = sum(arr[:k])
for i in range(k, len(arr)):
    window_sum = window_sum - arr[i - k] + arr[i]
    # Process window_sum
```

### **Variable Size Window**
```python
left = 0
for right in range(len(arr)):
    # Expand window
    while condition:
        # Shrink window
        left += 1
```

### **String Window**
```python
char_count = {}
for right in range(len(s)):
    char_count[s[right]] = char_count.get(s[right], 0) + 1
    while len(char_count) > k:
        char_count[s[left]] -= 1
        if char_count[s[left]] == 0:
            del char_count[s[left]]
        left += 1
``` 