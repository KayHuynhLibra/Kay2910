#!/usr/bin/env python3
"""
Script để thêm nút "Back" vào tất cả các file HTML trong dự án Algorithm Ecosystem
"""

import os
import re
from pathlib import Path

def add_back_button_to_html(file_path):
    """Thêm nút back vào file HTML"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Kiểm tra xem đã có nút back chưa
        if 'back-button' in content:
            print(f"  ✓ {file_path.name} - Đã có nút back")
            return False
        
        # Tìm header section
        header_pattern = r'(<div class="header"[^>]*>)'
        header_match = re.search(header_pattern, content)
        
        if not header_match:
            print(f"  ⚠ {file_path.name} - Không tìm thấy header")
            return False
        
        header_start = header_match.start()
        
        # Xác định đường dẫn back dựa trên vị trí file
        relative_path = file_path.relative_to(Path.cwd())
        path_parts = relative_path.parts
        
        if len(path_parts) >= 3 and path_parts[0] == 'AlgorithmEcosystem' and path_parts[1] == 'ui':
            # File trong thư mục ui/subfolder
            if path_parts[2] in ['analyzers', 'learning', 'dashboards', 'viewers', 'components', 'shared']:
                back_path = '../index.html'
                back_text = '← Quay lại Navigation Hub'
            else:
                back_path = '../../index.html'
                back_text = '← Quay lại thư mục gốc'
        elif len(path_parts) >= 2 and path_parts[0] == 'AlgorithmEcosystem':
            # File trong thư mục AlgorithmEcosystem
            back_path = '../index.html'
            back_text = '← Quay lại thư mục gốc'
        else:
            # File ở thư mục gốc
            back_path = 'index.html'
            back_text = '← Quay lại Navigation Hub'
        
        # CSS cho nút back
        back_button_css = '''
        .back-button {
            position: absolute;
            left: 0;
            top: 50%;
            transform: translateY(-50%);
            background: rgba(255, 255, 255, 0.2);
            border: 2px solid rgba(255, 255, 255, 0.3);
            color: white;
            padding: 10px 20px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 1rem;
            font-weight: 500;
            transition: all 0.3s ease;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .back-button:hover {
            background: rgba(255, 255, 255, 0.3);
            border-color: rgba(255, 255, 255, 0.5);
            transform: translateY(-50%) scale(1.05);
        }
        '''
        
        # Thêm CSS vào style section
        style_pattern = r'(<style>)'
        style_match = re.search(style_pattern, content)
        
        if style_match:
            # Thêm CSS vào đầu style section
            style_start = style_match.end()
            content = content[:style_start] + back_button_css + content[style_start:]
        else:
            # Tạo style section mới
            head_pattern = r'(</head>)'
            head_match = re.search(head_pattern, content)
            if head_match:
                head_end = head_match.start()
                style_section = f'    <style>{back_button_css}</style>\n'
                content = content[:head_end] + style_section + content[head_end:]
        
        # Thêm position relative cho header
        header_css_pattern = r'(\.header\s*\{[^}]*\})'
        header_css_match = re.search(header_css_pattern, content)
        
        if header_css_match:
            header_css = header_css_match.group(1)
            if 'position: relative' not in header_css:
                # Thêm position relative vào header CSS
                header_css_new = header_css.replace('{', '{\n            position: relative;')
                content = content.replace(header_css, header_css_new)
        
        # Thêm nút back vào header
        back_button_html = f'            <a href="{back_path}" class="back-button">\n                {back_text}\n            </a>\n'
        
        # Tìm vị trí để chèn nút back (sau thẻ mở header)
        header_end = content.find('>', header_start) + 1
        content = content[:header_end] + '\n' + back_button_html + content[header_end:]
        
        # Thêm responsive CSS cho mobile
        mobile_css = '''
        @media (max-width: 768px) {
            .back-button {
                position: relative;
                left: auto;
                top: auto;
                transform: none;
                margin-bottom: 20px;
                display: inline-block;
            }
        }
        '''
        
        # Thêm mobile CSS vào cuối style section
        style_end_pattern = r'(</style>)'
        style_end_match = re.search(style_end_pattern, content)
        
        if style_end_match:
            style_end = style_end_match.start()
            content = content[:style_end] + mobile_css + content[style_end:]
        
        # Ghi file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✓ {file_path.name} - Đã thêm nút back")
        return True
        
    except Exception as e:
        print(f"  ✗ {file_path.name} - Lỗi: {e}")
        return False

def find_html_files(directory):
    """Tìm tất cả file HTML trong thư mục"""
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                html_files.append(Path(root) / file)
    return html_files

def main():
    """Hàm chính"""
    print("🚀 Bắt đầu thêm nút Back vào tất cả file HTML...")
    print("=" * 60)
    
    # Tìm tất cả file HTML
    current_dir = Path.cwd()
    html_files = find_html_files(current_dir)
    
    if not html_files:
        print("❌ Không tìm thấy file HTML nào!")
        return
    
    print(f"📁 Tìm thấy {len(html_files)} file HTML:")
    
    success_count = 0
    skip_count = 0
    error_count = 0
    
    for html_file in html_files:
        print(f"\n📄 Xử lý: {html_file}")
        
        try:
            if add_back_button_to_html(html_file):
                success_count += 1
            else:
                skip_count += 1
        except Exception as e:
            print(f"  ✗ Lỗi: {e}")
            error_count += 1
    
    print("\n" + "=" * 60)
    print("📊 Kết quả:")
    print(f"  ✓ Thành công: {success_count} file")
    print(f"  ⚠ Bỏ qua: {skip_count} file")
    print(f"  ✗ Lỗi: {error_count} file")
    print(f"  📁 Tổng cộng: {len(html_files)} file")
    
    if success_count > 0:
        print("\n🎉 Hoàn thành! Tất cả file HTML đã có nút Back.")
        print("💡 Bây giờ bạn có thể điều hướng dễ dàng giữa các trang.")

if __name__ == "__main__":
    main() 