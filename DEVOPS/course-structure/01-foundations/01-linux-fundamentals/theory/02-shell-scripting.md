# Linux Fundamentals - Phần 2: Shell Scripting

## 1. Giới thiệu về Shell Scripting
- Shell là gì?
- Các loại shell phổ biến (Bash, Zsh, Fish)
- Lợi ích của shell scripting
- Cấu trúc cơ bản của một script

## 2. Biến và Kiểu dữ liệu
```bash
# Khai báo biến
name="John"
age=25

# Sử dụng biến
echo "Hello, $name"
echo "Age: ${age}"

# Biến môi trường
echo $PATH
echo $HOME

# Biến đặc biệt
echo $0    # Tên script
echo $#    # Số tham số
echo $@    # Tất cả tham số
echo $?    # Mã trả về của lệnh cuối
```

## 3. Cấu trúc điều khiển
```bash
# If-else
if [ $age -ge 18 ]; then
    echo "Adult"
else
    echo "Minor"
fi

# Case
case $1 in
    "start")
        echo "Starting..."
        ;;
    "stop")
        echo "Stopping..."
        ;;
    *)
        echo "Unknown command"
        ;;
esac

# For loop
for i in {1..5}; do
    echo "Number: $i"
done

# While loop
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done
```

## 4. Hàm
```bash
# Định nghĩa hàm
function greet() {
    local name=$1
    echo "Hello, $name!"
}

# Gọi hàm
greet "John"

# Hàm với nhiều tham số
function calculate() {
    local a=$1
    local b=$2
    echo $((a + b))
}

result=$(calculate 5 3)
echo "Result: $result"
```

## 5. Xử lý lỗi
```bash
# Kiểm tra lỗi
if ! command; then
    echo "Error: Command failed"
    exit 1
fi

# Trap
trap 'echo "Script interrupted"; exit 1' INT

# Try-catch
{
    # Code that might fail
} || {
    # Error handling
    echo "Error occurred"
    exit 1
}
```

## 6. Tương tác với người dùng
```bash
# Đọc input
read -p "Enter your name: " name
echo "Hello, $name"

# Menu
select option in "Option 1" "Option 2" "Quit"; do
    case $option in
        "Option 1")
            echo "You selected Option 1"
            ;;
        "Option 2")
            echo "You selected Option 2"
            ;;
        "Quit")
            break
            ;;
    esac
done
```

## 7. Xử lý file
```bash
# Đọc file
while IFS= read -r line; do
    echo "$line"
done < input.txt

# Ghi file
echo "Content" > output.txt
echo "More content" >> output.txt

# Kiểm tra file
if [ -f "file.txt" ]; then
    echo "File exists"
fi

if [ -d "directory" ]; then
    echo "Directory exists"
fi
```

## 8. Best Practices
- Sử dụng shebang
- Thêm comments
- Đặt tên biến có ý nghĩa
- Xử lý lỗi
- Kiểm tra điều kiện
- Sử dụng local variables
- Format code đúng chuẩn

## Bài tập thực hành
1. Tạo script quản lý người dùng
2. Tạo script backup tự động
3. Tạo script giám sát hệ thống
4. Tạo script cài đặt phần mềm

## Tài liệu tham khảo
- Bash Reference Manual
- Advanced Bash-Scripting Guide
- Shell Scripting Tutorial 