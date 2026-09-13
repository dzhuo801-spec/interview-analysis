@echo off
cd /d "%~dp0"
echo ========================================
echo  Running day1.py  (this window shows the result)
echo ========================================
echo.

if exist ".venv\Scripts\python.exe" (
    echo [using] .venv\Scripts\python.exe
    ".venv\Scripts\python.exe" src\day1.py
) else (
    echo [using] py launcher
    py src\day1.py
)

echo.
echo ========================================
echo  Done. Images are in the output folder.
echo ========================================
pause
