# AI/ML Learning Dashboard Launcher
# PowerShell Script

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "    AI/ML Learning Dashboard Launcher" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Kiểm tra xem file index.html có tồn tại không
$dashboardPath = "21_Dashboard_Web\index.html"
if (-not (Test-Path $dashboardPath)) {
    Write-Host "ERROR: Không tìm thấy file dashboard!" -ForegroundColor Red
    Write-Host "Hãy đảm bảo bạn đang ở thư mục gốc của dự án." -ForegroundColor Yellow
    Read-Host "Nhấn Enter để thoát"
    exit 1
}

Write-Host "Đang mở AI/ML Dashboard..." -ForegroundColor Green
Write-Host ""
Write-Host "Đường dẫn: $(Get-Location)\$dashboardPath" -ForegroundColor Gray
Write-Host ""

# Hiển thị menu tùy chọn
Write-Host "Chọn cách mở dashboard:" -ForegroundColor Yellow
Write-Host "1. Mở trong trình duyệt mặc định" -ForegroundColor White
Write-Host "2. Mở trong Chrome" -ForegroundColor White
Write-Host "3. Mở trong Firefox" -ForegroundColor White
Write-Host "4. Mở trong Edge" -ForegroundColor White
Write-Host "5. Chỉ hiển thị đường dẫn" -ForegroundColor White
Write-Host ""

$choice = Read-Host "Nhập lựa chọn (1-5) hoặc Enter để chọn mặc định"

switch ($choice) {
    "2" {
        # Mở trong Chrome
        if (Get-Command "chrome" -ErrorAction SilentlyContinue) {
            Start-Process "chrome" -ArgumentList $dashboardPath
        } elseif (Test-Path "C:\Program Files\Google\Chrome\Application\chrome.exe") {
            Start-Process "C:\Program Files\Google\Chrome\Application\chrome.exe" -ArgumentList $dashboardPath
        } else {
            Write-Host "Không tìm thấy Chrome. Mở trong trình duyệt mặc định..." -ForegroundColor Yellow
            Start-Process $dashboardPath
        }
    }
    "3" {
        # Mở trong Firefox
        if (Get-Command "firefox" -ErrorAction SilentlyContinue) {
            Start-Process "firefox" -ArgumentList $dashboardPath
        } elseif (Test-Path "C:\Program Files\Mozilla Firefox\firefox.exe") {
            Start-Process "C:\Program Files\Mozilla Firefox\firefox.exe" -ArgumentList $dashboardPath
        } else {
            Write-Host "Không tìm thấy Firefox. Mở trong trình duyệt mặc định..." -ForegroundColor Yellow
            Start-Process $dashboardPath
        }
    }
    "4" {
        # Mở trong Edge
        if (Get-Command "msedge" -ErrorAction SilentlyContinue) {
            Start-Process "msedge" -ArgumentList $dashboardPath
        } elseif (Test-Path "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe") {
            Start-Process "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" -ArgumentList $dashboardPath
        } else {
            Write-Host "Không tìm thấy Edge. Mở trong trình duyệt mặc định..." -ForegroundColor Yellow
            Start-Process $dashboardPath
        }
    }
    "5" {
        # Chỉ hiển thị đường dẫn
        Write-Host "Đường dẫn dashboard:" -ForegroundColor Green
        Write-Host "file://$(Get-Location)\$dashboardPath" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Copy đường dẫn trên và paste vào trình duyệt." -ForegroundColor Yellow
    }
    default {
        # Mở trong trình duyệt mặc định
        Start-Process $dashboardPath
    }
}

Write-Host ""
Write-Host "Dashboard đã được mở!" -ForegroundColor Green
Write-Host ""
Write-Host "Các tính năng có sẵn:" -ForegroundColor Yellow
Write-Host "- Xem nội dung thực tế từ các file AI/ML" -ForegroundColor White
Write-Host "- Duyệt 20 chủ đề chính" -ForegroundColor White
Write-Host "- Xem lý thuyết, code, quiz, project" -ForegroundColor White
Write-Host "- Dark theme toggle" -ForegroundColor White
Write-Host ""
Write-Host "Nhấn Enter để thoát..." -ForegroundColor Gray
Read-Host 