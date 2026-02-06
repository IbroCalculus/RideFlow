from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.websocket_manager import manager

router = APIRouter(prefix="/ws", tags=["websockets"])

@router.websocket("/connect/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await manager.connect(websocket, user_id)
    try:
        while True:
            data = await websocket.receive_json()
            # Handle incoming location updates or messages here
            # e.g., if data['type'] == 'LOCATION_UPDATE': save_to_redis(...)
            await manager.send_personal_message({"message": "Ack"}, user_id)
    except WebSocketDisconnect:
        manager.disconnect(user_id)
