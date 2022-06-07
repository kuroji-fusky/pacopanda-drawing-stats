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

router = FastAPI()

@router.get("/")
def main():
    return {"message": "test"}


@router.post("/artwork/")
async def get_artwork():
    return {"message": "test"}

@router.get("/artwork/")
def artwork():
    return {"message": "wow"}

@router.post("/character")
def get_character():
    json_data = jsonable_encoder("character-example.json")
    return json_data


@router.get("/character")
def character():
    character_data: object = json.loads("character-example.json")
    return character_data

if __name__ == "__main__":
    uvicorn.run("app:router", reload=True)
