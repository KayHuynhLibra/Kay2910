# Module Thống Kê và Xác Suất

Module này cung cấp các chức năng thống kê và xác suất cho hệ thống AI, bao gồm phân tích mô tả, kiểm định giả thuyết, phân tích tương quan và hồi quy.

## Tính Năng

1. **Thống Kê Mô Tả**
   - Trung bình, trung vị, mode
   - Độ lệch chuẩn và phương sai
   - Phân vị (quartiles)
   - Giá trị min/max

2. **Phân Phối Xác Suất**
   - Phân phối chuẩn (Normal)
   - Phân phối mũ (Exponential)
   - PDF và CDF
   - Tham số phân phối

3. **Kiểm Định Giả Thuyết**
   - T-test
   - Chi-square test
   - P-value và mức ý nghĩa
   - Kết luận thống kê

4. **Phân Tích Tương Quan**
   - Ma trận tương quan
   - Hệ số tương quan Pearson
   - Hệ số tương quan Spearman
   - Biểu đồ tương quan

5. **Phân Tích Hồi Quy**
   - Hồi quy tuyến tính đơn
   - Hồi quy tuyến tính bội
   - Hệ số hồi quy
   - R-squared và p-value

## Sử Dụng

1. **Thống Kê Mô Tả**
```python
result = await statistical_agent.process({
    "type": "descriptive",
    "data": [1, 2, 3, 4, 5]
})
```

2. **Phân Phối Xác Suất**
```python
result = await statistical_agent.process({
    "type": "probability",
    "data": [1, 2, 3, 4, 5],
    "params": {
        "distribution": "normal"
    }
})
```

3. **Kiểm Định Giả Thuyết**
```python
result = await statistical_agent.process({
    "type": "hypothesis",
    "data": [1, 2, 3, 4, 5],
    "params": {
        "test_type": "t-test",
        "alpha": 0.05
    }
})
```

4. **Phân Tích Tương Quan**
```python
result = await statistical_agent.process({
    "type": "correlation",
    "data": {
        "x": [1, 2, 3, 4, 5],
        "y": [2, 4, 6, 8, 10]
    }
})
```

5. **Phân Tích Hồi Quy**
```python
result = await statistical_agent.process({
    "type": "regression",
    "data": {
        "x1": [1, 2, 3, 4, 5],
        "x2": [2, 4, 6, 8, 10],
        "y": [3, 6, 9, 12, 15]
    },
    "params": {
        "x_columns": ["x1", "x2"],
        "y_column": "y"
    }
})
```

## Cài Đặt

1. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

2. Import module:
```python
from stats.statistical_agent import StatisticalAgent
```

## Lưu ý

1. Dữ liệu đầu vào phải là số thực
2. Xử lý ngoại lệ cho dữ liệu không hợp lệ
3. Cache kết quả để tối ưu hiệu suất
4. Logging cho debug và monitoring

## Mở Rộng

1. Thêm các phân phối xác suất mới
2. Bổ sung các phương pháp kiểm định
3. Tích hợp visualization
4. Thêm các phương pháp hồi quy nâng cao 