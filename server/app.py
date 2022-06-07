"""
Paco Drawing Stats FastAPI Back-end
Written by Kerby Keith Aquino (skepfusky / Kokoro Husky)
MIT License
"""

import argparse
import uvicorn
import json
from fastapi import FastAPI

parser = argparse.ArgumentParser(description="Paco Drawing Stats FastAPI Back-end written in Python")

parser.add_argument("--prod", action="store_true", help="Run the build/production app")

args = parser.parse_args()
config = vars(args)
print(config)

app = FastAPI()

@app.get("/")
def main():
  return {"message": "test"}

@app.get("/artwork")
def artwork():
    artwork_data: object = json.load("paco-fa-database.json")
    return artwork_data

@app.get("/character")
def character():
    character_data: object = json.load("character-example.json")
    return character_data

if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)
