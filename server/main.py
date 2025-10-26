from fastapi import FastAPI, Depends, HTTPException, status
from server.auth import api_key_auth
from server.middleware import RateLimiterMiddleware
from server.models import NewsRequest, TrendingRequest, TopicRequest, LocationRequest, RegisterResponse


app = FastAPI(
    title="GNews REST API",
    description="Comprehensive FastAPI wrapper for GNews functionality.",
    version="1.0.0"
)


app.add_middleware(RateLimiterMiddleware)


@app.get("/news", summary="Get news articles", response_model=dict)
async def get_news(q: str, limit: int = 10, api_key: str = Depends(api_key_auth)):
    if not q:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Query parameter 'q' is required.")
    # TODO: Integrate GNews logic here
    return {"results": [], "query": q, "limit": limit}


@app.get("/trending", summary="Get trending news", response_model=dict)
async def get_trending(country: str = "US", limit: int = 5, api_key: str = Depends(api_key_auth)):
    # TODO: Integrate GNews logic here
    return {"results": [], "country": country, "limit": limit}


@app.get("/topics/{topic}", summary="Get news by topic", response_model=dict)
async def get_topic_news(topic: str, limit: int = 10, api_key: str = Depends(api_key_auth)):
    # TODO: Integrate GNews logic here
    return {"results": [], "topic": topic, "limit": limit}


@app.get("/locations/{location}", summary="Get news by location", response_model=dict)
async def get_location_news(location: str, limit: int = 10, api_key: str = Depends(api_key_auth)):
    # TODO: Integrate GNews logic here
    return {"results": [], "location": location, "limit": limit}


@app.post("/auth/register", summary="Register for API key", response_model=RegisterResponse)
async def register():
    # TODO: Implement API key generation and storage
    return RegisterResponse(api_key="test-key")
