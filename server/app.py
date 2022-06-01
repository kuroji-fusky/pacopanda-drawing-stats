"""
Paco Drawing Stats FastAPI Back-end
Written by Kerby Keith Aquino (skepfusky / Kokoro Husky)
MIT License
"""

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World!"}
  
if __name__ == "__main__":
    uvicorn.run("fastapi_code:app")
