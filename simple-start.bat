@echo off
REM Clean startup script for baumer-act
setlocal enabledelayedexpansion

echo.
echo ============================================
echo   მიგების აქტი - Document Generator
echo       დაშვების სკრიპტი
echo ============================================
echo.

REM Get the directory where this script is located
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"

REM Start Backend in one window
echo Starting Backend on port 5000...
start "Backend - Flask API" /d "%SCRIPT_DIR%backend" cmd /k "python app.py"

REM Wait 3 seconds for backend to start
timeout /t 3 /nobreak

REM Start Frontend in another window
echo Starting Frontend on port 3000...
start "Frontend - React App" /d "%SCRIPT_DIR%frontend" cmd /k "npm start"

echo.
echo ✓ Both servers are starting...
echo   Backend:  http://localhost:5000
echo   Frontend: http://localhost:3000
echo.
echo Press Enter to close this window...
pause

endlocal
