import httpx
from fastapi import HTTPException

KOBO_API_URL = "https://kf.kobotoolbox.org/api/v2/assets/a5DffPT6s6zBJbwdHfFHn5/data/"

async def fetch_kobo_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(KOBO_API_URL)
        if response.status_code != 200:
            raise HTTPException(status_code=502, detail="Failed to fetch data from Kobo API")
        return response.json()
