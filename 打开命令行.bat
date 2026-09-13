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
echo  Run project scripts with the VENV interpreter:
echo    .venv\Scripts\python.exe src\day1.py
echo    .venv\Scripts\python.exe sql\02_practice.py
echo    .venv\Scripts\python.exe tests\week1_test.py
echo.
echo  NOTE - two traps (both verified 2026-09-13):
echo    * "python" does NOT work at all (0-byte Microsoft Store stub)
echo    * "py" works, but it uses the GLOBAL python which has only
echo      4 packages, so "py src\day1.py" fails with
echo      ModuleNotFoundError: No module named 'matplotlib'
echo ============================================
echo.
cmd /k