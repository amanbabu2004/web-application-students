Write-Host "Starting User Management System..." -ForegroundColor Green
Write-Host ""

Write-Host "Starting Backend (FastAPI)..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd backend; pip install -r requirements.txt; uvicorn main:app --reload"

Write-Host ""
Write-Host "Waiting 5 seconds for backend to start..." -ForegroundColor Cyan
Start-Sleep -Seconds 5

Write-Host "Starting Frontend (React)..." -ForegroundColor Yellow  
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd frontend; npm install; npm start"

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Backend: http://localhost:8000" -ForegroundColor White
Write-Host "Frontend: http://localhost:3000" -ForegroundColor White
Write-Host "API Docs: http://localhost:8000/docs" -ForegroundColor White
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Press any key to exit..." -ForegroundColor Cyan
$Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") | Out-Null
