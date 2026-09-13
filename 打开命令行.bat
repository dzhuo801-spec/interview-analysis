@echo off
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
