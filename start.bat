@echo off
echo ===========================================
echo   მიგების აქტი - Document Generator
echo       დაშვების სკრიპტი
echo ===========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python არ არის დაინსტალირებული!
    echo გთხოვთ დაინსტალირეთ Python https://www.python.org
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js არ არის დაინსტალირებული!
    echo გთხოვთ დაინსტალირეთ Node.js https://nodejs.org
    pause
    exit /b 1
)

echo ✓ Python დაინსტალირებული
echo ✓ Node.js დაინსტალირებული
echo.

REM Install backend dependencies if needed
if not exist "backend\__pycache__" (
    echo დოქელი: Backend დამოკიდებულებების დაინსტალაცია...
    cd backend
    pip install -r ../requirements.txt
    cd ..
    echo ✓ Backend დამოკიდებულებები დაინსტალირდა
    echo.
)

REM Install frontend dependencies if needed
if not exist "frontend\node_modules" (
    echo დოქელი: Frontend დამოკიდებულებების დაინსტალაცია...
    cd frontend
    call npm install
    cd ..
    echo ✓ Frontend დამოკიდებულებები დაინსტალირდა
    echo.
)

echo.
echo ===========================================
echo   დაშვება დაიწყო...
echo ===========================================
echo.
echo 🔵 Backend დაიშვება: http://localhost:5000
echo 🔵 Frontend დაიშვება: http://localhost:3000
echo.
echo დაუჭიროთ ნებისმიერ ღილაკს დასახურად...
echo.

start "Backend - Flask API" cmd /k "cd backend && python app.py"
timeout /t 3 /nobreak
start "Frontend - React App" cmd /k "cd frontend && npm start"

echo.
echo ✓ ორივე სერვერი თქვენი ბრაუზერში აიხსნება...
