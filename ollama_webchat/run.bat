@echo off
echo Starting Ollama Web Chat...
python -m uvicorn app:app --host 127.0.0.1 --port 8000
pause