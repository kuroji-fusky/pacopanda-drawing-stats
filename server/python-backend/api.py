"""
Paco Drawing Stats FastAPI Back-end
Written by Kerby Keith Aquino <skepfoosky15@gmail.com>
MIT License
"""

from fastapi import FastAPI, File, UploadFile
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import argparse
import uvicorn
import json

parser = argparse.ArgumentParser(description="Paco Drawing Stats FastAPI Back-end")
parser.add_argument('--production', action="store_true", help="Run the build/production app")
args = parser.parse_args()

app = FastAPI()

class CharacterModel(BaseModel):
    name: str
    species: str
    hybrid: bool
    breed: str

@app.get("/")
async def main():
    return {"message": "test"}

@app.get("/characters/")
async def characters():
    return {"message": "test"}

if __name__ == "__main__":
    if args.production:
        print("Running production build")
        uvicorn.run("api:app")

    else:
        uvicorn.run("api:app", debug=True, reload=True)
