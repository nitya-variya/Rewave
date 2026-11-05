@echo off
echo ===================================================
echo   REWAVE - Everyday Functional Wellness Experience
echo ===================================================
echo Starting REWAVE local server...
powershell -NoProfile -ExecutionPolicy Bypass -Command "if (!(Get-NetTCPConnection -LocalPort 8089 -ErrorAction SilentlyContinue)) { Start-Process python -ArgumentList 'server.py' -WindowStyle Hidden }"
echo Opening REWAVE website in your default browser...
start http://127.0.0.1:8089/index.html
