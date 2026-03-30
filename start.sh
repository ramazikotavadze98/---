#!/bin/bash

echo "=========================================="
echo "  მიგების აქტი - Document Generator"
echo "       დაშვების სკრიპტი"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python არ არის დაინსტალირებული!"
    echo "გთხოვთ დაინსტალირეთ Python"
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js არ არის დაინსტალირებული!"
    echo "გთხოვთ დაინსტალირეთ Node.js https://nodejs.org"
    exit 1
fi

echo "✓ Python დაინსტალირებული"
echo "✓ Node.js დაინსტალირებული"
echo ""

# Install backend dependencies if needed
if [ ! -d "backend/__pycache__" ]; then
    echo "დოქელი: Backend დამოკიდებულებების დაინსტალაცია..."
    cd backend
    pip3 install -r ../requirements.txt
    cd ..
    echo "✓ Backend დამოკიდებულებები დაინსტალირდა"
    echo ""
fi

# Install frontend dependencies if needed
if [ ! -d "frontend/node_modules" ]; then
    echo "დოქელი: Frontend დამოკიდებულებების დაინსტალაცია..."
    cd frontend
    npm install
    cd ..
    echo "✓ Frontend დამოკიდებულებები დაინსტალირდა"
    echo ""
fi

echo ""
echo "=========================================="
echo "   დაშვება დაიწყო..."
echo "=========================================="
echo ""
echo "🔵 Backend დაიშვება: http://localhost:5000"
echo "🔵 Frontend დაიშვება: http://localhost:3000"
echo ""

# Start backend in background
cd backend
python3 app.py &
BACKEND_PID=$!
cd ..

# Wait a bit for backend to start
sleep 3

# Start frontend
cd frontend
npm start

# Clean up
kill $BACKEND_PID 2>/dev/null
