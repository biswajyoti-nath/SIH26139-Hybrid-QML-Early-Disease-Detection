#!/bin/bash
echo "Starting Hybrid QML Platform Demo Mode..."

# Start backend
uv run uvicorn backend.api.main:app --reload --port 8000 &
BACKEND_PID=$!

# Start frontend
cd frontend
npm run dev -- --port 3000 &
FRONTEND_PID=$!

echo "=================================================="
echo "DEMO READY"
echo "Backend: http://localhost:8000"
echo "Frontend: http://localhost:3000"
echo "=================================================="
echo "Press Ctrl+C to stop"

trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT TERM
wait
