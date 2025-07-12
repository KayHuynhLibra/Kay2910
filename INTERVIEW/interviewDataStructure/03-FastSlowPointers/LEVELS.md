# FAST & SLOW POINTERS - 10 LEVELS TỪ CƠ BẢN ĐẾN NÂNG CAO

## 🎯 Tổng quan
10 level này được thiết kế để bạn học Fast & Slow Pointers từ cơ bản đến nâng cao, mỗi level tăng dần độ khó và phức tạp.

---

## 📚 **LEVEL 1: Hiểu cơ bản về Fast & Slow Pointers**
**Mục tiêu**: Hiểu khái niệm và cách hoạt động của fast & slow pointers

### Bài toán: Linked List Cycle Detection
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    """
    Phát hiện chu kỳ trong danh sách liên kết
    """
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False
```

**Độ khó**: ⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 2: Tìm điểm giữa của Linked List**
**Mục tiêu**: Thành thạo việc tìm điểm giữa

### Bài toán: Find Middle of Linked List
```python
def middle_node(head):
    """
    Tìm node giữa của danh sách liên kết
    """
    if not head:
        return None
    
    slow = head
    fast = head
    
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Nếu số node chẵn, trả về node thứ hai ở giữa
    if fast.next:
        return slow.next
    
    return slow
```

**Độ khó**: ⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 3: Tìm node thứ k từ cuối**
**Mục tiêu**: Sử dụng fast & slow để tìm node thứ k từ cuối

### Bài toán: Remove Nth Node From End of List
```python
def remove_nth_from_end(head, n):
    """
    Xóa node thứ n từ cuối danh sách
    """
    dummy = ListNode(0)
    dummy.next = head
    
    slow = dummy
    fast = dummy
    
    # Di chuyển fast n bước trước
    for _ in range(n + 1):
        fast = fast.next
    
    # Di chuyển cả hai con trỏ
    while fast:
        slow = slow.next
        fast = fast.next
    
    # Xóa node
    slow.next = slow.next.next
    
    return dummy.next
```

**Độ khó**: ⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 4: Phát hiện và tìm điểm bắt đầu chu kỳ**
**Mục tiêu**: Tìm điểm bắt đầu của chu kỳ

### Bài toán: Linked List Cycle II
```python
def detect_cycle(head):
    """
    Phát hiện và trả về node bắt đầu của chu kỳ
    """
    if not head or not head.next:
        return None
    
    # Bước 1: Tìm điểm gặp nhau
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    
    # Nếu không có chu kỳ
    if slow != fast:
        return None
    
    # Bước 2: Tìm điểm bắt đầu chu kỳ
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow
```

**Độ khó**: ⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 5: Palindrome Linked List**
**Mục tiêu**: Kết hợp fast & slow với đảo ngược linked list

### Bài toán: Palindrome Linked List
```python
def is_palindrome(head):
    """
    Kiểm tra xem danh sách liên kết có phải palindrome không
    """
    if not head or not head.next:
        return True
    
    # Bước 1: Tìm điểm giữa
    slow = head
    fast = head
    
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Bước 2: Đảo ngược nửa sau
    second_half = reverse_list(slow.next)
    
    # Bước 3: So sánh hai nửa
    first_half = head
    second_half_ptr = second_half
    
    while second_half_ptr:
        if first_half.val != second_half_ptr.val:
            return False
        first_half = first_half.next
        second_half_ptr = second_half_ptr.next
    
    return True

def reverse_list(head):
    """
    Đảo ngược danh sách liên kết
    """
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev
```

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 6: Reorder Linked List**
**Mục tiêu**: Sắp xếp lại linked list theo pattern phức tạp

### Bài toán: Reorder List
```python
def reorder_list(head):
    """
    Sắp xếp lại danh sách liên kết theo pattern: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
    """
    if not head or not head.next:
        return
    
    # Bước 1: Tìm điểm giữa
    slow = head
    fast = head
    
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Bước 2: Đảo ngược nửa sau
    second_half = reverse_list(slow.next)
    slow.next = None
    
    # Bước 3: Merge hai nửa
    first_half = head
    while first_half and second_half:
        temp1 = first_half.next
        temp2 = second_half.next
        
        first_half.next = second_half
        second_half.next = temp1
        
        first_half = temp1
        second_half = temp2
```

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 7: Happy Number**
**Mục tiêu**: Áp dụng fast & slow cho số học

### Bài toán: Happy Number
```python
def is_happy(n):
    """
    Kiểm tra xem số có phải là happy number không
    """
    def get_next(n):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit ** 2
        return total_sum
    
    slow = n
    fast = get_next(n)
    
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    
    return fast == 1
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(log n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 8: Find the Duplicate Number**
**Mục tiêu**: Kết hợp fast & slow với mảng

### Bài toán: Find the Duplicate Number
```python
def find_duplicate(nums):
    """
    Tìm số trùng lặp trong mảng [1, n] với n+1 phần tử
    """
    slow = nums[0]
    fast = nums[0]
    
    # Tìm điểm gặp nhau
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Tìm điểm bắt đầu chu kỳ
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 9: Intersection of Two Linked Lists**
**Mục tiêu**: Tìm điểm giao nhau của hai linked list

### Bài toán: Intersection of Two Linked Lists
```python
def get_intersection_node(headA, headB):
    """
    Tìm node giao nhau của hai danh sách liên kết
    """
    if not headA or not headB:
        return None
    
    # Tính độ dài hai danh sách
    lenA = get_length(headA)
    lenB = get_length(headB)
    
    # Điều chỉnh để hai con trỏ cùng xuất phát
    if lenA > lenB:
        for _ in range(lenA - lenB):
            headA = headA.next
    else:
        for _ in range(lenB - lenA):
            headB = headB.next
    
    # Tìm điểm giao nhau
    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next
    
    return None

def get_length(head):
    """
    Tính độ dài danh sách liên kết
    """
    length = 0
    while head:
        length += 1
        head = head.next
    return length
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 10: Advanced Cycle Detection**
**Mục tiêu**: Phát hiện chu kỳ trong đồ thị và cấu trúc phức tạp

### Bài toán: Circular Array Loop
```python
def circular_array_loop(nums):
    """
    Kiểm tra xem có chu kỳ trong mảng vòng không
    """
    n = len(nums)
    
    for i in range(n):
        if nums[i] == 0:
            continue
        
        slow = i
        fast = i
        
        # Kiểm tra hướng
        direction = nums[i] > 0
        
        while True:
            # Di chuyển slow
            slow = (slow + nums[slow]) % n
            if nums[slow] == 0 or (nums[slow] > 0) != direction:
                break
            
            # Di chuyển fast
            fast = (fast + nums[fast]) % n
            if nums[fast] == 0 or (nums[fast] > 0) != direction:
                break
            fast = (fast + nums[fast]) % n
            if nums[fast] == 0 or (nums[fast] > 0) != direction:
                break
            
            if slow == fast:
                # Kiểm tra độ dài chu kỳ > 1
                if slow == (slow + nums[slow]) % n:
                    break
                return True
    
    return False
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 🎯 **Lộ trình học tập**

### **Giai đoạn 1 (Level 1-3)**: Nền tảng
- Hiểu khái niệm fast & slow pointers
- Thành thạo việc tìm điểm giữa
- Làm quen với pattern cơ bản

### **Giai đoạn 2 (Level 4-6)**: Nâng cao
- Phát hiện và xử lý chu kỳ
- Kết hợp với đảo ngược linked list
- Xử lý bài toán phức tạp

### **Giai đoạn 3 (Level 7-8)**: Chuyên sâu
- Áp dụng cho số học và mảng
- Tìm điểm giao nhau
- Tối ưu hóa thuật toán

### **Giai đoạn 4 (Level 9-10)**: Master
- Xử lý đồ thị và cấu trúc phức tạp
- Tối ưu hóa cao cấp
- Edge cases phức tạp

## 💡 **Mẹo cho từng level**

- **Level 1-3**: Tập trung vào hiểu pattern cơ bản
- **Level 4-6**: Chú ý đến việc xử lý chu kỳ và đảo ngược
- **Level 7-8**: Hiểu sâu về ứng dụng trong các cấu trúc dữ liệu khác
- **Level 9-10**: Thực hành nhiều và phân tích các trường hợp đặc biệt

## 🔥 **Common Patterns**

### **Basic Cycle Detection**
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
```

### **Find Middle**
```python
slow = fast = head
while fast.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next
return slow
```

### **Find Kth from End**
```python
slow = fast = head
for _ in range(k):
    fast = fast.next
while fast:
    slow = slow.next
    fast = fast.next
``` 