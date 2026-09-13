@echo off
rem ============================================================
rem  Encoding fix (2026-09-13):
rem  The console default codepage here is cp936 (GBK). Characters
rem  like U+26A0 (warning sign), U+2705, U+1F4CC CANNOT be encoded
rem  in cp936, so any `print("...")` containing them raises
rem  UnicodeEncodeError and kills the script.
rem  chcp 65001 + PYTHONUTF8=1 makes both the console and Python
rem  speak UTF-8, so Chinese AND emoji survive.
rem ============================================================
chcp 65001 >nul
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8

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

set "RC=%ERRORLEVEL%"
echo.
echo ========================================
echo  Done. Exit code: %RC%
echo  Images are in the output folder.
echo ========================================
pause