@echo off
cd /d "%~dp0"

powershell -NoProfile -ExecutionPolicy Bypass -File ".\setup-theme.ps1"
if errorlevel 1 (
    echo.
    echo Theme setup failed. Please read the error above.
    pause
    exit /b 1
)

echo.
echo Starting Hugo...
hugo server -D
pause
