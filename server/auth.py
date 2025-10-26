from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader

API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# Dummy store for API keys
API_KEYS = {"test-key": True}

def api_key_auth(api_key: str = Depends(api_key_header)):
    if api_key in API_KEYS:
        return api_key
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key")
