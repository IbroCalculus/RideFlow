from app.services.redis_service import redis_service

class MatchingEngine:
    async def find_driver(self, pickup_lat: float, pickup_lng: float) -> int:
        """
        Finds the nearest driver within 5km radius using Redis Geo.
        """
        drivers = await redis_service.get_nearby_drivers(pickup_lat, pickup_lng, radius_km=5.0)
        
        if not drivers:
            return None
        
        # drivers is a list of (member, distance, (lat, lng)) items? 
        # Actually standard georadius withdist returns [(member, dist), ...]
        # We need to parse it. 
        # For simplicity, pick the first one (closest).
        nearest_driver = drivers[0] # (driver_id, distance)
        
        # Convert driver_id from bytes/string to int if needed
        return int(nearest_driver[0])

matching_engine = MatchingEngine()
