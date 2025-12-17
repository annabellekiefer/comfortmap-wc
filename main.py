from fastapi import FastAPI
from app.kobo import fetch_kobo_data

app = FastAPI()

@app.get("/kobo-data")
async def get_kobo_data():
    data = await fetch_kobo_data()
    return data
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.kobo import fetch_kobo_data

app = FastAPI()

# Allow requests from your frontend origin (adjust as needed)
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    # add other origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] to allow all origins (less secure)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/kobo-data")
async def get_kobo_data():
    data = await fetch_kobo_data()
    return data
