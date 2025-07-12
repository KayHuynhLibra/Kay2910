# Algorithm Ecosystem Platform - UI Launcher
# PowerShell script to quickly open the navigation hub

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Algorithm Ecosystem Platform" -ForegroundColor Yellow
Write-Host "   Opening Navigation Hub..." -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Get the current directory
$currentDir = Get-Location
$uiPath = Join-Path $currentDir "ui\index.html"

# Check if the file exists
if (Test-Path $uiPath) {
    Write-Host "✅ Navigation Hub found!" -ForegroundColor Green
    Write-Host "🚀 Opening in default browser..." -ForegroundColor Yellow
    
    # Open the navigation hub
    Start-Process $uiPath
    
    Write-Host ""
    Write-Host "📋 Available Keyboard Shortcuts:" -ForegroundColor Cyan
    Write-Host "   Ctrl + 1: Algorithm Analyzer" -ForegroundColor White
    Write-Host "   Ctrl + 2: Learning Accelerator" -ForegroundColor White
    Write-Host "   Ctrl + H: HTML Documentation" -ForegroundColor White
    Write-Host ""
    Write-Host "🎯 Quick Access URLs:" -ForegroundColor Cyan
    Write-Host "   Analyzer: ui\analyzers\algorithm_analyzer.html" -ForegroundColor Gray
    Write-Host "   Learning: ui\learning\learning_accelerator.html" -ForegroundColor Gray
    Write-Host "   Docs: docs\HTML_DEVELOPMENT_TECHNIQUES.md" -ForegroundColor Gray
} else {
    Write-Host "❌ Error: Navigation Hub not found!" -ForegroundColor Red
    Write-Host "Expected path: $uiPath" -ForegroundColor Red
}

Write-Host ""
Write-Host "Press any key to continue..." -ForegroundColor Yellow
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") 