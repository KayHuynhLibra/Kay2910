#!/bin/bash

echo ""
echo "========================================"
echo "    AI/ML Learning Dashboard Launcher"
echo "========================================"
echo ""

# Kiểm tra xem file index.html có tồn tại không
if [ ! -f "21_Dashboard_Web/index.html" ]; then
    echo "ERROR: Không tìm thấy file dashboard!"
    echo "Hãy đảm bảo bạn đang ở thư mục gốc của dự án."
    exit 1
fi

echo "Đang mở AI/ML Dashboard..."
echo ""
echo "Đường dẫn: $(pwd)/21_Dashboard_Web/index.html"
echo ""

# Mở dashboard trong trình duyệt mặc định
if command -v xdg-open &> /dev/null; then
    # Linux
    xdg-open "21_Dashboard_Web/index.html"
elif command -v open &> /dev/null; then
    # macOS
    open "21_Dashboard_Web/index.html"
else
    echo "Không thể mở trình duyệt tự động."
    echo "Vui lòng mở file: 21_Dashboard_Web/index.html"
fi

echo "Dashboard đã được mở trong trình duyệt!"
echo ""
echo "Các tính năng có sẵn:"
echo "- Xem nội dung thực tế từ các file AI/ML"
echo "- Duyệt 20 chủ đề chính"
echo "- Xem lý thuyết, code, quiz, project"
echo "- Dark theme toggle"
echo "" 