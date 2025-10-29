# GNews FastAPI REST API Usage Examples

## Authentication
All endpoints (except `/auth/register`) require an API key in the `X-API-Key` header.

## Endpoints

### 1. Get News
**GET /news?q=artificial+intelligence&limit=10**
```http
GET /news?q=artificial+intelligence&limit=10
X-API-Key: your-api-key
```
**Response:**
```json
{
  "results": [],
  "query": "artificial intelligence",
  "limit": 10
}
```

### 2. Get Trending News
**GET /trending?country=US&limit=5**
```http
GET /trending?country=US&limit=5
X-API-Key: your-api-key
```
**Response:**
```json
{
  "results": [],
  "country": "US",
  "limit": 5
}
```

### 3. Get News by Topic
**GET /topics/TECHNOLOGY?limit=10**
```http
GET /topics/TECHNOLOGY?limit=10
X-API-Key: your-api-key
```
**Response:**
```json
{
  "results": [],
  "topic": "TECHNOLOGY",
  "limit": 10
}
```

### 4. Get News by Location
**GET /locations/New+York?limit=10**
```http
GET /locations/New+York?limit=10
X-API-Key: your-api-key
```
**Response:**
```json
{
  "results": [],
  "location": "New York",
  "limit": 10
}
```

### 5. Register for API Key
**POST /auth/register**
```http
POST /auth/register
```
**Response:**
```json
{
  "api_key": "test-key"
}
```

## Error Handling
- 401 Unauthorized: Invalid API Key
- 429 Too Many Requests: Rate limit exceeded
- 400 Bad Request: Missing required parameters

## Swagger/OpenAPI Docs
Visit `/docs` for interactive API documentation.
