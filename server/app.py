"""
Paco Drawing Stats FastAPI Back-end
Written by Kerby Keith Aquino (skepfusky / Kokoro Husky)
MIT License
"""

import uvicorn
import json
from fastapi import FastAPI, Request

app = FastAPI(debug=True)

@app.get("/artwork")
def artwork():
    artwork_data: object = json.load("paco-fa-database.json")
    return artwork_data

@app.get("/characters")
def characters():
    character_data: object = json.load("characters-example.json")
    return character_data

if __name__ == "__main__":
    uvicorn.run("fastapi_code:app")
