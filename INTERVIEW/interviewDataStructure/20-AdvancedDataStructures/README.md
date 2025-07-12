# 🏗️ ADVANCED DATA STRUCTURES

## 📚 **Tổng quan**
Advanced Data Structures là các cấu trúc dữ liệu phức tạp được sử dụng để giải quyết các bài toán nâng cao trong lập trình thi đấu và phỏng vấn.

---

## 🎯 **20 LEVELS TỔNG QUAN**

### **Giai đoạn 1: Cơ bản (Level 1-5)**
- **Level 1**: Trie cơ bản
- **Level 2**: Trie với count
- **Level 3**: Trie với wildcard
- **Level 4**: Segment Tree cơ bản
- **Level 5**: Segment Tree với min/max

### **Giai đoạn 2: Nâng cao (Level 6-10)**
- **Level 6**: Fenwick Tree cơ bản
- **Level 7**: Fenwick Tree với range update
- **Level 8**: Disjoint Set cơ bản
- **Level 9**: Disjoint Set với size
- **Level 10**: Segment Tree với lazy propagation

### **Giai đoạn 3: Chuyên sâu (Level 11-15)**
- **Level 11**: Trie với XOR
- **Level 12**: Segment Tree với GCD
- **Level 13**: Fenwick Tree 2D
- **Level 14**: Disjoint Set với rollback
- **Level 15**: Segment Tree persistent

### **Giai đoạn 4: Master (Level 16-20)**
- **Level 16**: Trie compressed
- **Level 17**: Segment Tree merge sort
- **Level 18**: Fenwick Tree min/max
- **Level 19**: Disjoint Set weighted
- **Level 20**: Hybrid structures

---

## 🏗️ **CÁC CẤU TRÚC DỮ LIỆU CHÍNH**

### **1. Trie (Prefix Tree)**
- **Mục đích**: Lưu trữ và tìm kiếm chuỗi hiệu quả
- **Ứng dụng**: Autocomplete, spell checker, IP routing
- **Time Complexity**: O(m) cho insert/search (m = độ dài chuỗi)

### **2. Segment Tree**
- **Mục đích**: Range queries và updates
- **Ứng dụng**: Range sum, min/max, GCD queries
- **Time Complexity**: O(log n) cho query/update

### **3. Fenwick Tree (Binary Indexed Tree)**
- **Mục đích**: Prefix sum queries và point updates
- **Ứng dụng**: Cumulative frequency, inversion counting
- **Time Complexity**: O(log n) cho query/update

### **4. Disjoint Set (Union-Find)**
- **Mục đích**: Quản lý các tập hợp rời rạc
- **Ứng dụng**: Network connectivity, cycle detection
- **Time Complexity**: O(α(n)) với path compression

---

## 💡 **KỸ THUẬT NÂNG CAO**

### **Lazy Propagation**
- Trì hoãn việc cập nhật cho đến khi cần thiết
- Giảm số lượng operations
- Áp dụng cho Segment Tree

### **Path Compression**
- Nén đường đi trong Disjoint Set
- Giảm height của tree
- Cải thiện performance

### **Persistent Structures**
- Lưu trữ tất cả versions
- Hỗ trợ time travel queries
- Áp dụng cho Segment Tree, Trie

### **Compression**
- Giảm memory usage
- Tối ưu cho sparse data
- Áp dụng cho Trie, Segment Tree

---

## 🎯 **BÀI TOÁN TIÊU BIỂU**

### **Trie Problems:**
1. Implement Trie (Prefix Tree)
2. Word Search II
3. Maximum XOR of Two Numbers
4. Design Search Autocomplete System
5. Stream of Characters

### **Segment Tree Problems:**
1. Range Sum Query - Mutable
2. Range Minimum Query
3. Count of Smaller Numbers After Self
4. The Skyline Problem
5. My Calendar III

### **Fenwick Tree Problems:**
1. Count of Smaller Numbers After Self
2. Range Sum Query 2D - Mutable
3. Count Inversions
4. K-th Smallest Element in a Sorted Matrix
5. Reverse Pairs

### **Disjoint Set Problems:**
1. Number of Islands
2. Redundant Connection
3. Accounts Merge
4. Most Stones Removed with Same Row or Column
5. Regions Cut By Slashes

---

## 🚀 **LỘ TRÌNH HỌC TẬP**

### **Tuần 1-2: Cơ bản**
- Hiểu concept của từng cấu trúc
- Implement cơ bản
- Practice với bài toán đơn giản

### **Tuần 3-4: Nâng cao**
- Lazy propagation
- Path compression
- Range operations
- Advanced queries

### **Tuần 5-6: Chuyên sâu**
- Persistent structures
- 2D structures
- Weighted operations
- Complex applications

### **Tuần 7-8: Master**
- Hybrid structures
- Optimization techniques
- Real-world applications
- Competitive programming

---

## 💻 **IMPLEMENTATION TIPS**

### **Trie:**
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
```

### **Segment Tree:**
```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
```

### **Fenwick Tree:**
```python
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
```

### **Disjoint Set:**
```python
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
```

---

## 🎯 **INTERVIEW PREPARATION**

### **Common Questions:**
1. "Implement a Trie"
2. "Design an autocomplete system"
3. "Find range sum with updates"
4. "Detect cycles in a graph"
5. "Count inversions in an array"

### **Advanced Questions:**
1. "Design a persistent data structure"
2. "Implement 2D range queries"
3. "Optimize for memory usage"
4. "Handle concurrent updates"
5. "Scale to large datasets"

---

## 📚 **RESOURCES**

### **Online Platforms:**
- LeetCode Advanced Problems
- Codeforces Data Structure Problems
- HackerRank Advanced Algorithms
- AtCoder Educational Contests

### **Books:**
- "Advanced Data Structures" by Peter Brass
- "Competitive Programming" by Steven Halim
- "Introduction to Algorithms" (CLRS)

### **Practice:**
- Daily coding challenges
- Mock interviews
- Peer programming
- Code reviews

---

**🎉 Chúc bạn thành thạo Advanced Data Structures! 🎉** 