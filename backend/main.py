from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from websocket.game_socket import router as game_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include WebSocket router
app.include_router(game_router, prefix="/game", tags=["game"])


@app.get("/")
async def root():
    return {"message": "Welcome to Number Guessing Game!", "version": settings.app_version}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=settings.host, port=settings.port, reload=settings.debug)
