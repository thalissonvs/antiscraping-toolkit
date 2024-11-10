from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from typing import Dict
from time import time

app = FastAPI()


request_counter: Dict[str, Dict] = {}


REQUEST_LIMIT = 5
BLOCK_DURATION = 60

@app.middleware("http")
async def block_repeated_requests(request: Request, call_next):
    ip = request.client.host
    user_agent = request.headers.get("user-agent", "unknown")
    
    identifier = f"{ip}:{user_agent}"
    current_time = time()

    if identifier not in request_counter:
        request_counter[identifier] = {"count": 0, "start_time": current_time, "blocked_until": 0}

    if current_time < request_counter[identifier]["blocked_until"]:
        return JSONResponse(status_code=429, content={"detail": "Too many requests. Please wait."})
    
    request_counter[identifier]["count"] += 1

    if request_counter[identifier]["count"] > REQUEST_LIMIT:
        request_counter[identifier]["blocked_until"] = current_time + BLOCK_DURATION
        request_counter[identifier]["count"] = 0 
        return JSONResponse(status_code=429, content={"detail": "Too many requests. You are temporarily blocked."})

    # Processa a requisição normalmente
    response = await call_next(request)
    
    return response

@app.get("/")
async def root():
    return {"message": "Welcome! You are not blocked."}