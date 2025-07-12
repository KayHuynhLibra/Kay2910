# 🔄 IN-PLACE REVERSAL

## 📚 **Tổng quan**
In-Place Reversal là kỹ thuật đảo ngược các phần tử trong cấu trúc dữ liệu mà không cần sử dụng thêm bộ nhớ phụ.

---

## 🎯 **20 LEVELS TỔNG QUAN**

### **Giai đoạn 1: Cơ bản (Level 1-5)**
- **Level 1**: Array reversal cơ bản
- **Level 2**: Reverse array với range
- **Level 3**: Rotate array theo K
- **Level 4**: Reverse array theo blocks
- **Level 5**: Reverse với conditions

### **Giai đoạn 2: Nâng cao (Level 6-10)**
- **Level 6**: Linked list reversal cơ bản
- **Level 7**: Reverse nodes theo K-group
- **Level 8**: Reverse alternating groups
- **Level 9**: Reverse between range
- **Level 10**: Swap nodes in pairs

### **Giai đoạn 3: Chuyên sâu (Level 11-15)**
- **Level 11**: String reversal cơ bản
- **Level 12**: Reverse words in string
- **Level 13**: Reverse string theo K
- **Level 14**: Reverse vowels in string
- **Level 15**: Reverse only letters

### **Giai đoạn 4: Master (Level 16-20)**
- **Level 16**: Reverse bits
- **Level 17**: Reverse integer
- **Level 18**: Reverse Polish notation
- **Level 19**: Advanced array reversal
- **Level 20**: Complex reversal applications

---

## 🔄 **KỸ THUẬT IN-PLACE REVERSAL**

### **Nguyên lý hoạt động:**
1. **Two Pointers**: Sử dụng 2 con trỏ từ 2 đầu
2. **Swap Operation**: Hoán đổi phần tử tại 2 vị trí
3. **Memory Efficient**: Không cần thêm bộ nhớ phụ
4. **Time Complexity**: O(n) cho array, O(n) cho linked list

### **Implementation cơ bản:**
```python
def reverseArray(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
```

---

## 🎯 **BÀI TOÁN TIÊU BIỂU**

### **Array Reversal:**
1. Reverse Array
2. Rotate Array
3. Reverse Array in Groups
4. Reverse Array with Conditions
5. Advanced Array Manipulation

### **Linked List Reversal:**
1. Reverse Linked List
2. Reverse Nodes in K-Group
3. Reverse Alternating Groups
4. Reverse Between Range
5. Swap Nodes in Pairs

### **String Reversal:**
1. Reverse String
2. Reverse Words in String
3. Reverse String II
4. Reverse Vowels
5. Reverse Only Letters

### **Advanced Problems:**
1. Reverse Bits
2. Reverse Integer
3. Reverse Polish Notation
4. Advanced Applications
5. Complex Techniques

---

## 💡 **KỸ THUẬT NÂNG CAO**

### **Memory Optimization:**
- XOR swapping
- In-place operations
- Minimal extra space
- Efficient algorithms

### **Performance Optimization:**
- Early termination
- Pattern recognition
- Optimized loops
- Cache-friendly operations

### **Edge Case Handling:**
- Empty arrays/lists
- Single elements
- Null pointers
- Boundary conditions

### **Combination Techniques:**
- Multiple reversals
- Conditional reversal
- Pattern-based reversal
- Hybrid approaches

---

## 🚀 **LỘ TRÌNH HỌC TẬP**

### **Tuần 1-2: Cơ bản**
- Hiểu nguyên lý reversal
- Implement cơ bản
- Practice với array operations

### **Tuần 3-4: Nâng cao**
- Linked list reversal
- String manipulation
- Range operations
- Conditional reversal

### **Tuần 5-6: Chuyên sâu**
- Bit manipulation
- Integer operations
- Advanced algorithms
- Complex problems

### **Tuần 7-8: Master**
- Advanced applications
- Optimization techniques
- Real-world problems
- Competitive programming

---

## 💻 **IMPLEMENTATION TIPS**

### **Array Reversal Pattern:**
```python
def reversePattern(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
```

### **Linked List Reversal Pattern:**
```python
def reverseLinkedList(head):
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev
```

### **String Reversal Pattern:**
```python
def reverseString(s):
    s = list(s)
    left, right = 0, len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    return ''.join(s)
```

---

## 🎯 **INTERVIEW PREPARATION**

### **Common Questions:**
1. "Reverse an array in-place"
2. "Reverse a linked list"
3. "Rotate an array by k positions"
4. "Reverse words in a string"
5. "Reverse bits of a number"

### **Advanced Questions:**
1. "Reverse nodes in k-groups"
2. "Reverse with memory constraints"
3. "Optimize reversal for large datasets"
4. "Handle edge cases efficiently"
5. "Combine with other techniques"

---

## 📚 **RESOURCES**

### **Online Platforms:**
- LeetCode Array/String Problems
- HackerRank Data Structures
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

**🎉 Chúc bạn thành thạo In-Place Reversal! 🎉** 