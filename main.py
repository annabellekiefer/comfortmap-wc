from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.kobo import fetch_kobo_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # adjust for your frontend URLs if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/kobo-data")
async def get_kobo_data():
    return await fetch_kobo_data()

# Serve your frontend files from / (root URL)
app.mount("/", StaticFiles(directory="static", html=True), name="static")
