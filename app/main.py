import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .controllers import user_controller, call_controller
from .config import settings

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Call Blocker API",
    description="API for blocking non-Indian phone calls",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(user_controller.router, prefix=settings.API_PREFIX)
app.include_router(call_controller.router, prefix=settings.API_PREFIX)

@app.get("/")
def root():
    return {"message": "Welcome to Call Blocker API. Use /docs for API documentation."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        reload=False
    )