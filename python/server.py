import argparse
import uvicorn
from typing import Literal
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

### Argparse ###
parser = argparse.ArgumentParser()
parser.add_argument("--prod",
                    action="store_true",
                    help="Runs the server in production mode, disables reload mode")

args = parser.parse_args()

### FastAPI ###
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
    referer = str(request.base_url).strip("/")

    return {
        "version": "1",
        "source_code": "https://github.com/kuroji-fusky/pacopanda-drawing-stats",
        "artworks_url": f"{referer}/artworks",
        "artwork_url": referer + "/artwork{/artworks}",
        "characters_url": f"{referer}/characters",
        "character_url": referer + "/character{/characters}",
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

if __name__ == "__main__":
    __ASGIAppName = "server:app"
    if not args.prod:
        uvicorn.run(__ASGIAppName, host="127.0.0.1", port=4000)
    else:
        uvicorn.run(__ASGIAppName, host="127.0.0.1", port=4000, reload=True)
