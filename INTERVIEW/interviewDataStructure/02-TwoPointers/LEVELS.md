# TWO POINTERS - 20 LEVELS TỪ CƠ BẢN ĐẾN NÂNG CAO

## 🎯 Tổng quan
20 level này được thiết kế để bạn học Two Pointers từ cơ bản đến nâng cao.

---

## 📚 **LEVEL 1: Hiểu cơ bản về Two Pointers**
**Mục tiêu**: Hiểu khái niệm và cách hoạt động

### Bài toán: Two Sum II - Input Array Is Sorted
```python
def two_sum_sorted(numbers, target):
    """
    Tìm hai số có tổng bằng target trong mảng đã sắp xếp
    """
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []
```

**Độ khó**: ⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 2: Remove Duplicates from Sorted Array**
**Mục tiêu**: Loại bỏ phần tử trùng lặp trong mảng đã sắp xếp

### Bài toán: Remove Duplicates from Sorted Array
```python
def remove_duplicates(nums):
    """
    Loại bỏ phần tử trùng lặp trong mảng đã sắp xếp
    """
    if not nums:
        return 0
    
    write_index = 1
    
    for read_index in range(1, len(nums)):
        if nums[read_index] != nums[read_index - 1]:
            nums[write_index] = nums[read_index]
            write_index += 1
    
    return write_index
```

**Độ khó**: ⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 3: Remove Element**
**Mục tiêu**: Loại bỏ tất cả phần tử có giá trị val

### Bài toán: Remove Element
```python
def remove_element(nums, val):
    """
    Loại bỏ tất cả phần tử có giá trị val
    """
    write_index = 0
    
    for read_index in range(len(nums)):
        if nums[read_index] != val:
            nums[write_index] = nums[read_index]
            write_index += 1
    
    return write_index
```

**Độ khó**: ⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 4: Move Zeroes**
**Mục tiêu**: Di chuyển tất cả số 0 về cuối mảng

### Bài toán: Move Zeroes
```python
def move_zeroes(nums):
    """
    Di chuyển tất cả số 0 về cuối mảng
    """
    write_index = 0
    
    for read_index in range(len(nums)):
        if nums[read_index] != 0:
            nums[write_index] = nums[read_index]
            write_index += 1
    
    # Điền số 0 vào cuối
    while write_index < len(nums):
        nums[write_index] = 0
        write_index += 1
```

**Độ khó**: ⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 5: Reverse String**
**Mục tiêu**: Đảo ngược chuỗi

### Bài toán: Reverse String
```python
def reverse_string(s):
    """
    Đảo ngược chuỗi
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```

**Độ khó**: ⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 6: Valid Palindrome**
**Mục tiêu**: Kiểm tra xem chuỗi có phải palindrome không

### Bài toán: Valid Palindrome
```python
def is_palindrome(s):
    """
    Kiểm tra xem chuỗi có phải palindrome không
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Bỏ qua ký tự không phải alphanumeric
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

**Độ khó**: ⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 7: Container With Most Water**
**Mục tiêu**: Tìm container có thể chứa nhiều nước nhất

### Bài toán: Container With Most Water
```python
def max_area(height):
    """
    Tìm container có thể chứa nhiều nước nhất
    """
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_area = max(max_area, width * h)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area
```

**Độ khó**: ⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 8: Trapping Rain Water**
**Mục tiêu**: Tính lượng nước có thể giữ lại

### Bài toán: Trapping Rain Water
```python
def trap(height):
    """
    Tính lượng nước có thể giữ lại
    """
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    
    return water
```

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 9: 3Sum**
**Mục tiêu**: Tìm tất cả bộ ba số có tổng bằng 0

### Bài toán: 3Sum
```python
def three_sum(nums):
    """
    Tìm tất cả bộ ba số có tổng bằng 0
    """
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Bỏ qua duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(n²)  
**Không gian**: O(1)

---

## 📚 **LEVEL 10: 3Sum Closest**
**Mục tiêu**: Tìm bộ ba số có tổng gần target nhất

### Bài toán: 3Sum Closest
```python
def three_sum_closest(nums, target):
    """
    Tìm bộ ba số có tổng gần target nhất
    """
    nums.sort()
    closest_sum = float('inf')
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return target
    
    return closest_sum
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n²)  
**Không gian**: O(1)

---

## 📚 **LEVEL 11: 4Sum**
**Mục tiêu**: Tìm tất cả bộ bốn số có tổng bằng target

### Bài toán: 4Sum
```python
def four_sum(nums, target):
    """
    Tìm tất cả bộ bốn số có tổng bằng target
    """
    nums.sort()
    result = []
    
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            
            left, right = j + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n³)  
**Không gian**: O(1)

---

## 📚 **LEVEL 12: Sort Colors**
**Mục tiêu**: Sắp xếp mảng chỉ chứa 0, 1, 2

### Bài toán: Sort Colors
```python
def sort_colors(nums):
    """
    Sắp xếp mảng chỉ chứa 0, 1, 2
    """
    left, mid, right = 0, 0, len(nums) - 1
    
    while mid <= right:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 13: Merge Sorted Array**
**Mục tiêu**: Hợp nhất hai mảng đã sắp xếp

### Bài toán: Merge Sorted Array
```python
def merge(nums1, m, nums2, n):
    """
    Hợp nhất hai mảng đã sắp xếp
    """
    p1, p2, p = m - 1, n - 1, m + n - 1
    
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    # Thêm phần còn lại của nums2
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(m + n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 14: Intersection of Two Arrays II**
**Mục tiêu**: Tìm giao của hai mảng

### Bài toán: Intersection of Two Arrays II
```python
def intersect(nums1, nums2):
    """
    Tìm giao của hai mảng
    """
    nums1.sort()
    nums2.sort()
    
    i, j = 0, 0
    result = []
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(m log m + n log n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 15: Backspace String Compare**
**Mục tiêu**: So sánh hai chuỗi sau khi xử lý backspace

### Bài toán: Backspace String Compare
```python
def backspace_compare(s, t):
    """
    So sánh hai chuỗi sau khi xử lý backspace
    """
    def build_string(s):
        result = []
        for char in s:
            if char == '#':
                if result:
                    result.pop()
            else:
                result.append(char)
        return ''.join(result)
    
    return build_string(s) == build_string(t)
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 16: Squares of a Sorted Array**
**Mục tiêu**: Sắp xếp bình phương của mảng đã sắp xếp

### Bài toán: Squares of a Sorted Array
```python
def sorted_squares(nums):
    """
    Sắp xếp bình phương của mảng đã sắp xếp
    """
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1
        else:
            result[i] = nums[right] ** 2
            right -= 1
    
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 17: Longest Word in Dictionary through Deleting**
**Mục tiêu**: Tìm từ dài nhất trong dictionary có thể tạo từ s

### Bài toán: Longest Word in Dictionary through Deleting
```python
def find_longest_word(s, dictionary):
    """
    Tìm từ dài nhất trong dictionary có thể tạo từ s
    """
    def is_subsequence(word, s):
        i = 0
        for char in word:
            i = s.find(char, i)
            if i == -1:
                return False
            i += 1
        return True
    
    longest_word = ""
    
    for word in dictionary:
        if is_subsequence(word, s):
            if len(word) > len(longest_word) or (len(word) == len(longest_word) and word < longest_word):
                longest_word = word
    
    return longest_word
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n * m * l)  
**Không gian**: O(1)

---

## 📚 **LEVEL 18: Valid Triangle Number**
**Mục tiêu**: Đếm số bộ ba có thể tạo thành tam giác

### Bài toán: Valid Triangle Number
```python
def triangle_number(nums):
    """
    Đếm số bộ ba có thể tạo thành tam giác
    """
    nums.sort()
    count = 0
    
    for i in range(len(nums) - 2):
        if nums[i] == 0:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            if nums[i] + nums[left] > nums[right]:
                count += right - left
                right -= 1
            else:
                left += 1
    
    return count
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n²)  
**Không gian**: O(1)

---

## 📚 **LEVEL 19: Advanced Two Pointers with Multiple Arrays**
**Mục tiêu**: Two pointers với nhiều mảng và điều kiện phức tạp

### Bài toán: Advanced Two Pointers
```python
def advanced_two_pointers(arr1, arr2, arr3, target):
    """
    Tìm bộ ba số từ ba mảng có tổng gần target nhất
    """
    arr1.sort()
    arr2.sort()
    arr3.sort()
    
    closest_sum = float('inf')
    
    for i in range(len(arr1)):
        left, right = 0, len(arr3) - 1
        
        while left < len(arr2) and right >= 0:
            current_sum = arr1[i] + arr2[left] + arr3[right]
            
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return target
    
    return closest_sum
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n * m * k)  
**Không gian**: O(1)

---

## 📚 **LEVEL 20: Master Level - Complex Two Pointers Applications**
**Mục tiêu**: Ứng dụng two pointers trong bài toán phức tạp nhất

### Bài toán: Master Two Pointers
```python
def master_two_pointers(nums, k, target_sum, target_product):
    """
    Two pointers với nhiều điều kiện: k phần tử, tổng >= target_sum, tích <= target_product
    """
    def is_valid_combination(subarray):
        if len(subarray) != k:
            return False
        
        total_sum = sum(subarray)
        total_product = 1
        for num in subarray:
            total_product *= num
        
        return total_sum >= target_sum and total_product <= target_product
    
    nums.sort()
    result = []
    
    # Sử dụng sliding window với two pointers
    for i in range(len(nums) - k + 1):
        left, right = i, i + k - 1
        current_subarray = nums[left:right + 1]
        
        if is_valid_combination(current_subarray):
            result.append(current_subarray[:])
    
    return result
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n * k)  
**Không gian**: O(k)

---

## 🎯 **Lộ trình học tập**

### **Giai đoạn 1 (Level 1-5)**: Nền tảng
- Hiểu khái niệm two pointers
- Thành thạo basic operations
- Làm quen với pattern cơ bản

### **Giai đoạn 2 (Level 6-10)**: Nâng cao
- String manipulation
- Array operations
- Tối ưu hóa thuật toán

### **Giai đoạn 3 (Level 11-15)**: Chuyên sâu
- Multiple sum problems
- Advanced sorting
- Tối ưu hóa bộ nhớ

### **Giai đoạn 4 (Level 16-20)**: Master
- Complex applications
- Multiple arrays
- Edge cases phức tạp

## 💡 **Mẹo cho từng level**

- **Level 1-5**: Tập trung vào hiểu pattern cơ bản
- **Level 6-10**: Chú ý đến việc xử lý string và array
- **Level 11-15**: Hiểu sâu về multiple sum problems
- **Level 16-20**: Thực hành nhiều và phân tích các trường hợp đặc biệt

## 🔥 **Common Patterns**

### **Basic Two Pointers**
```python
left, right = 0, len(nums) - 1
while left < right:
    # Process nums[left] and nums[right]
    if condition:
        left += 1
    else:
        right -= 1
```

### **Read-Write Pointers**
```python
write_index = 0
for read_index in range(len(nums)):
    if condition:
        nums[write_index] = nums[read_index]
        write_index += 1
```

### **Multiple Pointers**
```python
i, j, k = 0, 0, 0
while i < len(nums1) and j < len(nums2):
    if nums1[i] < nums2[j]:
        # Process nums1[i]
        i += 1
    else:
        # Process nums2[j]
        j += 1
``` 