from typing import Literal
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:8000",
        "http://localhost:5173",
        "https://pacopandastats.kurojifusky.com"
    ],
)

QueryLimit = Literal["all"] | int


@app.get("/")
async def root(request: Request):
    referer = request.client.host

    return {
        "artworks_url": f"{referer}/artworks",
        "characters_url": f"{referer}/characters",
    }


@app.get("/artworks")
async def artworks_list(year: int = 2023, limit: QueryLimit = "all"):
    pass


@app.get("/characters")
async def characters_list(year: int = 2023, limit: QueryLimit = "all"):
    pass


@app.get("/character/{character}")
async def character(character: str):
    pass
