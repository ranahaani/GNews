from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException
import time

RATE_LIMIT = 100  # requests per hour
rate_store = {}

class RateLimiterMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        now = int(time.time())
        window = now // 3600
        key = f"{client_ip}:{window}"
        count = rate_store.get(key, 0)
        if count >= RATE_LIMIT:
            raise HTTPException(status_code=429, detail="Rate limit exceeded")
        rate_store[key] = count + 1
        response = await call_next(request)
        return response

rate_limiter = RateLimiterMiddleware
