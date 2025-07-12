# 🔄 CYCLIC SORT

## 📚 **Tổng quan**
Cyclic Sort là kỹ thuật sắp xếp mảng với O(n) time complexity khi các phần tử nằm trong range [1, n] hoặc [0, n-1].

---

## 🎯 **20 LEVELS TỔNG QUAN**

### **Giai đoạn 1: Cơ bản (Level 1-5)**
- **Level 1**: Cyclic sort cơ bản cho [1, n]
- **Level 2**: Cyclic sort cho [0, n-1]
- **Level 3**: Tìm số bị thiếu
- **Level 4**: Tìm tất cả số bị thiếu
- **Level 5**: Tìm số trùng lặp

### **Giai đoạn 2: Nâng cao (Level 6-10)**
- **Level 6**: Tìm tất cả số trùng lặp
- **Level 7**: Tìm số bị thiếu và trùng lặp
- **Level 8**: First missing positive
- **Level 9**: Kth missing positive
- **Level 10**: Tìm element trong rotated array

### **Giai đoạn 3: Chuyên sâu (Level 11-15)**
- **Level 11**: Tìm minimum trong rotated array
- **Level 12**: Tìm peak element
- **Level 13**: Search trong 2D matrix
- **Level 14**: Tìm range trong sorted array
- **Level 15**: Median of two sorted arrays

### **Giai đoạn 4: Master (Level 16-20)**
- **Level 16**: Search trong infinite array
- **Level 17**: Search trong bitonic array
- **Level 18**: Search với duplicates
- **Level 19**: Search với absent elements
- **Level 20**: Advanced applications

---

## 🔄 **KỸ THUẬT CYCLIC SORT**

### **Nguyên lý hoạt động:**
1. **Điều kiện**: Mảng chứa n phần tử trong range [1, n] hoặc [0, n-1]
2. **Ý tưởng**: Mỗi phần tử sẽ ở đúng vị trí của nó
3. **Thuật toán**: Swap cho đến khi phần tử ở đúng vị trí

### **Implementation cơ bản:**
```python
def cyclicSort(arr):
    n = len(arr)
    i = 0
    while i < n:
        correct_index = arr[i] - 1  # hoặc arr[i] cho [0, n-1]
        if arr[i] != arr[correct_index]:
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
        else:
            i += 1
    return arr
```

---

## 🎯 **BÀI TOÁN TIÊU BIỂU**

### **Missing Numbers:**
1. Find Missing Number
2. Find All Missing Numbers
3. First Missing Positive
4. Kth Missing Positive Number

### **Duplicate Numbers:**
1. Find Duplicate Number
2. Find All Duplicates
3. Set Mismatch
4. Find the Duplicate Number

### **Array Manipulation:**
1. Cyclic Sort
2. Find Element in Rotated Array
3. Find Minimum in Rotated Array
4. Search in 2D Matrix

### **Advanced Problems:**
1. Median of Two Sorted Arrays
2. Search in Infinite Array
3. Search in Bitonic Array
4. Complex Array Manipulation

---

## 💡 **KỸ THUẬT NÂNG CAO**

### **Handling Edge Cases:**
- Negative numbers
- Out of range elements
- Duplicates
- Empty arrays

### **Optimization Techniques:**
- Early termination
- Memory optimization
- Time complexity analysis
- Space complexity optimization

### **Combination with Other Techniques:**
- Binary search
- Two pointers
- Sliding window
- Dynamic programming

---

## 🚀 **LỘ TRÌNH HỌC TẬP**

### **Tuần 1-2: Cơ bản**
- Hiểu nguyên lý cyclic sort
- Implement cơ bản
- Practice với bài toán đơn giản

### **Tuần 3-4: Nâng cao**
- Missing numbers
- Duplicate numbers
- Array manipulation
- Edge cases

### **Tuần 5-6: Chuyên sâu**
- Rotated arrays
- 2D arrays
- Advanced search
- Complex problems

### **Tuần 7-8: Master**
- Infinite arrays
- Bitonic arrays
- Advanced applications
- Real-world problems

---

## 💻 **IMPLEMENTATION TIPS**

### **Basic Pattern:**
```python
def cyclicSortPattern(arr):
    n = len(arr)
    i = 0
    while i < n:
        correct_index = arr[i] - 1  # Adjust based on range
        if arr[i] != arr[correct_index]:
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
        else:
            i += 1
```

### **Finding Missing Numbers:**
```python
def findMissing(arr):
    # After cyclic sort
    for i in range(len(arr)):
        if arr[i] != i + 1:
            return i + 1
    return len(arr) + 1
```

### **Finding Duplicates:**
```python
def findDuplicate(arr):
    # After cyclic sort
    for i in range(len(arr)):
        if arr[i] != i + 1:
            return arr[i]
    return -1
```

---

## 🎯 **INTERVIEW PREPARATION**

### **Common Questions:**
1. "Sort an array in O(n) time"
2. "Find missing number in array"
3. "Find duplicate number"
4. "Find first missing positive"
5. "Search in rotated array"

### **Advanced Questions:**
1. "Handle negative numbers in cyclic sort"
2. "Optimize for memory usage"
3. "Handle multiple duplicates"
4. "Search in infinite array"
5. "Combine with other techniques"

---

## 📚 **RESOURCES**

### **Online Platforms:**
- LeetCode Array Problems
- HackerRank Sorting Challenges
- Codeforces Array Problems
- AtCoder Educational Contests

### **Books:**
- "Introduction to Algorithms" (CLRS)
- "Competitive Programming" by Steven Halim
- "Cracking the Coding Interview"

### **Practice:**
- Daily coding challenges
- Mock interviews
- Peer programming
- Code reviews

---

**🎉 Chúc bạn thành thạo Cyclic Sort! 🎉** 