# Merge Intervals (Gộp khoảng)

## Tổng quan
Merge Intervals là một kỹ thuật quan trọng để giải quyết các bài toán liên quan đến khoảng chồng lấn. Kỹ thuật này giúp hợp nhất các khoảng có thể gộp được và xử lý các bài toán về lịch trình, thời gian.

## Đặc điểm chính
- **Xử lý chồng lấn**: Hiểu rõ 6 trường hợp chồng lấn giữa hai khoảng
- **Sắp xếp**: Thường cần sắp xếp các khoảng theo thứ tự tăng dần
- **Ứng dụng rộng rãi**: Lịch trình, quản lý thời gian, phân tích dữ liệu

## 6 trường hợp chồng lấn

```
Trường hợp 1: [a, b] và [c, d] không chồng lấn (b < c)
Trường hợp 2: [a, b] và [c, d] chồng lấn một phần (a < c < b < d)
Trường hợp 3: [a, b] chứa hoàn toàn [c, d] (a < c < d < b)
Trường hợp 4: [c, d] chứa hoàn toàn [a, b] (c < a < b < d)
Trường hợp 5: [a, b] và [c, d] chồng lấn một phần (c < a < d < b)
Trường hợp 6: [a, b] và [c, d] tiếp xúc (b = c)
```

## Thuật toán cơ bản

```python
def merge_intervals(intervals):
    """
    Hợp nhất các khoảng chồng lấn
    """
    if not intervals:
        return []
    
    # Sắp xếp theo thứ tự tăng dần của start
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    current_interval = intervals[0]
    
    for next_interval in intervals[1:]:
        # Nếu có thể gộp
        if current_interval[1] >= next_interval[0]:
            current_interval[1] = max(current_interval[1], next_interval[1])
        else:
            merged.append(current_interval)
            current_interval = next_interval
    
    merged.append(current_interval)
    return merged
```

## Bài toán điển hình

### 1. Merge Intervals
```python
def merge(intervals):
    """
    Hợp nhất tất cả các khoảng chồng lấn
    """
    if not intervals:
        return []
    
    # Sắp xếp theo start time
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    current = intervals[0]
    
    for interval in intervals[1:]:
        # Nếu có thể gộp
        if current[1] >= interval[0]:
            current[1] = max(current[1], interval[1])
        else:
            merged.append(current)
            current = interval
    
    merged.append(current)
    return merged
```

### 2. Insert Interval
```python
def insert(intervals, new_interval):
    """
    Chèn khoảng mới vào danh sách các khoảng đã sắp xếp
    """
    result = []
    i = 0
    
    # Thêm tất cả khoảng kết thúc trước new_interval
    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    
    # Gộp các khoảng chồng lấn
    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    
    result.append(new_interval)
    
    # Thêm các khoảng còn lại
    while i < len(intervals):
        result.append(intervals[i])
        i += 1
    
    return result
```

### 3. Meeting Rooms
```python
def can_attend_meetings(intervals):
    """
    Kiểm tra xem có thể tham dự tất cả cuộc họp không
    """
    if not intervals:
        return True
    
    # Sắp xếp theo thời gian bắt đầu
    intervals.sort(key=lambda x: x[0])
    
    for i in range(1, len(intervals)):
        # Nếu cuộc họp trước kết thúc sau khi cuộc họp sau bắt đầu
        if intervals[i-1][1] > intervals[i][0]:
            return False
    
    return True

def min_meeting_rooms(intervals):
    """
    Tìm số phòng họp tối thiểu cần thiết
    """
    if not intervals:
        return 0
    
    # Tách thời gian bắt đầu và kết thúc
    start_times = sorted([interval[0] for interval in intervals])
    end_times = sorted([interval[1] for interval in intervals])
    
    start_pointer = 0
    end_pointer = 0
    used_rooms = 0
    
    while start_pointer < len(intervals):
        # Nếu có phòng trống (thời gian kết thúc <= thời gian bắt đầu mới)
        if start_times[start_pointer] >= end_times[end_pointer]:
            used_rooms -= 1
            end_pointer += 1
        
        # Cần thêm phòng mới
        used_rooms += 1
        start_pointer += 1
    
    return used_rooms
```

### 4. Non-overlapping Intervals
```python
def erase_overlap_intervals(intervals):
    """
    Tìm số khoảng tối thiểu cần xóa để không có khoảng nào chồng lấn
    """
    if not intervals:
        return 0
    
    # Sắp xếp theo thời gian kết thúc
    intervals.sort(key=lambda x: x[1])
    
    count = 0
    end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        # Nếu khoảng hiện tại chồng lấn với khoảng trước
        if intervals[i][0] < end:
            count += 1
        else:
            end = intervals[i][1]
    
    return count
```

### 5. Interval List Intersections
```python
def interval_intersection(first_list, second_list):
    """
    Tìm tất cả các giao điểm giữa hai danh sách khoảng
    """
    result = []
    i = j = 0
    
    while i < len(first_list) and j < len(second_list):
        # Tìm giao điểm
        start = max(first_list[i][0], second_list[j][0])
        end = min(first_list[i][1], second_list[j][1])
        
        # Nếu có giao điểm
        if start <= end:
            result.append([start, end])
        
        # Di chuyển con trỏ của khoảng kết thúc sớm hơn
        if first_list[i][1] < second_list[j][1]:
            i += 1
        else:
            j += 1
    
    return result
```

### 6. Employee Free Time
```python
def employee_free_time(schedule):
    """
    Tìm thời gian rảnh chung của tất cả nhân viên
    """
    # Gộp tất cả lịch trình
    all_intervals = []
    for employee_schedule in schedule:
        all_intervals.extend(employee_schedule)
    
    # Sắp xếp theo thời gian bắt đầu
    all_intervals.sort(key=lambda x: x[0])
    
    # Gộp các khoảng chồng lấn
    merged = []
    current = all_intervals[0]
    
    for interval in all_intervals[1:]:
        if current[1] >= interval[0]:
            current[1] = max(current[1], interval[1])
        else:
            merged.append(current)
            current = interval
    
    merged.append(current)
    
    # Tìm thời gian rảnh
    free_time = []
    for i in range(1, len(merged)):
        free_time.append([merged[i-1][1], merged[i][0]])
    
    return free_time
```

## Độ phức tạp
- **Thời gian**: O(n log n) - do cần sắp xếp các khoảng
- **Không gian**: O(n) - để lưu kết quả

## Lưu ý quan trọng
1. **Sắp xếp**: Luôn sắp xếp các khoảng trước khi xử lý
2. **Thứ tự sắp xếp**: Có thể sắp xếp theo start time hoặc end time tùy bài toán
3. **Xử lý chồng lấn**: Hiểu rõ logic xác định chồng lấn
4. **Edge cases**: Chú ý đến các trường hợp danh sách rỗng hoặc chỉ có 1 khoảng

## Bài tập thực hành
1. Meeting Rooms II
2. Car Pooling
3. Data Stream as Disjoint Intervals
4. Range Module
5. My Calendar I/II/III

## Mẹo và thủ thuật
- Sử dụng min-heap để tối ưu hóa một số bài toán
- Kết hợp với Two Pointers để xử lý hiệu quả
- Chú ý đến việc xử lý các trường hợp edge case
- Có thể áp dụng cho các bài toán về lịch trình và quản lý thời gian 