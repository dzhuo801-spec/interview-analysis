@echo off
rem Encoding fix (2026-09-13): see 运行day1.bat for why.
chcp 65001 >nul
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8

cd /d "%~dp0"
echo ============================================
echo  Command prompt opened at:
echo  %CD%
echo.
echo  Try running:
echo    py src\day1.py
echo.
echo  Or with the project venv:
echo    .venv\Scripts\python.exe src\day1.py
echo ============================================
echo.
cmd /k