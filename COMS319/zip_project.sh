#!/bin/bash

# Tên thư mục bạn muốn zip
PROJECT_NAME="activity10"

# 1. Xóa node_modules nếu tồn tại
if [ -d "$PROJECT_NAME/node_modules" ]; then
  echo "🧹 Deleting node_modules..."
  rm -rf "$PROJECT_NAME/node_modules"
fi

# 2. Tạo file zip
echo "📦 Zipping project (without node_modules)..."
zip -r "${PROJECT_NAME}.zip" "$PROJECT_NAME" -x "$PROJECT_NAME/node_modules/*"

# 3. Hoàn tất
echo "✅ Done! Created ${PROJECT_NAME}.zip"
