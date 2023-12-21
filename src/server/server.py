import argparse
import uvicorn
from datetime import datetime
from typing import Literal
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .logger import log

parser = argparse.ArgumentParser()
parser.add_argument("--prod",
                    action="store_true",
                    help="Runs the server in production mode, disables reload")

args = parser.parse_args()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:8000",
        "http://localhost:5173",
        "https://pds.kurojifusky.com"
    ],
)

QueryLimit = Literal["all"] | int


@app.get("/")
async def root(request: Request):
    referer = str(request.base_url).strip("/")

    return {
        "version": "1",
        "source_code": "https://github.com/kuroji-fusky/pacopanda-drawing-stats",
        "characters_url": f"{referer}/characters",
        "character_url": referer + "/character{/characters}",
        "character_apperances_url": referer + "/character{/characters}/appearances",
        "artworks_url": f"{referer}/artworks",
        "artwork_url": referer + "/artwork{/artworks}",
    }


# Ex: /character{/paco}
@app.get("/character/{character}")
async def character(character: str):
    pass


# /character{/paco}/appearances{?items,year}
@app.get("/character/{character}/appearances")
async def character(character: str, year: int, items: str):
    pass


# /characters{?items,year}
@app.get("/characters")
async def characters_list(year: int, items: str):
    pass


# Ex: /artwork{/big-tree}
@app.get("/artwork/{artwork}")
async def artworks_list(artwork: str):
    pass


# /artworks{?items,year}
@app.get("/artworks")
async def artworks_list(year: int, items: str):
    pass


if __name__ == "__main__":
    APP_NAME, HOST, PORT = "server:app", "localhost", 4000

    if not args.prod:
        log("info", "Running server in production")
        uvicorn.run(APP_NAME, host=HOST, port=PORT)
    else:
        log("info", "Running server")
        uvicorn.run(APP_NAME, host=HOST, port=PORT, reload=True)
