from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="AccessMatic API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # We'll restrict this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "AccessMatic API"}

@app.get("/")
async def root():
    return {"message": "AccessMatic API is running!", "version": "1.0.0"}

@app.get("/api/v1/test")
async def api_test():
    return {
        "message": "API endpoint working!", 
        "openai_configured": bool(os.getenv("OPENAI_API_KEY")),
        "environment": os.getenv("ENVIRONMENT", "development")
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
