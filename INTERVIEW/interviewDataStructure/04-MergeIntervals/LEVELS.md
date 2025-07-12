# MERGE INTERVALS - 10 LEVELS TỪ CƠ BẢN ĐẾN NÂNG CAO

## 🎯 Tổng quan
10 level này được thiết kế để bạn học Merge Intervals từ cơ bản đến nâng cao, mỗi level tăng dần độ khó và phức tạp.

---

## 📚 **LEVEL 1: Hiểu cơ bản về Merge Intervals**
**Mục tiêu**: Hiểu khái niệm và cách hoạt động của merge intervals

### Bài toán: Merge Intervals
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

**Độ khó**: ⭐  
**Thời gian**: O(n log n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 2: Insert Interval**
**Mục tiêu**: Chèn khoảng mới vào danh sách đã sắp xếp

### Bài toán: Insert Interval
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

**Độ khó**: ⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 3: Meeting Rooms**
**Mục tiêu**: Kiểm tra xem có thể tham dự tất cả cuộc họp không

### Bài toán: Meeting Rooms
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
```

**Độ khó**: ⭐⭐⭐  
**Thời gian**: O(n log n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 4: Minimum Meeting Rooms**
**Mục tiêu**: Tìm số phòng họp tối thiểu cần thiết

### Bài toán: Meeting Rooms II
```python
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

**Độ khó**: ⭐⭐⭐⭐  
**Thời gian**: O(n log n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 5: Non-overlapping Intervals**
**Mục tiêu**: Tìm số khoảng tối thiểu cần xóa để không chồng lấn

### Bài toán: Non-overlapping Intervals
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

**Độ khó**: ⭐⭐⭐⭐  
**Thời gian**: O(n log n)  
**Không gian**: O(1)

---

## 📚 **LEVEL 6: Interval List Intersections**
**Mục tiêu**: Tìm giao điểm giữa hai danh sách khoảng

### Bài toán: Interval List Intersections
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

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(n + m)  
**Không gian**: O(min(n, m))

---

## 📚 **LEVEL 7: Employee Free Time**
**Mục tiêu**: Tìm thời gian rảnh chung của tất cả nhân viên

### Bài toán: Employee Free Time
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

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(n log n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 8: Car Pooling**
**Mục tiêu**: Kiểm tra xem có thể chở tất cả hành khách không

### Bài toán: Car Pooling
```python
def car_pooling(trips, capacity):
    """
    Kiểm tra xem có thể chở tất cả hành khách không
    """
    # Tạo timeline events
    events = []
    for passengers, start, end in trips:
        events.append((start, passengers))
        events.append((end, -passengers))
    
    # Sắp xếp theo thời gian
    events.sort()
    
    current_passengers = 0
    for time, passengers in events:
        current_passengers += passengers
        if current_passengers > capacity:
            return False
    
    return True
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n log n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 9: Data Stream as Disjoint Intervals**
**Mục tiêu**: Xử lý stream dữ liệu và duy trì các khoảng rời rạc

### Bài toán: Data Stream as Disjoint Intervals
```python
class SummaryRanges:
    def __init__(self):
        self.intervals = []
    
    def addNum(self, value):
        """
        Thêm số mới vào stream
        """
        new_interval = [value, value]
        merged = []
        
        for interval in self.intervals:
            # Nếu khoảng mới nằm trước khoảng hiện tại
            if new_interval[1] + 1 < interval[0]:
                merged.append(new_interval)
                new_interval = interval
            # Nếu khoảng mới nằm sau khoảng hiện tại
            elif interval[1] + 1 < new_interval[0]:
                merged.append(interval)
            # Nếu có thể gộp
            else:
                new_interval[0] = min(new_interval[0], interval[0])
                new_interval[1] = max(new_interval[1], interval[1])
        
        merged.append(new_interval)
        self.intervals = merged
    
    def getIntervals(self):
        """
        Trả về tất cả các khoảng
        """
        return self.intervals
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n) cho mỗi thao tác addNum  
**Không gian**: O(n)

---

## 📚 **LEVEL 10: Range Module**
**Mục tiêu**: Xây dựng module quản lý khoảng với các thao tác phức tạp

### Bài toán: Range Module
```python
class RangeModule:
    def __init__(self):
        self.intervals = []
    
    def addRange(self, left, right):
        """
        Thêm khoảng [left, right)
        """
        new_intervals = []
        i = 0
        
        # Thêm các khoảng nằm trước
        while i < len(self.intervals) and self.intervals[i][1] < left:
            new_intervals.append(self.intervals[i])
            i += 1
        
        # Gộp các khoảng chồng lấn
        if i < len(self.intervals) and self.intervals[i][0] <= right:
            left = min(left, self.intervals[i][0])
            right = max(right, self.intervals[i][1])
            i += 1
        
        new_intervals.append([left, right])
        
        # Thêm các khoảng còn lại
        while i < len(self.intervals):
            new_intervals.append(self.intervals[i])
            i += 1
        
        self.intervals = new_intervals
    
    def queryRange(self, left, right):
        """
        Kiểm tra xem khoảng [left, right) có được bao phủ hoàn toàn không
        """
        for interval in self.intervals:
            if interval[0] <= left and interval[1] >= right:
                return True
            if interval[0] > left:
                break
        return False
    
    def removeRange(self, left, right):
        """
        Xóa khoảng [left, right)
        """
        new_intervals = []
        
        for interval in self.intervals:
            # Nếu khoảng nằm hoàn toàn bên ngoài
            if interval[1] <= left or interval[0] >= right:
                new_intervals.append(interval)
            else:
                # Nếu có phần giao
                if interval[0] < left:
                    new_intervals.append([interval[0], left])
                if interval[1] > right:
                    new_intervals.append([right, interval[1]])
        
        self.intervals = new_intervals
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n) cho mỗi thao tác  
**Không gian**: O(n)

---

## 🎯 **Lộ trình học tập**

### **Giai đoạn 1 (Level 1-3)**: Nền tảng
- Hiểu khái niệm merge intervals
- Thành thạo việc gộp khoảng chồng lấn
- Làm quen với pattern cơ bản

### **Giai đoạn 2 (Level 4-6)**: Nâng cao
- Xử lý bài toán phòng họp
- Tìm giao điểm giữa các khoảng
- Tối ưu hóa thuật toán

### **Giai đoạn 3 (Level 7-8)**: Chuyên sâu
- Xử lý stream dữ liệu
- Quản lý thời gian phức tạp
- Tối ưu hóa bộ nhớ

### **Giai đoạn 4 (Level 9-10)**: Master
- Xây dựng module hoàn chỉnh
- Xử lý các thao tác phức tạp
- Edge cases phức tạp

## 💡 **Mẹo cho từng level**

- **Level 1-3**: Tập trung vào hiểu pattern cơ bản
- **Level 4-6**: Chú ý đến việc tối ưu hóa và xử lý edge cases
- **Level 7-8**: Hiểu sâu về xử lý dữ liệu thời gian thực
- **Level 9-10**: Thực hành nhiều và phân tích các trường hợp đặc biệt

## 🔥 **Common Patterns**

### **Basic Merge**
```python
intervals.sort(key=lambda x: x[0])
merged = []
current = intervals[0]

for interval in intervals[1:]:
    if current[1] >= interval[0]:
        current[1] = max(current[1], interval[1])
    else:
        merged.append(current)
        current = interval
merged.append(current)
```

### **Insert Interval**
```python
result = []
i = 0
while i < len(intervals) and intervals[i][1] < new_interval[0]:
    result.append(intervals[i])
    i += 1

while i < len(intervals) and intervals[i][0] <= new_interval[1]:
    new_interval[0] = min(new_interval[0], intervals[i][0])
    new_interval[1] = max(new_interval[1], intervals[i][1])
    i += 1

result.append(new_interval)
result.extend(intervals[i:])
```

### **Meeting Rooms II**
```python
start_times = sorted([interval[0] for interval in intervals])
end_times = sorted([interval[1] for interval in intervals])

start_pointer = end_pointer = used_rooms = 0
while start_pointer < len(intervals):
    if start_times[start_pointer] >= end_times[end_pointer]:
        used_rooms -= 1
        end_pointer += 1
    used_rooms += 1
    start_pointer += 1
``` 