from fastapi import FastAPI

app = FastAPI()

@app.get("/initiate")
async def root():
    return "Microservice is successfully triggered"