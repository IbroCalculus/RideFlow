from fastapi import FastAPI
from app.core.database import init_db
from app.routers import auth, trips, websockets

app = FastAPI(title="RideFlow API", version="1.0.0")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(auth.router)
app.include_router(trips.router)
app.include_router(websockets.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to RideFlow API 🚖"}
