# Fast and Slow Pointers (Con trỏ nhanh và chậm)

## Tổng quan
Fast and Slow Pointers (còn gọi là Floyd's Cycle Finding Algorithm) là một kỹ thuật mạnh mẽ được sử dụng để phát hiện chu kỳ trong danh sách liên kết và các cấu trúc dữ liệu khác.

## Đặc điểm chính
- **Phát hiện chu kỳ**: Hiệu quả trong việc phát hiện chu kỳ trong danh sách liên kết
- **Tìm điểm giữa**: Có thể tìm điểm giữa của danh sách liên kết
- **Tìm phần tử thứ k từ cuối**: Ứng dụng trong nhiều bài toán khác nhau

## Nguyên lý hoạt động
- **Con trỏ chậm (slow)**: Di chuyển 1 bước mỗi lần
- **Con trỏ nhanh (fast)**: Di chuyển 2 bước mỗi lần
- **Phát hiện chu kỳ**: Nếu có chu kỳ, hai con trỏ sẽ gặp nhau

## Thuật toán cơ bản

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

def find_middle(head):
    """
    Tìm điểm giữa của danh sách liên kết
    """
    if not head:
        return None
    
    slow = head
    fast = head
    
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow
```

## Bài toán điển hình

### 1. Linked List Cycle Detection
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

### 2. Find Middle of Linked List
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

### 3. Remove Nth Node From End of List
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

### 4. Palindrome Linked List
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

### 5. Reorder List
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

### 6. Happy Number
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

## Độ phức tạp
- **Thời gian**: O(n) - mỗi node được truy cập tối đa 2 lần
- **Không gian**: O(1) - chỉ sử dụng hai con trỏ

## Lưu ý quan trọng
1. **Khởi tạo con trỏ**: Đảm bảo cả hai con trỏ bắt đầu từ cùng một điểm
2. **Điều kiện dừng**: Chú ý đến điều kiện dừng để tránh lỗi null pointer
3. **Tốc độ di chuyển**: Fast pointer thường di chuyển gấp đôi slow pointer
4. **Xử lý edge cases**: Chú ý đến các trường hợp danh sách rỗng hoặc chỉ có 1 node

## Bài tập thực hành
1. Linked List Cycle II
2. Find the Duplicate Number
3. Rotate List
4. Intersection of Two Linked Lists
5. Sort List

## Mẹo và thủ thuật
- Sử dụng dummy node để xử lý các trường hợp đặc biệt
- Kết hợp với việc đảo ngược danh sách liên kết
- Chú ý đến việc xử lý các trường hợp edge case
- Có thể áp dụng cho các bài toán tìm chu kỳ trong mảng 