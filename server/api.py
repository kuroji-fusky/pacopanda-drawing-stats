"""
Paco Drawing Stats FastAPI Back-end
Written by Kerby Keith Aquino (skepfusky / Kokoro Husky)
MIT License
"""

import argparse
import uvicorn
import json
from fastapi import FastAPI, File, UploadFile
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

parser = argparse.ArgumentParser(
    description="Paco Drawing Stats FastAPI Back-end written in Python")

parser.add_argument("--prod", action="store_true",
                    help="Run the build/production app")

args = parser.parse_args()
config = vars(args)
print(config)

app = FastAPI()


class CharacterModel(BaseModel):
    name: str
    species: str
    hybrid: bool
    breed: str | null = None


@app.get("/")
async def main():
    return {"message": "test"}


@app.get("/characters/")
async def characters():
    return {"message": "test"}


if __name__ == "__main__":
    uvicorn.run("api:app", reload=True)
