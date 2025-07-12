# Sliding Window (Cửa sổ trượt)

## Tổng quan
Sliding Window là một kỹ thuật quan trọng trong lập trình giải thuật, được sử dụng để thực hiện các thao tác trên một khoảng cố định của mảng hoặc danh sách liên kết.

## Đặc điểm chính
- **Kích thước cửa sổ**: Có thể cố định hoặc thay đổi tùy theo bài toán
- **Hiệu quả**: Giảm độ phức tạp từ O(n²) xuống O(n) trong nhiều trường hợp
- **Ứng dụng rộng rãi**: Từ xử lý chuỗi đến phân tích dữ liệu

## Các loại Sliding Window

### 1. Fixed Size Window (Cửa sổ kích thước cố định)
- Kích thước cửa sổ không thay đổi
- Ví dụ: Tìm tổng lớn nhất của k phần tử liên tiếp

### 2. Variable Size Window (Cửa sổ kích thước thay đổi)
- Kích thước cửa sổ thay đổi dựa trên điều kiện
- Ví dụ: Tìm dãy con ngắn nhất có tổng ≥ target

## Thuật toán cơ bản

```python
def sliding_window_fixed_size(arr, k):
    """
    Sliding window với kích thước cố định k
    """
    if len(arr) < k:
        return None
    
    # Tính tổng cửa sổ đầu tiên
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Trượt cửa sổ
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

def sliding_window_variable_size(arr, target):
    """
    Sliding window với kích thước thay đổi
    """
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        # Thu nhỏ cửa sổ khi thỏa mãn điều kiện
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0
```

## Bài toán điển hình

### 1. Maximum Sum Subarray of Size K
```python
def max_sum_subarray_of_size_k(arr, k):
    """
    Tìm tổng lớn nhất của dãy con có k phần tử liên tiếp
    """
    if len(arr) < k:
        return None
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### 2. Longest Substring Without Repeating Characters
```python
def longest_substring_without_repeating(s):
    """
    Tìm chuỗi con dài nhất không có ký tự lặp lại
    """
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

### 3. Minimum Size Subarray Sum
```python
def min_subarray_len(target, nums):
    """
    Tìm độ dài nhỏ nhất của dãy con có tổng >= target
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

## Độ phức tạp
- **Thời gian**: O(n) - mỗi phần tử được xử lý tối đa 2 lần
- **Không gian**: O(1) - chỉ sử dụng một số biến đếm

## Lưu ý quan trọng
1. **Khởi tạo cửa sổ**: Cần xác định cách khởi tạo cửa sổ ban đầu
2. **Điều kiện trượt**: Xác định khi nào cần mở rộng hoặc thu nhỏ cửa sổ
3. **Cập nhật kết quả**: Cập nhật kết quả tại thời điểm phù hợp
4. **Xử lý biên**: Chú ý các trường hợp đặc biệt khi mảng rỗng hoặc kích thước không hợp lệ

## Bài tập thực hành
1. Maximum Average Subarray I
2. Permutation in String
3. Longest Repeating Character Replacement
4. Sliding Window Maximum
5. Minimum Window Substring

## Mẹo và thủ thuật
- Sử dụng HashMap để theo dõi tần suất xuất hiện
- Kết hợp với Two Pointers để tối ưu hóa
- Chú ý đến việc xử lý các trường hợp edge case 