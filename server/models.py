from pydantic import BaseModel

class NewsRequest(BaseModel):
    q: str
    limit: int = 10

class TrendingRequest(BaseModel):
    country: str = "US"
    limit: int = 5

class TopicRequest(BaseModel):
    topic: str
    limit: int = 10

class LocationRequest(BaseModel):
    location: str
    limit: int = 10

class RegisterResponse(BaseModel):
    api_key: str
