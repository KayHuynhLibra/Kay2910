@echo off
echo.
echo ========================================
echo    AI/ML Learning Dashboard Launcher
echo ========================================
echo.

REM Kiểm tra xem file index.html có tồn tại không
if not exist "21_Dashboard_Web\index.html" (
    echo ERROR: Khong tim thay file dashboard!
    echo Hay dam bao ban dang o thu muc goc cua du an.
    pause
    exit /b 1
)

echo Dang mo AI/ML Dashboard...
echo.
echo Duong dan: %cd%\21_Dashboard_Web\index.html
echo.

REM Mở dashboard trong trình duyệt mặc định
start "" "21_Dashboard_Web\index.html"

echo Dashboard da duoc mo trong trinh duyet!
echo.
echo Cac tinh nang co san:
echo - Xem noi dung thuc te tu cac file AI/ML
echo - Duyet 20 chu de chinh
echo - Xem ly thuyet, code, quiz, project
echo - Dark theme toggle
echo.
echo Nhan phim bat ky de dong...
pause >nul 