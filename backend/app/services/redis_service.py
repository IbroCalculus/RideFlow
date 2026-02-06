import redis.asyncio as redis
from app.core.config import settings

class RedisService:
    def __init__(self):
        self.redis = redis.from_url(settings.REDIS_URL, encoding="utf-8", decode_responses=True)

    async def update_driver_location(self, driver_id: int, lat: float, lng: float):
        # GEOADD key longitude latitude member
        await self.redis.geoadd("drivers:locations", [lng, lat, str(driver_id)])

    async def get_nearby_drivers(self, lat: float, lng: float, radius_km: float = 5.0):
        # GEORADIUS key longitude latitude radius unit
        # Returns list of driver IDs
        drivers = await self.redis.georadius(
            "drivers:locations",
            longitude=lng,
            latitude=lat,
            radius=radius_km,
            unit="km",
            withdist=True
        )
        return drivers

redis_service = RedisService()
