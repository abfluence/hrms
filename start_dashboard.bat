@echo off
title AB Fluence HRMS

:: Start Ollama with CORS open (allows localhost origins)
echo Starting Ollama...
set OLLAMA_ORIGINS=*
start "" ollama serve

:: Wait for Ollama to be ready
timeout /t 3 /nobreak > nul

:: Start local HTTP server for the dashboard on port 8585
echo Starting dashboard server on http://localhost:8585
start "" http://localhost:8585/hr%%20dashboard.html
python -m http.server 8585
