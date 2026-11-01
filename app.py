from fastapi import FastAPI

app = FastAPI(
    title="hello-service",
    description="Simple Hello World REST API",
    version="1.0.0",
)

@app.get("/health")
def health():
    return {"status": "UP", "application": "hello-service"}

@app.get("/api/hello")
def hello():
    return {"application": "hello-service", "message": "Hello from Python!"}

