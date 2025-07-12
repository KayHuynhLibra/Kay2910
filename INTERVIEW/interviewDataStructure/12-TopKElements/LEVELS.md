# TOP K ELEMENTS - 10 LEVELS TỪ CƠ BẢN ĐẾN NÂNG CAO

## 🎯 Tổng quan
10 level này được thiết kế để bạn học Top K Elements từ cơ bản đến nâng cao.

---

## 📚 **LEVEL 1: Hiểu cơ bản về Top K Elements**
**Mục tiêu**: Hiểu khái niệm và cách hoạt động

### Bài toán: Top K Frequent Elements
```python
import heapq
from collections import Counter

def top_k_frequent(nums, k):
    """
    Tìm k phần tử xuất hiện nhiều nhất
    """
    # Đếm tần suất
    frequency = Counter(nums)
    
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

**Độ khó**: ⭐  
**Thời gian**: O(n log k)  
**Không gian**: O(n)

---

## 📚 **LEVEL 2: Kth Largest Element**
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

**Độ khó**: ⭐⭐  
**Thời gian**: O(n log k)  
**Không gian**: O(k)

---

## 📚 **LEVEL 3: Top K Frequent Words**
**Mục tiêu**: Tìm k từ xuất hiện nhiều nhất

### Bài toán: Top K Frequent Words
```python
def top_k_frequent_words(words, k):
    """
    Tìm k từ xuất hiện nhiều nhất
    """
    # Đếm tần suất
    frequency = Counter(words)
    
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

**Độ khó**: ⭐⭐⭐  
**Thời gian**: O(n log n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 4: Merge K Sorted Lists**
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

## 📚 **LEVEL 5: Kth Smallest Element in Sorted Matrix**
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

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(k log k)  
**Không gian**: O(k)

---

## 📚 **LEVEL 6: Find K Pairs with Smallest Sums**
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

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(k log k)  
**Không gian**: O(k)

---

## 📚 **LEVEL 7: Top K Frequent Elements (Advanced)**
**Mục tiêu**: Tối ưu hóa việc tìm top k elements

### Bài toán: Optimized Top K Frequent Elements
```python
def top_k_frequent_optimized(nums, k):
    """
    Tối ưu hóa việc tìm k phần tử xuất hiện nhiều nhất
    """
    # Sử dụng bucket sort
    frequency = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    
    for num, freq in frequency.items():
        buckets[freq].append(num)
    
    result = []
    for freq in range(len(nums), 0, -1):
        result.extend(buckets[freq])
        if len(result) >= k:
            break
    
    return result[:k]
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 8: Design Twitter**
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

## 📚 **LEVEL 9: IPO (Initial Public Offering)**
**Mục tiêu**: Tìm vốn tối đa sau k dự án

### Bài toán: IPO
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

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n log n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 10: Advanced Top K Applications**
**Mục tiêu**: Ứng dụng top k trong bài toán phức tạp

### Bài toán: Rearrange String k Distance Apart
```python
def rearrange_string(s, k):
    """
    Sắp xếp lại chuỗi sao cho các ký tự giống nhau cách nhau ít nhất k vị trí
    """
    if k <= 1:
        return s
    
    # Đếm tần suất
    frequency = Counter(s)
    
    # Sử dụng max heap
    heap = [(-freq, char) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    result = []
    queue = []  # Lưu các ký tự đã sử dụng gần đây
    
    while heap:
        freq, char = heapq.heappop(heap)
        result.append(char)
        
        # Thêm vào queue để kiểm tra khoảng cách
        queue.append((freq + 1, char))
        
        # Nếu đã đủ k ký tự, có thể sử dụng lại ký tự đầu tiên
        if len(queue) >= k:
            freq, char = queue.pop(0)
            if freq < 0:
                heapq.heappush(heap, (freq, char))
    
    return ''.join(result) if len(result) == len(s) else ""
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n log n)  
**Không gian**: O(n)

---

## 🎯 **Lộ trình học tập**

### **Giai đoạn 1 (Level 1-3)**: Nền tảng
- Hiểu khái niệm top k elements
- Thành thạo heap operations
- Làm quen với pattern cơ bản

### **Giai đoạn 2 (Level 4-6)**: Nâng cao
- Merge k sorted lists
- Matrix problems
- Tối ưu hóa thuật toán

### **Giai đoạn 3 (Level 7-8)**: Chuyên sâu
- System design
- Optimization problems
- Tối ưu hóa bộ nhớ

### **Giai đoạn 4 (Level 9-10)**: Master
- Advanced applications
- Complex constraints
- Edge cases phức tạp

## 💡 **Mẹo cho từng level**

- **Level 1-3**: Tập trung vào hiểu pattern cơ bản
- **Level 4-6**: Chú ý đến việc chọn heap phù hợp
- **Level 7-8**: Hiểu sâu về ứng dụng trong system design
- **Level 9-10**: Thực hành nhiều và phân tích các trường hợp đặc biệt

## 🔥 **Common Patterns**

### **Top K with Min Heap**
```python
heap = []
for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)
return heap[0]
```

### **Top K with Max Heap**
```python
heap = [(-freq, item) for item, freq in frequency.items()]
heapq.heapify(heap)
result = []
for _ in range(k):
    result.append(heapq.heappop(heap)[1])
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