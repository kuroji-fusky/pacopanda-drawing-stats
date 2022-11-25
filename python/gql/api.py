import argparse
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from utils import success_msg

parser = argparse.ArgumentParser(description="FastAPI crap")
parser.add_argument('--prod', action="store_true",
                    help="Run the API in production mode")

args = parser.parse_args()

app = FastAPI()


class Artwork(BaseModel):
  title: str
  date: str
  characters: list[str]


class Character(BaseModel):
  name: str
  full_name: str
  species: str
  hybrid: bool


@app.get("/")
async def root():
  return {"message": "Oh daddy"}

if __name__ == '__main__':
  if args.prod:
    success_msg("--prod flag detected: running API in Production Mode")
    uvicorn.run("app:app", host="127.0.0.1", port=5000)
  else:
    uvicorn.run("app:app", host="127.0.0.1",
                post=5000, reload=True, debug=True)
