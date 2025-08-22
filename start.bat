@echo off
echo Starting User Management System...
echo.

echo Starting Backend (FastAPI)...
start "Backend Server" cmd /k "cd backend && pip install -r requirements.txt && uvicorn main:app --reload"

echo.
echo Waiting 5 seconds for backend to start...
timeout /t 5 /nobreak >nul

echo Starting Frontend (React)...
start "Frontend Server" cmd /k "cd frontend && npm install && npm start"

echo.
echo ========================================
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
echo API Docs: http://localhost:8000/docs
echo ========================================
echo.
echo Press any key to exit...
pause >nul
