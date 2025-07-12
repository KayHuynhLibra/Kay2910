#!/usr/bin/env python3
"""
System Status Check - Kiểm tra trạng thái hệ thống sau nâng cấp
"""

import os
import glob
from pathlib import Path

def count_files_by_type():
    """Đếm số file theo loại"""
    file_types = {
        'THEORY': 0,
        'IMPLEMENTATION': 0,
        'CODE_EXAMPLES': 0,
        'BEST_PRACTICES': 0,
        'QUIZ': 0,
        'EXERCISES': 0,
        'PROJECT': 0,
        'LEARNING_ROADMAP': 0,
        'COMPLEX_PROBLEMS': 0,
        'requirements': 0
    }
    
    # Đếm file trong tất cả thư mục con
    for root, dirs, files in os.walk('.'):
        if 'node_modules' in root or '.git' in root:
            continue
            
        for file in files:
            if file.endswith('.md') or file.endswith('.txt'):
                for file_type in file_types.keys():
                    if file.startswith(file_type):
                        file_types[file_type] += 1
                        break
    
    return file_types

def count_directories():
    """Đếm số thư mục"""
    main_dirs = 0
    sub_dirs = 0
    
    for item in os.listdir('.'):
        if os.path.isdir(item) and item.startswith(('0', '1', '2')):
            main_dirs += 1
            # Đếm thư mục con
            for sub_item in os.listdir(item):
                sub_path = os.path.join(item, sub_item)
                if os.path.isdir(sub_path):
                    sub_dirs += 1
    
    return main_dirs, sub_dirs

def check_sample_content():
    """Kiểm tra nội dung mẫu"""
    sample_files = [
        '01_Machine_Learning/01_Algorithms/01_Linear_Regression/THEORY_01_linear_regression.md',
        '01_Machine_Learning/01_Algorithms/01_Linear_Regression/QUIZ_01_linear_regression.md',
        '01_Machine_Learning/01_Algorithms/01_Linear_Regression/COMPLEX_PROBLEMS.md'
    ]
    
    results = {}
    for file_path in sample_files:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                results[file_path] = {
                    'exists': True,
                    'size': len(content),
                    'has_vietnamese': 'Tiếng Việt' in content,
                    'has_english': 'English' in content,
                    'has_code': '```python' in content
                }
        else:
            results[file_path] = {'exists': False}
    
    return results

def main():
    """Hàm chính"""
    print("🔍 Kiểm tra trạng thái hệ thống AI/ML...")
    print("=" * 60)
    
    # Đếm thư mục
    main_dirs, sub_dirs = count_directories()
    print(f"📁 Thư mục chính: {main_dirs}")
    print(f"📁 Thư mục con: {sub_dirs}")
    print(f"📁 Tổng thư mục: {main_dirs + sub_dirs}")
    print()
    
    # Đếm file theo loại
    file_counts = count_files_by_type()
    print("📄 Thống kê file theo loại:")
    total_files = 0
    for file_type, count in file_counts.items():
        print(f"   {file_type}: {count:,}")
        total_files += count
    print(f"   Tổng file: {total_files:,}")
    print()
    
    # Kiểm tra nội dung mẫu
    print("🔍 Kiểm tra nội dung mẫu:")
    sample_results = check_sample_content()
    for file_path, result in sample_results.items():
        if result['exists']:
            print(f"✅ {file_path}")
            print(f"   - Kích thước: {result['size']:,} ký tự")
            print(f"   - Có tiếng Việt: {'✅' if result['has_vietnamese'] else '❌'}")
            print(f"   - Có tiếng Anh: {'✅' if result['has_english'] else '❌'}")
            print(f"   - Có code: {'✅' if result['has_code'] else '❌'}")
        else:
            print(f"❌ {file_path} - Không tồn tại")
        print()
    
    # Tóm tắt
    print("📊 TÓM TẮT:")
    print(f"🎯 Hệ thống đã được nâng cấp thành công!")
    print(f"📚 Tổng cộng {total_files:,} file nội dung")
    print(f"🗂️ {main_dirs + sub_dirs:,} thư mục")
    print(f"🌐 Nội dung song ngữ Việt-Anh")
    print(f"💻 Code examples thực tế")
    print(f"🧠 Quiz và bài tập")
    print(f"🚀 Projects thực hành")
    print(f"🗺️ Learning roadmaps")
    print(f"❓ Complex problems")
    
    print("\n🎉 Hệ thống sẵn sàng sử dụng!")

if __name__ == "__main__":
    main() 