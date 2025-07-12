# Two Pointers (Hai con trỏ)

## Tổng quan
Two Pointers là một kỹ thuật mạnh mẽ được sử dụng để giải quyết các bài toán liên quan đến mảng và danh sách liên kết. Kỹ thuật này sử dụng hai con trỏ để duyệt dữ liệu một cách hiệu quả.

## Đặc điểm chính
- **Hiệu quả**: Giảm độ phức tạp thời gian so với việc sử dụng một con trỏ
- **Linh hoạt**: Có thể áp dụng cho nhiều loại bài toán khác nhau
- **Tối ưu**: Đặc biệt hiệu quả với dữ liệu đã sắp xếp

## Các loại Two Pointers

### 1. Opposite Directional (Hai con trỏ ngược chiều)
- Hai con trỏ bắt đầu từ hai đầu và di chuyển về phía nhau
- Thích hợp cho mảng đã sắp xếp

### 2. Same Directional (Hai con trỏ cùng chiều)
- Hai con trỏ bắt đầu từ cùng một điểm và di chuyển cùng chiều
- Thường dùng cho sliding window

### 3. Fast and Slow (Con trỏ nhanh và chậm)
- Một con trỏ di chuyển nhanh hơn con trỏ còn lại
- Dùng để phát hiện chu kỳ

## Thuật toán cơ bản

```python
def two_pointers_opposite_directional(arr, target):
    """
    Two pointers ngược chiều - tìm cặp số có tổng bằng target
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return [-1, -1]

def two_pointers_same_directional(arr):
    """
    Two pointers cùng chiều - loại bỏ phần tử trùng lặp
    """
    if not arr:
        return 0
    
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    
    return slow + 1
```

## Bài toán điển hình

### 1. Two Sum II - Input Array Is Sorted
```python
def two_sum_sorted(numbers, target):
    """
    Tìm cặp số có tổng bằng target trong mảng đã sắp xếp
    """
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return [-1, -1]
```

### 2. Remove Duplicates from Sorted Array
```python
def remove_duplicates(nums):
    """
    Loại bỏ phần tử trùng lặp trong mảng đã sắp xếp
    """
    if not nums:
        return 0
    
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1
```

### 3. Container With Most Water
```python
def max_area(height):
    """
    Tìm container có thể chứa nhiều nước nhất
    """
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        area = width * h
        max_area = max(max_area, area)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area
```

### 4. 3Sum
```python
def three_sum(nums):
    """
    Tìm tất cả bộ ba số có tổng bằng 0
    """
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Bỏ qua các phần tử trùng lặp
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    
    return result
```

### 5. Valid Palindrome
```python
def is_palindrome(s):
    """
    Kiểm tra xem chuỗi có phải là palindrome không
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Bỏ qua các ký tự không phải chữ cái hoặc số
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True
```

## Độ phức tạp
- **Thời gian**: O(n) - mỗi phần tử được xử lý tối đa 1 lần
- **Không gian**: O(1) - chỉ sử dụng một số biến đếm

## Lưu ý quan trọng
1. **Sắp xếp dữ liệu**: Nhiều bài toán yêu cầu dữ liệu phải được sắp xếp trước
2. **Xử lý trùng lặp**: Chú ý đến việc bỏ qua các phần tử trùng lặp
3. **Điều kiện dừng**: Xác định rõ điều kiện dừng của vòng lặp
4. **Cập nhật con trỏ**: Đảm bảo con trỏ được cập nhật đúng cách

## Bài tập thực hành
1. Valid Palindrome II
2. Sort Colors
3. Trapping Rain Water
4. Squares of a Sorted Array
5. Backspace String Compare

## Mẹo và thủ thuật
- Với mảng đã sắp xếp, thường dùng opposite directional pointers
- Với mảng chưa sắp xếp, có thể cần sắp xếp trước hoặc dùng same directional
- Kết hợp với HashMap để tối ưu hóa một số bài toán
- Chú ý đến việc xử lý các trường hợp edge case 