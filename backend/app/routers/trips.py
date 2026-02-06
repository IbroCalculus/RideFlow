from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/trips", tags=["trips"])

class RideRequest(BaseModel):
    pickup_lat: float
    pickup_lng: float
    dest_lat: float
    dest_lng: float
    rider_id: int

@router.post("/request")
def request_ride(ride: RideRequest):
    # Logic to find drivers via Redis will go here
    return {"message": "Looking for drivers...", "ride_id": "123", "status": "SEARCHING"}
