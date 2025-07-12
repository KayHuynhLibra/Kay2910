# TWO HEAPS - 10 LEVELS TỪ CƠ BẢN ĐẾN NÂNG CAO

## 🎯 Tổng quan
10 level này được thiết kế để bạn học Two Heaps từ cơ bản đến nâng cao.

---

## 📚 **LEVEL 1: Hiểu cơ bản về Two Heaps**
**Mục tiêu**: Hiểu khái niệm và cách hoạt động của two heaps

### Bài toán: Find Median from Data Stream
```python
import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []  # Lưu nửa nhỏ hơn
        self.min_heap = []  # Lưu nửa lớn hơn
    
    def add_num(self, num):
        # Thêm vào max heap trước
        heapq.heappush(self.max_heap, -num)
        
        # Cân bằng hai heap
        if (self.max_heap and self.min_heap and 
            -self.max_heap[0] > self.min_heap[0]):
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        
        # Đảm bảo kích thước cân bằng
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
    
    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2
```

**Độ khó**: ⭐  
**Thời gian**: O(log n) cho add, O(1) cho find  
**Không gian**: O(n)

---

## 📚 **LEVEL 2: Sliding Window Median**
**Mục tiêu**: Tìm median trong sliding window

### Bài toán: Sliding Window Median
```python
def median_sliding_window(nums, k):
    """
    Tìm median trong sliding window kích thước k
    """
    def add_num(num):
        heapq.heappush(max_heap, -num)
        
        if max_heap and min_heap and -max_heap[0] > min_heap[0]:
            val = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, val)
        
        if len(max_heap) > len(min_heap) + 1:
            val = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, val)
        elif len(min_heap) > len(max_heap):
            val = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -val)
    
    def remove_num(num):
        if num <= -max_heap[0]:
            max_heap.remove(-num)
            heapq.heapify(max_heap)
        else:
            min_heap.remove(num)
            heapq.heapify(min_heap)
    
    def get_median():
        if len(max_heap) > len(min_heap):
            return -max_heap[0]
        return (-max_heap[0] + min_heap[0]) / 2
    
    max_heap = []
    min_heap = []
    result = []
    
    for i in range(len(nums)):
        add_num(nums[i])
        
        if i >= k - 1:
            result.append(get_median())
            remove_num(nums[i - k + 1])
    
    return result
```

**Độ khó**: ⭐⭐  
**Thời gian**: O(n log k)  
**Không gian**: O(k)

---

## 📚 **LEVEL 3: Top K Frequent Elements**
**Mục tiêu**: Tìm k phần tử xuất hiện nhiều nhất

### Bài toán: Top K Frequent Elements
```python
def top_k_frequent(nums, k):
    """
    Tìm k phần tử xuất hiện nhiều nhất
    """
    # Đếm tần suất
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    
    # Sử dụng min heap để lưu k phần tử lớn nhất
    heap = []
    for num, freq in frequency.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    # Trả về kết quả
    result = []
    while heap:
        result.append(heapq.heappop(heap)[1])
    
    return result[::-1]
```

**Độ khó**: ⭐⭐⭐  
**Thời gian**: O(n log k)  
**Không gian**: O(n)

---

## 📚 **LEVEL 4: Kth Largest Element**
**Mục tiêu**: Tìm phần tử lớn thứ k

### Bài toán: Kth Largest Element in an Array
```python
def find_kth_largest(nums, k):
    """
    Tìm phần tử lớn thứ k
    """
    # Sử dụng min heap
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]
```

**Độ khó**: ⭐⭐⭐  
**Thời gian**: O(n log k)  
**Không gian**: O(k)

---

## 📚 **LEVEL 5: Merge K Sorted Lists**
**Mục tiêu**: Hợp nhất k danh sách đã sắp xếp

### Bài toán: Merge k Sorted Lists
```python
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

**Độ khó**: ⭐⭐⭐⭐  
**Thời gian**: O(n log k)  
**Không gian**: O(k)

---

## 📚 **LEVEL 6: Find Median from Data Stream (Advanced)**
**Mục tiêu**: Tối ưu hóa việc tìm median

### Bài toán: Optimized Median Finder
```python
class OptimizedMedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.max_heap_size = 0
        self.min_heap_size = 0
    
    def add_num(self, num):
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
            self.max_heap_size += 1
        else:
            heapq.heappush(self.min_heap, num)
            self.min_heap_size += 1
        
        # Cân bằng kích thước
        if self.max_heap_size > self.min_heap_size + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
            self.max_heap_size -= 1
            self.min_heap_size += 1
        elif self.min_heap_size > self.max_heap_size:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
            self.min_heap_size -= 1
            self.max_heap_size += 1
    
    def find_median(self):
        if self.max_heap_size > self.min_heap_size:
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2
```

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(log n) cho add, O(1) cho find  
**Không gian**: O(n)

---

## 📚 **LEVEL 7: Kth Smallest Element in Sorted Matrix**
**Mục tiêu**: Tìm phần tử nhỏ thứ k trong ma trận đã sắp xếp

### Bài toán: Kth Smallest Element in a Sorted Matrix
```python
def kth_smallest(matrix, k):
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

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(k log k)  
**Không gian**: O(k)

---

## 📚 **LEVEL 8: Top K Frequent Words**
**Mục tiêu**: Tìm k từ xuất hiện nhiều nhất

### Bài toán: Top K Frequent Words
```python
def top_k_frequent_words(words, k):
    """
    Tìm k từ xuất hiện nhiều nhất
    """
    # Đếm tần suất
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    # Sử dụng heap với (-freq, word) để sắp xếp theo thứ tự giảm dần
    heap = []
    for word, freq in frequency.items():
        heapq.heappush(heap, (-freq, word))
    
    # Lấy k phần tử đầu tiên
    result = []
    for _ in range(k):
        result.append(heapq.heappop(heap)[1])
    
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n log n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 9: Design Twitter**
**Mục tiêu**: Thiết kế hệ thống Twitter với feed

### Bài toán: Design Twitter
```python
class Twitter:
    def __init__(self):
        self.tweets = {}  # user_id -> list of (timestamp, tweet_id)
        self.following = {}  # user_id -> set of followee_id
        self.timestamp = 0
    
    def post_tweet(self, user_id, tweet_id):
        if user_id not in self.tweets:
            self.tweets[user_id] = []
        self.tweets[user_id].append((self.timestamp, tweet_id))
        self.timestamp += 1
    
    def get_news_feed(self, user_id):
        # Thu thập tweets từ user và những người user follow
        candidates = []
        
        # Tweets của user
        if user_id in self.tweets:
            candidates.extend(self.tweets[user_id])
        
        # Tweets của những người user follow
        if user_id in self.following:
            for followee_id in self.following[user_id]:
                if followee_id in self.tweets:
                    candidates.extend(self.tweets[followee_id])
        
        # Sắp xếp theo timestamp và lấy 10 tweets gần nhất
        candidates.sort(reverse=True)
        return [tweet_id for _, tweet_id in candidates[:10]]
    
    def follow(self, follower_id, followee_id):
        if follower_id not in self.following:
            self.following[follower_id] = set()
        self.following[follower_id].add(followee_id)
    
    def unfollow(self, follower_id, followee_id):
        if follower_id in self.following:
            self.following[follower_id].discard(followee_id)
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n log n) cho get_news_feed  
**Không gian**: O(n)

---

## 📚 **LEVEL 10: Advanced Two Heaps Applications**
**Mục tiêu**: Ứng dụng two heaps trong bài toán phức tạp

### Bài toán: IPO (Initial Public Offering)
```python
def find_maximized_capital(k, w, profits, capital):
    """
    Tìm vốn tối đa sau k dự án
    """
    # Sắp xếp theo capital
    projects = sorted(zip(capital, profits))
    
    # Max heap cho profits
    max_heap = []
    i = 0
    
    for _ in range(k):
        # Thêm tất cả dự án có thể thực hiện
        while i < len(projects) and projects[i][0] <= w:
            heapq.heappush(max_heap, -projects[i][1])
            i += 1
        
        # Chọn dự án có profit cao nhất
        if max_heap:
            w -= heapq.heappop(max_heap)
        else:
            break
    
    return w
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n log n)  
**Không gian**: O(n)

---

## 🎯 **Lộ trình học tập**

### **Giai đoạn 1 (Level 1-3)**: Nền tảng
- Hiểu khái niệm two heaps
- Thành thạo median finder
- Làm quen với pattern cơ bản

### **Giai đoạn 2 (Level 4-6)**: Nâng cao
- Top K elements
- Merge k sorted lists
- Tối ưu hóa thuật toán

### **Giai đoạn 3 (Level 7-8)**: Chuyên sâu
- Matrix problems
- Word frequency
- Tối ưu hóa bộ nhớ

### **Giai đoạn 4 (Level 9-10)**: Master
- System design
- Advanced applications
- Edge cases phức tạp

## 💡 **Mẹo cho từng level**

- **Level 1-3**: Tập trung vào hiểu pattern cơ bản
- **Level 4-6**: Chú ý đến việc chọn heap phù hợp
- **Level 7-8**: Hiểu sâu về ứng dụng trong các bài toán khác
- **Level 9-10**: Thực hành nhiều và phân tích các trường hợp đặc biệt

## 🔥 **Common Patterns**

### **Two Heaps for Median**
```python
max_heap = []  # Nửa nhỏ hơn
min_heap = []  # Nửa lớn hơn

def add_num(num):
    heapq.heappush(max_heap, -num)
    # Cân bằng hai heap
    # Đảm bảo kích thước
```

### **Top K Elements**
```python
heap = []
for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)
```

### **Merge K Lists**
```python
heap = []
for lst in lists:
    if lst:
        heapq.heappush(heap, (lst.val, lst))

while heap:
    val, node = heapq.heappop(heap)
    # Process node
    if node.next:
        heapq.heappush(heap, (node.next.val, node.next))
``` 