from fastapi import FastAPI

app = FastAPI(openapi_url="/api/v1/skipper/tasks/openapi.json",
              docs_url="/api/v1/skipper/tasks/docs")

@app.get("/initiate")
async def root():
    return "Microservice is successfully triggered"